#!/usr/bin/env python3
"""refineMask — feathers + thresholds the alpha to clean up halos."""
from __future__ import annotations
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _common import (banner, gradient, box, progress, rgb, RESET,
                     glitch, list_pngs)
try:
    from PIL import Image, ImageFilter
except ImportError:
    print("python -m pip install Pillow"); sys.exit(1)

def run():
    banner("⟢ refineMask", "smooth & threshold the alpha channel")

    feather = input(rgb(0,220,255) + "  Feather radius " + RESET +
                    rgb(120,120,140) + "[1.5]" + RESET + " > ").strip() or "1.5"
    thresh  = input(rgb(0,220,255) + "  Alpha threshold " + RESET +
                    rgb(120,120,140) + "[16]" + RESET + " > ").strip() or "16"
    feather = float(feather); thresh = int(thresh)

    pngs = list_pngs()
    print(gradient(f"\n⟶ refining {len(pngs)} mask(s)\n"))
    for i, p in enumerate(pngs, 1):
        img = Image.open(p).convert("RGBA")
        r,g,b,a = img.split()
        a = a.point(lambda v: 0 if v < thresh else v)
        a = a.filter(ImageFilter.GaussianBlur(feather))
        Image.merge("RGBA", (r,g,b,a)).save(p)
        progress(i, len(pngs), label=p.name)
    print(box("✔ masks polished", color=(0,255,160)))

if __name__ == "__main__": run()
