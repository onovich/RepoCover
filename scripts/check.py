#!/usr/bin/env python3

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "repo-cover"
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
    for path in (SKILL / "scripts").glob("*.mjs"):
        subprocess.run([node, "--check", str(path)], check=True)


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
    check_skill_references()
    check_sources()
    check_images()
    print(
        "RepoCover checks passed: metadata, skill references, UTF-8, syntax, "
        f"and {len(EXPECTED_EXAMPLES) + 1} preview images."
    )


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, UnicodeError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
        print(f"RepoCover check failed: {error}", file=sys.stderr)
        sys.exit(1)
