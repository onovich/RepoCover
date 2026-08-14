#!/usr/bin/env python3

import json
import re
import struct
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

from build_site import build as build_site, load_site_config


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "repo-cover"
PLUGIN = ROOT / ".codex-plugin" / "plugin.json"
PLUGIN_SKILL = ROOT / "skills" / "repo-cover"
SITE = ROOT / "site"
TEXT_SUFFIXES = {
    ".json",
    ".html",
    ".css",
    ".js",
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
    "research.png",
}
EXAMPLE_REPOSITORIES = {
    "Research": "https://github.com/onovich/Research",
    "PrismDraft": "https://github.com/onovich/PrismDraft",
    "LittlePNG": "https://github.com/onovich/LitPng",
    "DeskMochi": "https://github.com/onovich/DeskMochi",
    "AudioTrim": "https://github.com/onovich/AudioTrim",
    "Beat": "https://github.com/onovich/Beat",
    "JustGoal.skill": "https://github.com/onovich/JustGoal.skill",
    "Knot": "https://github.com/onovich/Knot",
    "Ping": "https://github.com/onovich/Ping",
}
EXPECTED_SOCIAL_ASSETS = {
    "repocover-launch-landscape.png": (1600, 1000),
    "repocover-linkedin-en.png": (1200, 627),
    "repocover-linkedin-zh.png": (1200, 627),
    "repocover-portrait-en.png": (1080, 1350),
    "repocover-portrait-zh.png": (1080, 1350),
    "repocover-product-hunt-gallery.png": (1270, 760),
    "repocover-product-hunt-thumbnail.png": (240, 240),
    "repocover-square-en.png": (1080, 1080),
    "repocover-square-zh.png": (1080, 1080),
    "repocover-x-en.png": (1280, 640),
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
    site_config = load_site_config()
    canonical_prefix = site_config["origin"] + site_config["base_path"]
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
                canonical_prefix
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
        if canonical_prefix + "sitemap.xml" not in robots:
            fail("robots.txt must advertise the canonical sitemap")

        for path in output.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in {".html", ".json", ".txt", ".xml"}:
                continue
            text = path.read_text(encoding="utf-8")
            if "{{SITE_" in text:
                fail(f"Site build contains an unresolved URL token: {path.relative_to(output)}")
            if "https://blog.onovich.com/RepoCover" in text:
                fail(f"Site build still refers to the legacy origin: {path.relative_to(output)}")
            if path.suffix.lower() == ".html" and (
                'href="https://github.com/onovich"' in text
                or '"url": "https://github.com/onovich"' in text
            ):
                fail(
                    "Site must not link directly to the author's GitHub profile: "
                    f"{path.relative_to(output)}"
                )

        for required in (
            "assets/app.js",
            "assets/repo-cover-mark.svg",
            "assets/social-preview.png",
            "assets/styles.css",
            ".nojekyll",
        ):
            if not (output / required).is_file():
                fail(f"Site build is missing {required}")

        for filename in EXPECTED_SOCIAL_ASSETS:
            required = output / "assets" / "social" / filename
            if not required.is_file():
                fail(f"Site build is missing assets/social/{filename}")

        seo_pages = (
            "index.html",
            "zh/index.html",
            "examples/index.html",
            "zh/examples/index.html",
            "github-social-preview-guide/index.html",
            "zh/github-social-preview-guide/index.html",
        )
        required_social_metadata = (
            'property="og:site_name"',
            'property="og:locale"',
            'property="og:image:type"',
            'property="og:image:width"',
            'property="og:image:height"',
            'property="og:image:alt"',
            'name="twitter:title"',
            'name="twitter:description"',
            'name="twitter:image"',
            'name="twitter:image:alt"',
        )
        for relative in seo_pages:
            text = (output / relative).read_text(encoding="utf-8")
            for marker in required_social_metadata:
                if marker not in text:
                    fail(f"SEO page is missing {marker}: {relative}")
            json_ld_blocks = re.findall(
                r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
                text,
                re.DOTALL,
            )
            if not json_ld_blocks:
                fail(f"SEO page is missing JSON-LD: {relative}")
            for block in json_ld_blocks:
                json.loads(block)

        sitemap_text = (output / "sitemap.xml").read_text(encoding="utf-8")
        if sitemap_text.count('hreflang="x-default"') < 6:
            fail("Sitemap must include x-default for every bilingual content page")

        homepage_text = (output / "index.html").read_text(encoding="utf-8")
        homepage_zh_text = (output / "zh" / "index.html").read_text(encoding="utf-8")
        examples_text = (output / "examples" / "index.html").read_text(encoding="utf-8")
        examples_zh_text = (output / "zh" / "examples" / "index.html").read_text(
            encoding="utf-8"
        )

        retired_public_copy = (
            "300+",
            "more than 300 repositories",
            "三百多",
            "restart Codex",
            "Restart Codex",
            "重启 Codex",
            "hero image",
            "Hero asset",
            "Cold start",
            "The short version.",
            "简单说。",
            "Same constraints. No shared template.",
            "相同的规格，不共用一套模板。",
            "No project needs all three.",
            "不需要同时具备。",
            "Three starting points",
            "三种起点",
            "Separate actions",
            "操作分开",
            "Automatically checked",
            "自动检查",
            "pretending an earlier cover exists",
            "也不假设以前已有封面",
        )
        repository_copy = (ROOT / "README.md").read_text(encoding="utf-8")
        repository_copy += (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        launch_copy = (ROOT / "docs" / "LAUNCH_KIT.md").read_text(encoding="utf-8")
        public_copy = (
            homepage_text
            + homepage_zh_text
            + examples_text
            + examples_zh_text
            + repository_copy
            + launch_copy
        )
        for phrase in retired_public_copy:
            if phrase in public_copy:
                fail(f"Site still contains retired public wording: {phrase}")

        retired_site_copy = (
            "Browse real covers",
            "查看真实案例",
            "Featured case",
            "Working product",
            "重点案例",
            "可运行产品",
            "Real repositories, recognizable Social Previews",
            "真实仓库，也能有一眼可认的 Social Preview",
        )
        site_copy = homepage_text + homepage_zh_text + examples_text + examples_zh_text
        for phrase in retired_site_copy:
            if phrase in site_copy:
                fail(f"Site still contains retired example wording: {phrase}")

        for required_phrase in (
            "Create a distinctive cover for your",
            "为你的代码仓库，",
            "有辨识度的封面。",
            "Best size for GitHub Social Preview",
            "GitHub Social Preview 最佳显示规格",
            "What is Social Preview, and how do I set it?",
            "了解 Social Preview 是什么，以及如何设置",
            "Three situations",
            "三种情况",
            "Open your AI agent—Codex is recommended—and send it these two messages in order.",
            "打开你的 AI Agent 工具（首选 Codex），把下面两句话依次发给它。",
            "Install the Skill from https://github.com/onovich/RepoCover.",
            "安装 https://github.com/onovich/RepoCover 的 Skill。",
            "Use $repo-cover to create a cover for the current project.",
            "使用 $repo-cover 为当前项目生成封面。",
        ):
            if required_phrase not in public_copy:
                fail(f"Site is missing required plain-language copy: {required_phrase}")

        for relative, text in (
            ("examples/index.html", examples_text),
            ("zh/examples/index.html", examples_zh_text),
        ):
            for repository_name, repository_url in EXAMPLE_REPOSITORIES.items():
                if not re.search(
                    rf'<h2[^>]*translate="no"[^>]*>{re.escape(repository_name)}</h2>',
                    text,
                ):
                    fail(
                        f"Repository name must remain untranslated in {relative}: "
                        f"{repository_name}"
                    )
                if not re.search(
                    rf'<a\s+class="example-card"\s+href="{re.escape(repository_url)}"',
                    text,
                ):
                    fail(
                        f"Example must link to its public repository in {relative}: "
                        f"{repository_name}"
                    )


def check_images() -> None:
    social_directory = ROOT / "assets" / "social"
    actual_social_assets = {path.name for path in social_directory.glob("*.png")}
    if actual_social_assets != set(EXPECTED_SOCIAL_ASSETS):
        fail(
            "Social asset set mismatch: "
            f"expected {sorted(EXPECTED_SOCIAL_ASSETS)}, got {sorted(actual_social_assets)}"
        )
    for filename, expected_dimensions in EXPECTED_SOCIAL_ASSETS.items():
        image = social_directory / filename
        header = image.read_bytes()[:24]
        if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
            fail(f"Social asset is not a valid PNG: {filename}")
        actual_dimensions = struct.unpack(">II", header[16:24])
        if actual_dimensions != expected_dimensions:
            fail(
                f"Social asset dimensions mismatch for {filename}: "
                f"expected {expected_dimensions}, got {actual_dimensions}"
            )
        if image.stat().st_size >= 5 * 1024 * 1024:
            fail(f"Social asset exceeds 5 MB: {filename}")

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

    research_svg = ROOT / "examples" / "research.svg"
    completed = subprocess.run(
        [
            sys.executable,
            str(validator),
            str(ROOT / "examples" / "research.png"),
            "--svg",
            str(research_svg),
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
        f"syntax, {len(EXPECTED_EXAMPLES) + 1} preview images, and "
        f"{len(EXPECTED_SOCIAL_ASSETS)} social assets."
    )


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, UnicodeError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
        print(f"RepoCover check failed: {error}", file=sys.stderr)
        sys.exit(1)
