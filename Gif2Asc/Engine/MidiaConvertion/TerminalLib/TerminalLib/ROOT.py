from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


# Files 
class Addresses:
    Downloads = PROJECT_ROOT / "Files" / "Downloads"
    PngFrames = PROJECT_ROOT / "Files" / "PngFrames"
    Settings = PROJECT_ROOT / "Files" / "Settings"
    Song = PROJECT_ROOT / "Files" / "Song"
    TextFrames = PROJECT_ROOT / "Files" / "TextFrames"

