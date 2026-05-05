"""ROOT path helper — resolves Files/ relative to project root."""
from pathlib import Path

def project_root() -> Path:
    # walks up until it finds the MidiaConvertion folder
    here = Path(__file__).resolve()
    for p in [here, *here.parents]:
        if p.name == "MidiaConvertion":
            return p
    return here.parents[3]

def files_dir() -> Path:
    return project_root() / "Files"

def png_dir():       return files_dir() / "PngFrames"
def text_dir():      return files_dir() / "TextFrames"
def downloads_dir(): return files_dir() / "Downloads"
def song_dir():      return files_dir() / "Song"
def settings_dir():  return files_dir() / "Settings"
