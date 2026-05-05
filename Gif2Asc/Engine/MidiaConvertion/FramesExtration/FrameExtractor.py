#!/usr/bin/env python3
"""
FrameExtractor — pulls PNG frames + audio from a local file or URL.
Output: Files/PngFrames/{N}.png  +  Files/Song/audio.{ext}
"""
from __future__ import annotations
import sys, os, shutil, subprocess, urllib.parse, urllib.request, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "TerminalLib"))

from TerminalLib.Terminal import (
    banner, gradient, glitch, box, Spinner, rgb, RESET, typewriter, confirm,
)
from TerminalLib.ROOT import png_dir, downloads_dir, song_dir

URL_RE = re.compile(r"^https?://", re.I)

def _sanitize(p: str) -> str:
    p = p.strip().strip('"').strip("'")
    return p.replace("\\ ", " ")

def _ask_path() -> str:
    print(gradient("⟢ Drop a path or URL (gif / mp4 / webm)"))
    for attempt in range(3):
        raw = input(rgb(0,220,255) + "  ➜  " + RESET).strip()
        raw = _sanitize(raw)
        if not raw:
            glitch("  ✗ empty input"); continue
        if URL_RE.match(raw):
            return raw
        if Path(raw).exists():
            return raw
        glitch(f"  ✗ not found: {raw}  ({2-attempt} tries left)")
    sys.exit(1)

def _download(url: str) -> Path:
    downloads_dir().mkdir(parents=True, exist_ok=True)
    ext = Path(urllib.parse.urlparse(url).path).suffix or ".gif"
    out = downloads_dir() / f"input{ext}"
    with Spinner(f"downloading {url[:60]}…"):
        urllib.request.urlretrieve(url, out)
    print(box(f"✔ saved → {out}", color=(0,255,160)))
    return out

def _clean(path: Path):
    if path.exists():
        for f in path.iterdir():
            if f.is_file(): f.unlink()
    path.mkdir(parents=True, exist_ok=True)

def extract(src: Path):
    if not shutil.which("ffmpeg"):
        glitch("  ✗ ffmpeg not in PATH"); sys.exit(1)

    _clean(png_dir())
    print(gradient("\n⟶ extracting frames…\n"))
    with Spinner("ffmpeg is doing ffmpeg things"):
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(src), str(png_dir() / "%d.png")],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
        )
    n = len(list(png_dir().glob("*.png")))
    print(box(f"✔ {n} PNG frames → {png_dir()}", color=(0,255,160)))

    if confirm("\nAlso extract the audio track?"):
        song_dir().mkdir(parents=True, exist_ok=True)
        out = song_dir() / "audio.mp3"
        with Spinner("ripping audio"):
            subprocess.run(
                ["ffmpeg", "-y", "-i", str(src), "-vn", "-acodec", "libmp3lame", str(out)],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
            )
        if out.exists() and out.stat().st_size > 0:
            print(box(f"✔ audio → {out}", color=(0,255,160)))
        else:
            glitch("  ⚠ no audio track found in source")

def run():
    banner("⟢ Frame Extractor", "GIF/MP4/URL → PNG sequence (+ audio)")
    raw = _ask_path()
    src = _download(raw) if URL_RE.match(raw) else Path(raw)
    extract(src)

if __name__ == "__main__":
    run()
