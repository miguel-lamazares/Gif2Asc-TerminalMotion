import os
import subprocess
import sys
from TerminalLib import asc
import json
import shutil

# ---------------------------------------------
# Fetching
# ---------------------------------------------

with open("/home/dex/Documentos/GitHub/Inutil-things-for-JAVA/Gif2Asc/Engine/MidiaConvertion/JP2ASettings/jp2aconfig.json", "r") as f:
        config = json.load(f)

jp2a_cmd = config["jp2a_args"]


# ---------------------------------------------
# INPUT FOLDER
# ---------------------------------------------

FOLDER = "./Gif/Gif_to_asc/Frame in png"

folder = sys.argv[1] if len(sys.argv) > 1 else FOLDER

if not os.path.isdir(folder):
    print(f"Folder not found: {folder}")
    sys.exit(1)

png_files = sorted(f for f in os.listdir(folder) if f.endswith(".png"))
total = len(png_files)

if total == 0:
    print("No PNG files found.")
    sys.exit(1)

frames = []

# ---------------------------------------------
# GENERATE ASCII FRAMES
# ---------------------------------------------

for i, file in enumerate(png_files):
    path = os.path.join(folder, file)

    result = subprocess.run(
        jp2a_cmd + [path],
        capture_output=True,
        text=True
    )

    frames.append(result.stdout)
    asc.print_progress_bar(i + 1, total)

# ---------------------------------------------
#  CLEANING OLD FRAMES
# ---------------------------------------------
out = "./Gif/AscFrames"

if os.path.exists(out):
    shutil.rmtree(out)
os.makedirs(out, exist_ok=True)

asc_files = sorted(f for f in os.listdir(out) if f.endswith(".asc"))

for file in asc_files:
    os.remove(os.path.join(out, file))

# ---------------------------------------------
# WRITING ASC FRAMES
# ---------------------------------------------

for i, frame in enumerate(frames):
    path = os.path.join(out, f"{i:04d}.asc")
    with open(path, "w", encoding="utf-8") as f:
        f.write(frame)

print("Finish with sucess, java starting")
