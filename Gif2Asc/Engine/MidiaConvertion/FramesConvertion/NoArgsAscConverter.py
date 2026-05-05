#!/usr/bin/env python3
"""
NoArgsAscConverter — re-runs the last saved jp2a config without questions.
Reads Files/Settings/jp2aconfig.json and renders Files/PngFrames → Files/TextFrames.
"""
from __future__ import annotations
import sys, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "TerminalLib"))

from TerminalLib.Terminal import banner, glitch, box, rgb, RESET
from TerminalLib.ROOT import settings_dir

# reuse the renderer
sys.path.insert(0, str(HERE))
from AscConverter import render, CFG_PATH

if __name__ == "__main__":
    banner("⟢ NoArgs Render", "reusing your last jp2a config")
    if not CFG_PATH.exists():
        glitch(f"  ✗ no config at {CFG_PATH} — run AscConverter first.")
        sys.exit(1)
    cfg = json.loads(CFG_PATH.read_text())
    print(box(f"charset : {cfg['charset_name']}\n"
              f"size    : {cfg['width']}×{cfg['height']}\n"
              f"invert  : {cfg.get('invert', False)}\n"
              f"color   : {cfg.get('color', False)}",
              color=(0,200,255)))
    render(cfg)
