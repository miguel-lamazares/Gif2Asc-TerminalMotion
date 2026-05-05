#!/usr/bin/env python3
"""Ia-offline — offline AI background removal via rembg."""
from __future__ import annotations
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _common import (banner, gradient, box, Spinner, progress, glitch, list_pngs)

try:
    from rembg import remove
except ImportError:
    print("Install:  python -m pip install rembg onnxruntime"); sys.exit(1)

def run():
    banner("⟢ Ia-offline", "AI background removal (rembg / U²-Net)")
    pngs = list_pngs()
    print(gradient(f"\n⟶ inferring on {len(pngs)} frame(s)\n"))
    for i, p in enumerate(pngs, 1):
        with Spinner(f"frame {i}/{len(pngs)} — {p.name}"):
            data = p.read_bytes()
            out = remove(data)
        p.write_bytes(out)
        progress(i, len(pngs), label=p.name)
    print(box("✔ backgrounds vaporized", color=(0,255,160)))

if __name__ == "__main__": run()
