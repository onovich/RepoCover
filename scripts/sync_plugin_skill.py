#!/usr/bin/env python3

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skill" / "repo-cover"
TARGET = ROOT / "skills" / "repo-cover"


def main() -> None:
    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, TARGET)
    print(f"Synced plugin skill from {SOURCE} to {TARGET}")


if __name__ == "__main__":
    main()
