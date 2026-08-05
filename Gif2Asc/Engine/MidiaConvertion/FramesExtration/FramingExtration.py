from __future__ import annotations
from pathlib import Path
import sys, os, shutil, subprocess, urllib.parse, urllib.request, re

# Style and address from TermForge
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "TermForge"))

from termforge.Terminal import (
    banner, gradient, glitch, box, Spinner, rgb, RESET, typewriter, confirm, confirmAudio
)
from termforge.ROOT import png_dir, downloads_dir, song_dir
from termforge.core import Clear_all

# Checking for paths, urls and existed address

for folder in [png_dir(), downloads_dir(), song_dir()]:
    os.makedirs(folder, exist_ok=True)

URL_RE = re.compile(r"^https?://", re.I)

def _sanitize(p: str) -> str:
    p = p.strip().strip('"').strip("'")
    return p.replace("\\ ", " ")

# Get path or url

def _ask_path() -> str:
    print(gradient("⟢ Drop a path or URL"))
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


def audio_extract(src: Path):
    song_dir().mkdir(parents=True, exist_ok=True)
    out = song_dir() / "audio.wav"
    with Spinner("ripping audio"):
                    subprocess.run(
        [
            "ffmpeg",
            "-y",                 
            "-i", str(src),       
            "-vn",                
            "-ar", "22050",       
            "-ac", "1",           
            "-f", "wav",          
            str(out),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if out.exists() and out.stat().st_size > 0:
        print(box(f"✔ audio → {out}", color=(0,255,160)))
    else:
        glitch("  ⚠ no audio track found in source")
# extrating frames 

Image_ext = [".png", ".webp", ".gif"]
ImageToBeConverted = [".jpeg", ".jpg", ".svg"]
Video_ext = [".mp4",".mov",".avi",".mkv", ".webm"]

def extract(src: Path):
    if not shutil.which("ffmpeg"):
        glitch("  ✗ ffmpeg not in PATH"); sys.exit(1)

    _clean(png_dir())
    print(gradient("\n⟶ extracting frames…\n"))
    with Spinner("ffmpeg is doing ffmpeg things"):
        if Path(src).suffix.lower() in Image_ext or Path(src).suffix.lower() in ImageToBeConverted:
            subprocess.run(
                ["ffmpeg", "-y", "-i", str(src), str(png_dir() / "%d.png")],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
            )

        if Path(src).suffix.lower() in Video_ext:
            subprocess.run(
                ["ffmpeg", "-y", "-i", str(src), str(png_dir() / "%d.png")],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
            )
        
        
    
    
    if Path(src).suffix.lower() in Image_ext or Path(src).suffix.lower() in ImageToBeConverted:
            audio_choice = confirm("\nDo you wanna play some audio?")
            if audio_choice == 1:
                print(gradient("What's the song's address?"))
                song_path = input("-> ")
                audio_extract(song_path)
    if Path(src).suffix.lower() in Video_ext:
            audio_choice = confirmAudio("\nAlso extract the audio track or play some audio?")
            if audio_choice == 2:
                pass
            elif audio_choice == 1:
                print(gradient("What's the song's address?"))
                song_path = input("-> ")
                audio_extract(song_path)
            elif audio_choice == 0:
                audio_extract(src)

    n = len(list(png_dir().glob("*.png")))
    print(box(f"✔ {n} PNG frames → {png_dir()}", color=(0,255,160)))

def run():
    banner("⟢ Frame Extractor")
    raw = _ask_path()
    src = _download(raw) if URL_RE.match(raw) else Path(raw)
    extract(src)

if __name__ == "__main__":
    run()