#!/usr/bin/env python3

import argparse
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
CONFIG = SITE / "site.config.json"
TEXT_OUTPUT_SUFFIXES = {".html", ".json", ".txt", ".xml"}


def load_site_config() -> dict[str, str]:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    origin = config.get("origin", "").rstrip("/")
    base_path = "/" + config.get("basePath", "/").strip("/")
    if base_path != "/":
        base_path += "/"
    if not origin.startswith("https://"):
        raise ValueError("site.config.json origin must be an HTTPS URL")
    return {"origin": origin, "base_path": base_path}


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def build(output: Path) -> None:
    config = load_site_config()
    if output.exists():
        shutil.rmtree(output)

    shutil.copytree(SITE, output)
    (output / CONFIG.name).unlink()

    for image in sorted((ROOT / "examples").glob("*.png")):
        copy_file(image, output / "examples" / image.name)

    copy_file(ROOT / "docs" / "social-preview.png", output / "assets" / "social-preview.png")
    copy_file(ROOT / "assets" / "repo-cover-mark.svg", output / "assets" / "repo-cover-mark.svg")
    for image in sorted((ROOT / "assets" / "social").glob("*.png")):
        copy_file(image, output / "assets" / "social" / image.name)

    replacements = {
        "{{SITE_ORIGIN}}": config["origin"],
        "{{SITE_BASE_PATH}}": config["base_path"],
    }
    for path in output.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_OUTPUT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        for token, value in replacements.items():
            text = text.replace(token, value)
        path.write_text(text, encoding="utf-8")

    (output / ".nojekyll").write_text("", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the static RepoCover GitHub Pages site.")
    parser.add_argument("--output", type=Path, default=ROOT / ".site-dist")
    args = parser.parse_args()
    build(args.output.resolve())
    print(f"Built RepoCover site at {args.output.resolve()}")


if __name__ == "__main__":
    main()
