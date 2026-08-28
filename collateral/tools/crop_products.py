"""Crop a product PNG to its alpha-channel bounding box plus padding.

Every source product photo (as delivered from Drive) only used ~45-65% of
its own canvas, leaving huge transparent margins that made products look
small/lost inside the catalog's fixed-size beige frames. This crops each
image down to the actual chair silhouette, so `max-width`/`max-height` on
the <img> tags in the catalog HTML controls the real visible size instead
of mostly padding.

Usage:
    python3 crop_products.py <src.png> <dst-crop.png> [pad_frac]
or import crop_product() directly.
"""
import sys
from PIL import Image


def crop_product(src, dst, pad_frac=0.06):
    im = Image.open(src).convert("RGBA")
    alpha = im.split()[-1]
    bbox = alpha.point(lambda a: 255 if a > 12 else 0).getbbox()
    if bbox is None:
        im.save(dst)
        return
    left, top, right, bottom = bbox
    w, h = right - left, bottom - top
    pad_x, pad_y = int(w * pad_frac), int(h * pad_frac)
    left = max(0, left - pad_x)
    top = max(0, top - pad_y)
    right = min(im.width, right + pad_x)
    bottom = min(im.height, bottom + pad_y)
    im.crop((left, top, right, bottom)).save(dst)


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    pad = float(sys.argv[3]) if len(sys.argv) > 3 else 0.06
    crop_product(src, dst, pad)
    print(f"cropped {src} -> {dst} (pad_frac={pad})")
