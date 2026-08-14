#!/usr/bin/env python3

import argparse
import json
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
CONFIG = SITE / "site.config.json"
SITEMAP = SITE / "sitemap.xml"
KEY_FILE = SITE / "indexnow-key.txt"
DEFAULT_ENDPOINT = "https://api.indexnow.org/indexnow"


def load_submission() -> dict[str, object]:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    origin = config["origin"].rstrip("/")
    parsed_origin = urlparse(origin)
    if parsed_origin.scheme != "https" or not parsed_origin.netloc:
        raise ValueError("site.config.json must contain an HTTPS origin")

    key = KEY_FILE.read_text(encoding="utf-8").strip()
    if not 8 <= len(key) <= 128 or not all(
        character.isalnum() or character == "-" for character in key
    ):
        raise ValueError("IndexNow key must be 8-128 letters, numbers, or dashes")

    sitemap_text = SITEMAP.read_text(encoding="utf-8").replace(
        "{{SITE_ORIGIN}}", origin
    )
    sitemap = ET.fromstring(sitemap_text)
    namespace = {"sitemap": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [
        element.text.strip()
        for element in sitemap.findall("sitemap:url/sitemap:loc", namespace)
        if element.text
    ]
    if not urls:
        raise ValueError("sitemap.xml contains no canonical URLs")
    if any(urlparse(url).netloc != parsed_origin.netloc for url in urls):
        raise ValueError("IndexNow submission may contain only canonical site URLs")

    return {
        "host": parsed_origin.netloc,
        "key": key,
        "keyLocation": f"{origin}/{KEY_FILE.name}",
        "urlList": urls,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Notify IndexNow-compatible search engines after a site deployment."
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    args = parser.parse_args()

    submission = load_submission()
    if args.dry_run:
        print(json.dumps(submission, ensure_ascii=False, indent=2))
        return

    request = urllib.request.Request(
        args.endpoint,
        data=json.dumps(submission).encode("utf-8"),
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "RepoCover-IndexNow/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status = response.status
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"IndexNow returned HTTP {error.code}: {detail}") from error

    if status not in {200, 202}:
        raise RuntimeError(f"IndexNow returned unexpected HTTP {status}")
    print(
        json.dumps(
            {"status": status, "submitted": len(submission["urlList"])},
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
