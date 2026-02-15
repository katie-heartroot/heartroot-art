"""Optimize Katie's photos for web gallery."""
from PIL import Image
from pathlib import Path
import shutil

SRC = Path(r"C:\Users\rlack\Desktop\for-katie\photos-for-clara")
DST = Path(r"C:\Users\rlack\Desktop\katie-tudor\images")

# Map source files to clean web-friendly names
# Artwork photos
artwork = {
    "IMG_20260215_003443.png": "gold-pendant.jpg",
    "IMG_20260215_003503 (2).png": "gold-pendant-detail.jpg",
    "IMG_20260215_003451 (1).png": "wall-pocket.jpg",
    "IMG_20260215_003502 (1).png": "wall-pocket-alt.jpg",
    "IMG_20260215_003451.png": "sculpture-creatures.jpg",
    "IMG_20260215_003502 (2).png": "sculpture-creatures-alt.jpg",
    "IMG_20260215_003502.png": "sculpture-creatures-top.jpg",
    "IMG_20260215_003502 (3).png": "wall-sculpture-green.jpg",
    "IMG_20260215_003503 (1).png": "vessel-midnight.jpg",
    "IMG_20260215_003503.png": "fossil-platter.jpg",
}

# Katie photos
katie = {
    "20260214_233530.jpg": "katie-at-wheel.jpg",  # smiling at camera - best for About
    "20260214_233525.jpg": "katie-working.jpg",
    "20260214_233536.jpg": "katie-centering.jpg",
    "20260214_233553.jpg": "katie-setup.jpg",
}

MAX_WIDTH = 1200  # gallery images
MAX_WIDTH_THUMB = 600  # thumbnails
QUALITY = 82

def optimize(src_path, dst_path, max_width=MAX_WIDTH):
    img = Image.open(src_path)
    # Convert RGBA to RGB if needed
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    # Resize if wider than max
    w, h = img.size
    if w > max_width:
        ratio = max_width / w
        new_size = (max_width, int(h * ratio))
        img = img.resize(new_size, Image.LANCZOS)
    img.save(dst_path, 'JPEG', quality=QUALITY, optimize=True)
    size_kb = dst_path.stat().st_size / 1024
    print(f"  {dst_path.name}: {img.size[0]}x{img.size[1]}, {size_kb:.0f}KB")

print("=== Optimizing artwork ===")
for src_name, dst_name in artwork.items():
    src = SRC / src_name
    if src.exists():
        optimize(src, DST / dst_name)
    else:
        print(f"  MISSING: {src_name}")

print("\n=== Optimizing Katie photos ===")
for src_name, dst_name in katie.items():
    src = SRC / src_name
    if src.exists():
        optimize(src, DST / dst_name)
    else:
        print(f"  MISSING: {src_name}")

print("\nDone!")
