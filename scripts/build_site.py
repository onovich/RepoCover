#!/usr/bin/env python3

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def build(output: Path) -> None:
    if output.exists():
        shutil.rmtree(output)

    shutil.copytree(SITE, output)

    for image in sorted((ROOT / "examples").glob("*.png")):
        copy_file(image, output / "examples" / image.name)

    copy_file(ROOT / "docs" / "social-preview.png", output / "assets" / "social-preview.png")
    copy_file(ROOT / "assets" / "repo-cover-mark.svg", output / "assets" / "repo-cover-mark.svg")

    (output / ".nojekyll").write_text("", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the static RepoCover GitHub Pages site.")
    parser.add_argument("--output", type=Path, default=ROOT / ".site-dist")
    args = parser.parse_args()
    build(args.output.resolve())
    print(f"Built RepoCover site at {args.output.resolve()}")


if __name__ == "__main__":
    main()
