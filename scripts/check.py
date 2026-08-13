#!/usr/bin/env python3

import json
import re
import subprocess
import sys
from pathlib import Path


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
    images.append(ROOT / "docs" / "social-preview.png")
    if len(images) != 5:
        fail(f"Expected four examples and one product preview; got {len(images)} images")

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
    check_sources()
    check_images()
    print("RepoCover checks passed: metadata, UTF-8, syntax, and 5 preview images.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, UnicodeError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
        print(f"RepoCover check failed: {error}", file=sys.stderr)
        sys.exit(1)
