#!/usr/bin/env python3

import json
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

from build_site import build as build_site


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "repo-cover"
PLUGIN = ROOT / ".codex-plugin" / "plugin.json"
PLUGIN_SKILL = ROOT / "skills" / "repo-cover"
SITE = ROOT / "site"
TEXT_SUFFIXES = {
    ".json",
    ".md",
    ".mjs",
    ".py",
    ".svg",
    ".toml",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
TEXT_NAMES = {".gitattributes", ".gitignore", "LICENSE"}
EXPECTED_EXAMPLES = {
    "audiotrim.png",
    "beat.png",
    "deskmochi.png",
    "justgoal-skill.png",
    "knot.png",
    "littlepng.png",
    "ping.png",
    "prismdraft.png",
}
REQUIRED_REFERENCES = {
    "cold-start.md",
    "common-quality.md",
    "design-ledger-template.md",
    "design-recipes.md",
    "source-material.md",
    "version-regression.md",
}
EXPECTED_SITE_PAGES = {
    "404.html",
    "index.html",
    "examples/index.html",
    "github-social-preview-guide/index.html",
    "privacy/index.html",
    "support/index.html",
    "terms/index.html",
    "zh/index.html",
    "zh/examples/index.html",
    "zh/github-social-preview-guide/index.html",
    "zh/privacy/index.html",
    "zh/support/index.html",
    "zh/terms/index.html",
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.canonical = ""
        self.description = ""
        self.alternate_languages = set()
        self.in_title = False
        self.lang = ""
        self.references = []
        self.title_parts = []
        self.images_without_alt = []

    def handle_starttag(self, tag: str, attrs) -> None:
        values = dict(attrs)
        if tag == "html":
            self.lang = values.get("lang", "")
        elif tag == "title":
            self.in_title = True
        elif tag == "meta" and values.get("name", "").lower() == "description":
            self.description = values.get("content", "").strip()
        elif tag == "link" and "canonical" in values.get("rel", "").split():
            self.canonical = values.get("href", "").strip()
        elif tag == "link" and "alternate" in values.get("rel", "").split():
            if values.get("hreflang"):
                self.alternate_languages.add(values["hreflang"])

        for key in ("href", "src"):
            if key in values:
                self.references.append(values[key])

        if tag == "img" and "alt" not in values:
            self.images_without_alt.append(values.get("src", "<unknown>"))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

    @property
    def title(self) -> str:
        return "".join(self.title_parts).strip()


def fail(message: str) -> None:
    raise RuntimeError(message)


def check_utf8_without_bom() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in TEXT_NAMES:
            continue
        data = path.read_bytes()
        if data.startswith(b"\xef\xbb\xbf"):
            fail(f"UTF-8 BOM is not allowed: {path.relative_to(ROOT)}")
        data.decode("utf-8")


def check_metadata() -> None:
    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not re.search(r"(?m)^name: repo-cover$", skill_text):
        fail("SKILL.md must declare name: repo-cover")
    if "Create or refresh" not in skill_text and "creates or refreshes" not in skill_text:
        fail("SKILL.md description no longer describes creation or refresh behavior")

    interface_text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
    for expected in ('display_name: "RepoCover"', "$repo-cover"):
        if expected not in interface_text:
            fail(f"agents/openai.yaml is missing {expected!r}")


def check_plugin_manifest() -> None:
    manifest = json.loads(PLUGIN.read_text(encoding="utf-8"))
    if manifest.get("name") != "repo-cover":
        fail("Plugin manifest name must be repo-cover")
    if not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")):
        fail("Plugin manifest must use a stable semantic version")
    if manifest.get("skills") != "./skills/":
        fail("Plugin manifest must point at the required ./skills/ package directory")

    interface = manifest.get("interface", {})
    for key in ("displayName", "shortDescription", "longDescription", "developerName"):
        if not interface.get(key):
            fail(f"Plugin interface is missing {key}")
    if interface.get("displayName") != "RepoCover":
        fail("Plugin displayName must be RepoCover")

    for key in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL"):
        if not interface.get(key, "").startswith("https://"):
            fail(f"Plugin interface {key} must be an HTTPS URL")

    for key in ("composerIcon", "logo", "logoDark"):
        target = interface.get(key, "")
        if not target.startswith("./") or not (ROOT / target[2:]).is_file():
            fail(f"Plugin asset does not resolve: {key}={target!r}")
    for target in interface.get("screenshots", []):
        if not target.startswith("./assets/") or not (ROOT / target[2:]).is_file():
            fail(f"Plugin screenshot does not resolve under assets: {target!r}")

    source_files = {
        path.relative_to(SKILL).as_posix(): path
        for path in SKILL.rglob("*")
        if path.is_file()
    }
    packaged_files = {
        path.relative_to(PLUGIN_SKILL).as_posix(): path
        for path in PLUGIN_SKILL.rglob("*")
        if path.is_file()
    }
    if source_files.keys() != packaged_files.keys():
        fail("Packaged plugin skill file set is out of sync; run scripts/sync_plugin_skill.py")
    for relative, source in source_files.items():
        if source.read_bytes() != packaged_files[relative].read_bytes():
            fail(
                "Packaged plugin skill content is out of sync: "
                f"{relative}; run scripts/sync_plugin_skill.py"
            )


def check_skill_references() -> None:
    references = SKILL / "references"
    actual = {path.name for path in references.glob("*.md")}
    missing = REQUIRED_REFERENCES - actual
    if missing:
        fail(f"Missing required skill references: {', '.join(sorted(missing))}")

    markdown_link = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for source in [SKILL / "SKILL.md", *sorted(references.glob("*.md"))]:
        text = source.read_text(encoding="utf-8")
        for raw_target in markdown_link.findall(text):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            relative_target = unquote(target.split("#", 1)[0])
            resolved = (source.parent / relative_target).resolve()
            if not resolved.exists():
                fail(f"Broken relative Markdown link in {source.relative_to(ROOT)}: {target}")


def check_sources() -> None:
    for path in ROOT.rglob("*.py"):
        if ".git" not in path.parts:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")

    node = "node.exe" if sys.platform == "win32" else "node"
    for path in [
        *sorted((SKILL / "scripts").glob("*.mjs")),
        *sorted((ROOT / "scripts").glob("*.mjs")),
    ]:
        subprocess.run([node, "--check", str(path)], check=True)


def check_site() -> None:
    with tempfile.TemporaryDirectory(prefix="repocover-site-") as temporary:
        output = Path(temporary) / "site"
        build_site(output)
        canonical_urls = set()

        actual_pages = {
            path.relative_to(output).as_posix() for path in output.rglob("*.html")
        }
        if actual_pages != EXPECTED_SITE_PAGES:
            fail(
                "Site page set mismatch: "
                f"expected {sorted(EXPECTED_SITE_PAGES)}, got {sorted(actual_pages)}"
            )

        for relative in sorted(EXPECTED_SITE_PAGES):
            page = output / relative
            parser = PageParser()
            parser.feed(page.read_text(encoding="utf-8"))
            if not parser.lang:
                fail(f"Site page is missing html lang: {relative}")
            if not parser.title:
                fail(f"Site page is missing a title: {relative}")
            if relative != "404.html" and len(parser.title) > 70:
                fail(f"Site page title is longer than 70 characters: {relative}")
            if relative != "404.html" and not parser.description:
                fail(f"Site page is missing a meta description: {relative}")
            if relative != "404.html" and not parser.canonical.startswith(
                "https://blog.onovich.com/RepoCover/"
            ):
                fail(f"Site page has an invalid canonical URL: {relative}")
            if relative != "404.html":
                if parser.canonical in canonical_urls:
                    fail(f"Duplicate canonical URL: {parser.canonical}")
                canonical_urls.add(parser.canonical)
                if parser.alternate_languages != {"en", "zh-CN", "x-default"}:
                    fail(
                        f"Site page has incomplete hreflang links: {relative}: "
                        f"{sorted(parser.alternate_languages)}"
                    )
            if parser.images_without_alt:
                fail(
                    f"Site page has images without alt attributes: {relative}: "
                    f"{', '.join(parser.images_without_alt)}"
                )

            for reference in parser.references:
                parsed = urlparse(reference)
                if parsed.scheme or parsed.netloc or reference.startswith(("#", "/", "mailto:")):
                    continue
                target = (page.parent / unquote(parsed.path)).resolve()
                if reference.endswith("/") or target.is_dir():
                    target = target / "index.html"
                if not target.exists():
                    fail(f"Broken site reference in {relative}: {reference}")

        ET.parse(output / "sitemap.xml")
        robots = (output / "robots.txt").read_text(encoding="utf-8")
        if "https://blog.onovich.com/RepoCover/sitemap.xml" not in robots:
            fail("robots.txt must advertise the canonical sitemap")

        for required in (
            "assets/app.js",
            "assets/repo-cover-mark.svg",
            "assets/social-preview.png",
            "assets/styles.css",
            ".nojekyll",
        ):
            if not (output / required).is_file():
                fail(f"Site build is missing {required}")


def check_images() -> None:
    validator = SKILL / "scripts" / "validate_preview.py"
    images = sorted((ROOT / "examples").glob("*.png"))
    actual_examples = {image.name for image in images}
    if actual_examples != EXPECTED_EXAMPLES:
        fail(
            "Example image set mismatch: "
            f"expected {sorted(EXPECTED_EXAMPLES)}, got {sorted(actual_examples)}"
        )
    images.append(ROOT / "docs" / "social-preview.png")

    results = []
    for image in images:
        completed = subprocess.run(
            [sys.executable, str(validator), str(image)],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        results.append(json.loads(completed.stdout))

    product_svg = ROOT / "docs" / "social-preview.svg"
    completed = subprocess.run(
        [
            sys.executable,
            str(validator),
            str(ROOT / "docs" / "social-preview.png"),
            "--svg",
            str(product_svg),
        ],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    json.loads(completed.stdout)


def main() -> None:
    check_utf8_without_bom()
    check_metadata()
    check_plugin_manifest()
    check_skill_references()
    check_sources()
    check_site()
    check_images()
    print(
        "RepoCover checks passed: metadata, plugin, skill references, site, UTF-8, "
        f"syntax, and {len(EXPECTED_EXAMPLES) + 1} preview images."
    )


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, UnicodeError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
        print(f"RepoCover check failed: {error}", file=sys.stderr)
        sys.exit(1)
