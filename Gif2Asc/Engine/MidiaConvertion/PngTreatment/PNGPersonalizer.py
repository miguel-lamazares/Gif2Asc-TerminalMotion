#!/usr/bin/env python3
"""
PNGPersonalizer — interactive tweaks for every PNG in Files/PngFrames.
Brightness · Contrast · Saturation · Scale · Invert.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "TerminalLib"))

try:
    from PIL import Image, ImageEnhance, ImageOps
except ImportError:
    print("Install Pillow:  python -m pip install Pillow"); sys.exit(1)

from TerminalLib.Terminal import (
    banner, gradient, glitch, box, Spinner, progress,
    arrow_menu, confirm, rgb, RESET, typewriter,
)
from TerminalLib.ROOT import png_dir

def _ask_float(label, default, lo=0.0, hi=5.0):
    while True:
        raw = input(rgb(0,220,255) + f"  {label} " + RESET +
                    rgb(120,120,140) + f"[{default}]" + RESET + " > ").strip()
        if not raw: return default
        try:
            v = float(raw)
            if lo <= v <= hi: return v
        except ValueError: pass
        glitch(f"  ✗ need float in [{lo}, {hi}]")

def _ask_int(label, default, lo=1, hi=2000):
    while True:
        raw = input(rgb(0,220,255) + f"  {label} " + RESET +
                    rgb(120,120,140) + f"[{default}]" + RESET + " > ").strip()
        if not raw: return default
        try:
            v = int(raw)
            if lo <= v <= hi: return v
        except ValueError: pass
        glitch(f"  ✗ need int in [{lo}, {hi}]")

def run():
    banner("⟢ PNG Personalizer", "tweak every frame in Files/PngFrames")

    pngs = sorted(png_dir().glob("*.png"),
                  key=lambda p: int(p.stem) if p.stem.isdigit() else 0)
    if not pngs:
        glitch(f"  ✗ no PNGs in {png_dir()}"); sys.exit(1)

    print(box(f"found {len(pngs)} frame(s)", color=(0,200,255)))
    print()

    bright = _ask_float("Brightness", 1.0, 0.0, 3.0)
    contrast = _ask_float("Contrast  ", 1.0, 0.0, 3.0)
    sat = _ask_float("Saturation", 1.0, 0.0, 3.0)
    scale = _ask_int("Scale (% of original)", 100, 10, 400)
    invert = confirm("\nInvert colors?")

    print(gradient("\n⟶ applying tweaks\n"))
    for i, p in enumerate(pngs, 1):
        img = Image.open(p).convert("RGBA")
        if scale != 100:
            w, h = img.size
            img = img.resize((max(1, w*scale//100), max(1, h*scale//100)), Image.LANCZOS)
        if bright   != 1.0: img = ImageEnhance.Brightness(img).enhance(bright)
        if contrast != 1.0: img = ImageEnhance.Contrast(img).enhance(contrast)
        if sat      != 1.0: img = ImageEnhance.Color(img).enhance(sat)
        if invert:
            r,g,b,a = img.split()
            rgb_inv = ImageOps.invert(Image.merge("RGB", (r,g,b)))
            img = Image.merge("RGBA", (*rgb_inv.split(), a))
        img.save(p)
        progress(i, len(pngs), label=p.name)

    print(box(f"✔ updated {len(pngs)} frame(s) in place", color=(0,255,160)))

if __name__ == "__main__":
    run()
