"""Remove a (near-)white studio background from a product photo, producing
a transparent PNG that `crop_products.py` can then crop to bbox.

The vendor/user-supplied photos in this project are clean studio shots on
a white or off-white seamless background, so a border-connected flood fill
on "whitish" pixels is enough — no ML segmentation needed. Flood fill runs
on a small downscaled copy for speed, then the mask is upscaled back with
smooth resampling so the cutout edge isn't jagged.

Usage:
    python3 remove_white_bg.py <src.jpg> <dst-transparent.png> [white_thresh]
or import remove_white_bg() directly.
"""
import sys
from collections import deque

from PIL import Image


def _flood_bg_mask(small_rgb, white_thresh):
    w, h = small_rgb.size
    px = small_rgb.load()

    def is_bg(x, y):
        r, g, b = px[x, y]
        mn, mx = min(r, g, b), max(r, g, b)
        return mn > white_thresh and (mx - mn) < 30

    visited = bytearray(w * h)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if is_bg(x, y) and not visited[y * w + x]:
                visited[y * w + x] = 1
                q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if is_bg(x, y) and not visited[y * w + x]:
                visited[y * w + x] = 1
                q.append((x, y))

    while q:
        x, y = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not visited[ny * w + nx]:
                if is_bg(nx, ny):
                    visited[ny * w + nx] = 1
                    q.append((nx, ny))

    mask = Image.frombytes("L", (w, h), bytes(255 if v else 0 for v in visited))
    return mask


def _fill_enclosed_holes(small_rgb, border_bg_mask, hole_thresh=236, max_area_frac=0.35):
    """Catch bright see-through gaps (armrest loops, base gaps) that the
    border flood fill can't reach because they don't touch the image edge.
    Only small, very-white islands are removed, so a genuinely light-
    colored chair (gray/taupe) doesn't get eaten."""
    w, h = small_rgb.size
    px = small_rgb.load()
    already = border_bg_mask.load()
    max_area = w * h * max_area_frac

    def is_hole_candidate(x, y):
        if already[x, y]:
            return False
        r, g, b = px[x, y]
        mn, mx = min(r, g, b), max(r, g, b)
        return mn > hole_thresh and (mx - mn) < 20

    visited = bytearray(w * h)
    out = bytearray(w * h)
    for y in range(h):
        for x in range(w):
            idx = y * w + x
            if visited[idx] or not is_hole_candidate(x, y):
                continue
            comp = [(x, y)]
            visited[idx] = 1
            q = deque([(x, y)])
            touches_border = x == 0 or y == 0 or x == w - 1 or y == h - 1
            while q:
                cx, cy = q.popleft()
                for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                    if 0 <= nx < w and 0 <= ny < h and not visited[ny * w + nx]:
                        if is_hole_candidate(nx, ny):
                            visited[ny * w + nx] = 1
                            if nx == 0 or ny == 0 or nx == w - 1 or ny == h - 1:
                                touches_border = True
                            comp.append((nx, ny))
                            q.append((nx, ny))
            if not touches_border and len(comp) <= max_area:
                for cx, cy in comp:
                    out[cy * w + cx] = 255
    return Image.frombytes("L", (w, h), bytes(out))


def remove_white_bg(src, dst, white_thresh=205, work_size=500):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    scale = work_size / max(w, h)
    small = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)

    bg_mask_small = _flood_bg_mask(small, white_thresh)
    holes_small = _fill_enclosed_holes(small, bg_mask_small)
    combined_small = Image.frombytes(
        "L", small.size, bytes(max(a, b) for a, b in zip(bg_mask_small.tobytes(), holes_small.tobytes()))
    )
    bg_mask = combined_small.resize((w, h), Image.LANCZOS)

    rgba = im.convert("RGBA")
    alpha = Image.eval(bg_mask, lambda a: 255 - a)
    rgba.putalpha(alpha)
    rgba.save(dst)


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    thresh = int(sys.argv[3]) if len(sys.argv) > 3 else 205
    remove_white_bg(src, dst, thresh)
    print(f"removed background {src} -> {dst} (white_thresh={thresh})")
