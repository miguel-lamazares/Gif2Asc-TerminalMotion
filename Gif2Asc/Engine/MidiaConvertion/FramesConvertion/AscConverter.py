#!/usr/bin/env python3
"""
AscConverter — interactive jp2a wizard.
Reads PNGs from Files/PngFrames, writes .asc to Files/TextFrames,
and persists the chosen settings to Files/Settings/jp2aconfig.json.
"""
from __future__ import annotations
import os, sys, json, subprocess, shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "TerminalLib"))
sys.path.insert(0, str(HERE / "Defs"))

from TerminalLib.Terminal import (
    banner, gradient, glitch, box, Spinner, progress,
    arrow_menu, confirm, rgb, RESET, typewriter,
)
from TerminalLib.ROOT import png_dir, text_dir, settings_dir
from Defs import select_charset

CFG_PATH = settings_dir() / "jp2aconfig.json"

def _ask_int(label: str, default: int, lo=1, hi=400) -> int:
    while True:
        raw = input(rgb(0,220,255) + f"  {label} " + RESET + rgb(120,120,140) + f"[{default}]" + RESET + " > ").strip()
        if not raw: return default
        try:
            v = int(raw)
            if lo <= v <= hi: return v
        except ValueError: pass
        glitch(f"  ✗ invalid (need int between {lo} and {hi})")

def wizard() -> dict:
    banner("⟢ jp2a Wizard", "configure how your PNGs become art")

    typewriter("  ◇ Picking the perfect glyphs…", color=rgb(140,140,160))
    name, glyphs = select_charset()
    print()

    width  = _ask_int("Width  (cols)", 100)
    height = _ask_int("Height (rows)", 30)

    invert = confirm("Invert luminance?")
    print()
    color  = confirm("Color output?  (slower but pretty)")
    print()

    cfg = {"charset_name": name, "charset": glyphs,
           "width": width, "height": height,
           "invert": invert, "color": color}

    settings_dir().mkdir(parents=True, exist_ok=True)
    CFG_PATH.write_text(json.dumps(cfg, indent=2))
    print(box(f"✔ saved → {CFG_PATH.relative_to(CFG_PATH.parents[2])}", color=(0,255,160)))
    return cfg

def jp2a_args(cfg: dict) -> list[str]:
    args = [f"--width={cfg['width']}", f"--height={cfg['height']}",
            f"--chars={cfg['charset']}"]
    if cfg.get("invert"): args.append("--invert")
    if cfg.get("color"):  args.append("--color")
    return args

def render(cfg: dict):
    if not shutil.which("jp2a"):
        glitch("  ✗ jp2a not found in PATH — install it first."); sys.exit(1)

    src, dst = png_dir(), text_dir()
    dst.mkdir(parents=True, exist_ok=True)
    pngs = sorted(src.glob("*.png"), key=lambda p: int(p.stem) if p.stem.isdigit() else 0)
    if not pngs:
        glitch(f"  ✗ no PNGs in {src}"); sys.exit(1)

    print(gradient(f"\n⟶ rendering {len(pngs)} frames\n"))
    for i, png in enumerate(pngs, 1):
        out = dst / f"{i-1:09d}.asc"
        subprocess.run(["jp2a", *jp2a_args(cfg), str(png)],
                       stdout=open(out, "w"), stderr=subprocess.DEVNULL, check=False)
        progress(i, len(pngs), label=png.name)
    print(box(f"✔ wrote {len(pngs)} .asc → {dst}", color=(0,255,160)))

if __name__ == "__main__":
    cfg = wizard()
    if confirm("\nRender frames now with these settings?"):
        render(cfg)
