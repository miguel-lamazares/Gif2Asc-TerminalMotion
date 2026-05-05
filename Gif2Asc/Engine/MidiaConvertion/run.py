#!/usr/bin/env python3
"""
run.py — the one ring to ASCII-fy them all.

Guided pipeline:
  1) Extract frames (FrameExtractor)
  2) (optional) Treat PNGs (PNGPersonalizer + BackgroundRemover)
  3) Convert to .asc — wizard (AscConverter) OR re-use last config (NoArgs)
"""
from __future__ import annotations
import sys, runpy, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "TerminalLib"))

from TerminalLib.Terminal import (
    banner, gradient, gradient_block, glitch, box, Spinner,
    arrow_menu, confirm, typewriter, rgb, RESET, clear,
)
from TerminalLib.ROOT import settings_dir, png_dir
from TerminalLib.asc import LOGO

TREATMENT = {
    "PNG Personalizer (brightness/contrast/scale)": ROOT / "PngTreatment" / "PNGPersonalizer.py",
    "removeColor   — strip a color → alpha":        ROOT / "PngTreatment" / "backgroundRemover" / "removeColor.py",
    "refineMask    — smooth & threshold alpha":     ROOT / "PngTreatment" / "backgroundRemover" / "refineMask.py",
    "keepCenter    — keep middle, drop edges":      ROOT / "PngTreatment" / "backgroundRemover" / "keepcenter.py",
    "Ia-offline    — AI bg removal (rembg)":        ROOT / "PngTreatment" / "backgroundRemover" / "Ia-offline.py",
}

def _run_script(path: Path):
    if not path.exists():
        glitch(f"  ✗ missing script: {path}"); return
    print()
    runpy.run_path(str(path), run_name="__main__")
    print()

def _intro():
    clear()
    print(gradient_block(LOGO))
    typewriter("  the engine that turns motion into glyphs ⟶ ASCII",
               color=rgb(140,140,160), delay=0.008)
    print()

def _step_extract():
    print(box("STEP 1/3 · EXTRACT", color=(0,200,255)))
    if confirm("Extract frames now?"):
        _run_script(ROOT / "FramesExtration" / "FrameExtractor.py")
    else:
        typewriter("  ↷ skipping extraction", color=rgb(140,140,160))

def _step_treat():
    print(box("STEP 2/3 · TREAT  (optional)", color=(180,0,255)))
    if not confirm("Want to tweak the PNG frames before converting?"):
        typewriter("  ↷ skipping treatment", color=rgb(140,140,160)); return

    pngs = list(png_dir().glob("*.png"))
    if not pngs:
        glitch(f"  ⚠ no PNGs in {png_dir()} — nothing to treat"); return

    while True:
        opts = list(TREATMENT.keys()) + ["✓ Done — move on"]
        idx = arrow_menu("◇ Pick a treatment (run as many as you want)", opts)
        if idx == len(opts) - 1: return
        _run_script(TREATMENT[list(TREATMENT.keys())[idx]])
        if not confirm("Apply another treatment?"): return

def _step_convert():
    print(box("STEP 3/3 · CONVERT", color=(0,255,160)))
    cfg = settings_dir() / "jp2aconfig.json"
    has_cfg = cfg.exists()

    options = ["⟢ New wizard (configure from scratch)"]
    if has_cfg: options.insert(0, "♻ Use last config (jp2aconfig.json)")
    options.append("✗ Skip conversion")

    idx = arrow_menu("How do you want to render?", options)
    choice = options[idx]

    if choice.startswith("♻"):
        _run_script(ROOT / "FramesConvertion" / "NoArgsAscConverter.py")
    elif choice.startswith("⟢"):
        _run_script(ROOT / "FramesConvertion" / "AscConverter.py")
    else:
        typewriter("  ↷ skipping conversion", color=rgb(140,140,160))

def main():
    _intro()
    try:
        _step_extract()
        _step_treat()
        _step_convert()
        print()
        print(box("✔ pipeline complete — go feed the Player\n   Files/TextFrames/  →  Java / C renderer",
                  color=(0,255,160)))
    except KeyboardInterrupt:
        print()
        glitch("  ✗ aborted by user")

if __name__ == "__main__":
    main()
