#!/usr/bin/env python3
"""keepcenter — keeps an elliptical region in the center; fades the rest."""
from __future__ import annotations
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _common import (banner, gradient, box, progress, rgb, RESET,
                     glitch, list_pngs)
try:
    from PIL import Image, ImageDraw, ImageFilter, ImageChops
except ImportError:
    print("python -m pip install Pillow"); sys.exit(1)

def run():
    banner("⟢ keepCenter", "keep the middle, drop the edges")

    pct = input(rgb(0,220,255) + "  Keep area % " + RESET +
                rgb(120,120,140) + "[70]" + RESET + " > ").strip() or "70"
    feather = input(rgb(0,220,255) + "  Edge feather " + RESET +
                    rgb(120,120,140) + "[20]" + RESET + " > ").strip() or "20"
    pct = max(5, min(99, int(pct))); feather = max(0, int(feather))

    pngs = list_pngs()
    print(gradient(f"\n⟶ centering {len(pngs)} frame(s)\n"))
    for i, p in enumerate(pngs, 1):
        img = Image.open(p).convert("RGBA")
        w,h = img.size
        mask = Image.new("L", (w,h), 0)
        ew, eh = w*pct//100, h*pct//100
        x0, y0 = (w-ew)//2, (h-eh)//2
        ImageDraw.Draw(mask).ellipse([x0,y0,x0+ew,y0+eh], fill=255)
        if feather: mask = mask.filter(ImageFilter.GaussianBlur(feather))
        r,g,b,a = img.split()
        a = ImageChops.multiply(a, mask)
        Image.merge("RGBA", (r,g,b,a)).save(p)
        progress(i, len(pngs), label=p.name)
    print(box("✔ center preserved", color=(0,255,160)))

if __name__ == "__main__": run()
