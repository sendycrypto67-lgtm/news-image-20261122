#!/usr/bin/env python3
"""Copy entry.png to the output directory after validating it.

The entry is a single 1024x1024 newspaper front page, entry.png, stored
next to this file. This program checks that the file is a whole, valid
PNG within the competition limits and copies it byte for byte to
$MAKEFUN_OUTPUT_DIR (or /output when unset), then verifies the copy.

Standard library only. No network, no randomness.
"""

import hashlib
import os
import shutil
import struct
import sys

MAX_BYTES = 1048576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def read_dimensions(data, path):
    """Return (width, height) after checking the PNG magic and IHDR chunk."""
    if len(data) < 8 or data[:8] != PNG_MAGIC:
        fail(path + " is not a PNG file (bad magic bytes)")
    if len(data) < 33:
        fail(path + " is too short to hold a PNG header")
    ihdr_len = struct.unpack(">I", data[8:12])[0]
    if data[12:16] != b"IHDR":
        fail(path + " has no IHDR chunk where one is expected")
    if ihdr_len != 13:
        fail(path + " has an IHDR chunk of length %d, expected 13" % ihdr_len)
    width, height = struct.unpack(">II", data[16:24])
    if width == 0 or height == 0:
        fail(path + " has zero width or height")
    if width > MAX_SIDE or height > MAX_SIDE:
        fail(
            "%s is %dx%d, larger than the %dx%d limit"
            % (path, width, height, MAX_SIDE, MAX_SIDE)
        )
    return width, height


def check_iend(data, path):
    """Check the last 12 bytes are a well-formed IEND chunk."""
    if len(data) < 12:
        fail(path + " is too short to hold an IEND chunk")
    tail = data[-12:]
    if tail[0:4] != b"\x00\x00\x00\x00" or tail[4:8] != b"IEND":
        fail(path + " has no IEND chunk at the end of the file")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    try:
        with open(source, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        fail("cannot read " + source + ": " + str(exc))
    if len(data) > MAX_BYTES:
        fail(
            "%s is %d bytes, over the %d byte limit"
            % (source, len(data), MAX_BYTES)
        )
    width, height = read_dimensions(data, source)
    check_iend(data, source)
    digest = hashlib.sha256(data).hexdigest()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    try:
        shutil.copyfile(source, dest)
    except OSError as exc:
        fail("cannot write " + dest + ": " + str(exc))
    try:
        with open(dest, "rb") as handle:
            copied = handle.read()
    except OSError as exc:
        fail("cannot re-read " + dest + ": " + str(exc))
    if hashlib.sha256(copied).hexdigest() != digest:
        fail(dest + " sha256 does not match " + source)
    if len(copied) != len(data):
        fail(dest + " size does not match " + source)
    copy_width, copy_height = read_dimensions(copied, dest)
    if (copy_width, copy_height) != (width, height):
        fail(dest + " dimensions do not match " + source)
    print("source: " + source)
    print("dimensions: %dx%d" % (width, height))
    print("size: %d bytes" % len(data))
    print("sha256: " + digest)
    print("destination: " + dest)


if __name__ == "__main__":
    main()
