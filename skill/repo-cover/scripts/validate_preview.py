#!/usr/bin/env python3

import argparse
import json
import re
import struct
import sys
from pathlib import Path
from xml.etree import ElementTree

EXPECTED_WIDTH = 1280
EXPECTED_HEIGHT = 640
MAX_BYTES = 1_000_000


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Validate a GitHub social preview raster and optional SVG source."
    )
    parser.add_argument("image", type=Path, help="PNG, JPG, JPEG, or GIF preview")
    parser.add_argument("--svg", type=Path, help="Optional editable SVG source")
    return parser.parse_args()


def read_dimensions(path):
    with path.open("rb") as stream:
        signature = stream.read(10)

        if signature.startswith(b"\x89PNG\r\n\x1a\n"):
            stream.seek(16)
            width, height = struct.unpack(">II", stream.read(8))
            return "png", width, height

        if signature[:6] in (b"GIF87a", b"GIF89a"):
            width, height = struct.unpack("<HH", signature[6:10])
            return "gif", width, height

        if signature[:2] == b"\xff\xd8":
            return "jpeg", *read_jpeg_dimensions(stream)

    raise ValueError("Unsupported or invalid image signature; use PNG, JPG, JPEG, or GIF.")


def read_jpeg_dimensions(stream):
    stream.seek(2)
    start_of_frame = {
        0xC0,
        0xC1,
        0xC2,
        0xC3,
        0xC5,
        0xC6,
        0xC7,
        0xC9,
        0xCA,
        0xCB,
        0xCD,
        0xCE,
        0xCF,
    }

    while True:
        byte = stream.read(1)
        if not byte:
            break
        if byte != b"\xff":
            continue

        marker = stream.read(1)
        while marker == b"\xff":
            marker = stream.read(1)
        if not marker:
            break

        marker_value = marker[0]
        if marker_value in (0x01, *range(0xD0, 0xD9)):
            continue

        length_bytes = stream.read(2)
        if len(length_bytes) != 2:
            break
        segment_length = struct.unpack(">H", length_bytes)[0]
        if segment_length < 2:
            raise ValueError("Invalid JPEG segment length.")

        if marker_value in start_of_frame:
            payload = stream.read(5)
            if len(payload) != 5:
                break
            height, width = struct.unpack(">HH", payload[1:5])
            return width, height

        stream.seek(segment_length - 2, 1)

    raise ValueError("Could not find JPEG dimensions.")


def parse_svg_number(value):
    if value is None:
        raise ValueError("SVG width and height are required.")
    match = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*(?:px)?\s*", value)
    if not match:
        raise ValueError(f"Unsupported SVG dimension: {value!r}")
    return float(match.group(1))


def validate_svg(path):
    if not path.is_file():
        raise ValueError(f"SVG source does not exist: {path}")

    root = ElementTree.parse(path).getroot()
    if root.tag.rsplit("}", 1)[-1] != "svg":
        raise ValueError("Editable source root must be <svg>.")

    width = parse_svg_number(root.get("width"))
    height = parse_svg_number(root.get("height"))
    view_box = [float(value) for value in (root.get("viewBox") or "").split()]

    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError("SVG must declare width=1280 and height=640.")
    if view_box != [0.0, 0.0, 1280.0, 640.0]:
        raise ValueError('SVG must declare viewBox="0 0 1280 640".')

    children = {child.tag.rsplit("}", 1)[-1]: child for child in root}
    for tag in ("title", "desc"):
        if tag not in children or not "".join(children[tag].itertext()).strip():
            raise ValueError(f"SVG must include a non-empty <{tag}> element.")

    return {"path": str(path.resolve()), "width": int(width), "height": int(height)}


def main():
    arguments = parse_arguments()
    image_path = arguments.image

    if not image_path.is_file():
        raise ValueError(f"Preview image does not exist: {image_path}")

    byte_size = image_path.stat().st_size
    image_format, width, height = read_dimensions(image_path)

    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(
            f"Preview must be exactly {EXPECTED_WIDTH}x{EXPECTED_HEIGHT}; got {width}x{height}."
        )
    if byte_size >= MAX_BYTES:
        raise ValueError(f"Preview must be under {MAX_BYTES} bytes; got {byte_size}.")

    result = {
        "ok": True,
        "image": {
            "path": str(image_path.resolve()),
            "format": image_format,
            "width": width,
            "height": height,
            "bytes": byte_size,
        },
    }
    if arguments.svg:
        result["svg"] = validate_svg(arguments.svg)

    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, ElementTree.ParseError) as error:
        print(f"repo-cover: {error}", file=sys.stderr)
        sys.exit(1)
