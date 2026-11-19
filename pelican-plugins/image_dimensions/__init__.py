"""
Image Dimensions Plugin
=======================

Sets ``image_width`` and ``image_height`` on articles and pages whose
``Image`` metadata points to a local file, so templates can emit
``width``/``height`` attributes and the browser reserves space before the
image loads (no layout shift).

Reads PNG, GIF, JPEG and WebP headers directly; no Pillow dependency.
Remote URLs and unreadable files are skipped silently.

Usage:
    Add 'image_dimensions' to PLUGINS in pelicanconf.py
"""

import logging
import struct
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlparse

from pelican import signals

logger = logging.getLogger(__name__)

_JPEG_SOF = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}


def _jpeg_size(f):
    f.seek(2)
    while True:
        byte = f.read(1)
        while byte and byte != b"\xff":
            byte = f.read(1)
        while byte == b"\xff":
            byte = f.read(1)
        if not byte:
            return None
        marker = byte[0]
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            continue
        (length,) = struct.unpack(">H", f.read(2))
        if marker in _JPEG_SOF:
            height, width = struct.unpack(">xHH", f.read(5))
            return width, height
        f.seek(length - 2, 1)


def read_image_size(path):
    """Return (width, height) of a PNG/GIF/JPEG/WebP file, or None."""
    try:
        with open(path, "rb") as f:
            head = f.read(30)
            if head.startswith(b"\x89PNG\r\n\x1a\n"):
                return struct.unpack(">II", head[16:24])
            if head[:6] in (b"GIF87a", b"GIF89a"):
                return struct.unpack("<HH", head[6:10])
            if head.startswith(b"\xff\xd8"):
                return _jpeg_size(f)
            if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
                chunk = head[12:16]
                if chunk == b"VP8 ":
                    w, h = struct.unpack("<HH", head[26:30])
                    return w & 0x3FFF, h & 0x3FFF
                if chunk == b"VP8L":
                    b = head[21:25]
                    w = 1 + (((b[1] & 0x3F) << 8) | b[0])
                    h = 1 + (((b[3] & 0x0F) << 10) | (b[2] << 2) | ((b[1] & 0xC0) >> 6))
                    return w, h
                if chunk == b"VP8X":
                    w = 1 + int.from_bytes(head[24:27], "little")
                    h = 1 + int.from_bytes(f.read(3), "little")
                    return w, h
    except (OSError, struct.error, IndexError):
        return None
    return None


@lru_cache(maxsize=None)
def _cached_size(path):
    return read_image_size(path)


def resolve_local_image(image, content_path, siteurl=""):
    """Map an ``Image`` value to a file under the content directory."""
    if not image:
        return None
    if siteurl and image.startswith(siteurl):
        image = image[len(siteurl):]
    parsed = urlparse(image)
    if parsed.scheme or parsed.netloc:
        return None
    candidate = Path(content_path) / parsed.path.lstrip("/")
    return candidate if candidate.is_file() else None


def add_dimensions(content):
    image = getattr(content, "image", None)
    if not image or getattr(content, "image_width", None):
        return
    settings = content.settings
    path = resolve_local_image(image, settings.get("PATH", "content"), settings.get("SITEURL", ""))
    if path is None:
        return
    size = _cached_size(str(path))
    if size:
        content.image_width, content.image_height = size
    else:
        logger.debug("image_dimensions: could not read size of %s", path)


def register():
    signals.content_object_init.connect(add_dimensions)
