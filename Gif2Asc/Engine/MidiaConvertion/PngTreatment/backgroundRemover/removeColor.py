#!/usr/bin/env python3
"""removeColor — strips a target color (default: white) into transparency."""
from __future__ import annotations
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _common import (banner, gradient, box, progress, rgb, RESET,
                     glitch, list_pngs)
try:
    from PIL import Image
except ImportError:
    print("python -m pip install Pillow"); sys.exit(1)

def _hex(s: str) -> tuple[int,int,int]:
    s = s.strip().lstrip("#")
    if len(s) == 3: s = "".join(c*2 for c in s)
    return (int(s[0:2],16), int(s[2:4],16), int(s[4:6],16))

def run():
    banner("⟢ removeColor", "knock out a color → alpha")
    raw = input(rgb(0,220,255) + "  Hex color " + RESET +
                rgb(120,120,140) + "[FFFFFF]" + RESET + " > ").strip() or "FFFFFF"
    try: target = _hex(raw)
    except Exception:
        glitch("  ✗ invalid hex"); sys.exit(1)

    tol_raw = input(rgb(0,220,255) + "  Tolerance " + RESET +
                    rgb(120,120,140) + "[24]" + RESET + " > ").strip() or "24"
    tol = int(tol_raw)

    pngs = list_pngs()
    print(gradient(f"\n⟶ killing {raw.upper()} on {len(pngs)} frame(s)\n"))
    for i, p in enumerate(pngs, 1):
        img = Image.open(p).convert("RGBA")
        px = img.load()
        for y in range(img.height):
            for x in range(img.width):
                r,g,b,a = px[x,y]
                if abs(r-target[0])<=tol and abs(g-target[1])<=tol and abs(b-target[2])<=tol:
                    px[x,y] = (r,g,b,0)
        img.save(p)
        progress(i, len(pngs), label=p.name)
    print(box(f"✔ {len(pngs)} frames cleansed", color=(0,255,160)))

if __name__ == "__main__": run()
