import os
import subprocess
import sys
from TerminalLib import asc
import json
import shutil

# ---------------------------------------------
# UI — BASIC OPTIONS
# ---------------------------------------------
asc.Clear_all()

asc.typewrite(asc.Colors.PURPLE + "Configure your jp2a\n", 0.04)
asc.typewrite(asc.Colors.GREEN + "Border and text\n\n", 0.02)

asc.typewrite(asc.Colors.CYAN + "Border? (1 - yes / 2 - no)\n", 0.02)
border = "--border" if asc.read_int(1,3) == 1 else ""

asc.Clear_all()

asc.typewrite(asc.Colors.CYAN + "Special characters? (1 - yes / 2 - no)\n", 0.02)
if asc.read_int(1,3) == 1:
    asc.Clear_all()
    asc.typewrite(asc.Colors.YELLOW + "1 - Blocks\n2 - Unicode (Braille)\n3 - spaced unicode\n4 - half blocks\n5 - japanese\n6 - it's up to you <3 \n\n", 0.02)
    options = asc.read_int(1,7) 
    if options == 1:
        char = "--chars="" ░▒▓█"
    if options == 2:
        char = "--chars="" ⣀⣤⣶⣯⣟⣷⣿"
    if options == 3:
        char = "--chars="" ⠁⠃⠇⠏⠟⠿⡿⣿"
    if options == 4:
        chars="--chars="" ▘▝ ▖▗ ▌▐▀▄█"
    if options == 5:
        chars="--chars="" .おまえはもう死んでいる"
    if options == 6:
        asc.typewrite(asc.Colors.RED + "Characters (min 2):\n")
        char = f"--chars={input()}"
else:
    char = ""

asc.Clear_all()

asc.typewrite(asc.Colors.CYAN + "Frame is big? (1 - yes / 2 - no)\n", 0.02)
fit = "--term-fit" if asc.read_int(1,3) == 1 else ""

asc.Clear_all()

asc.typewrite(
    asc.Colors.CYAN +
    "Light characters on dark background? (1 - yes / 2 - no)\n",
    0.02
)
back = "--background=dark" if asc.read_int(1,3) == 1 else "--background=light"

asc.Clear_all()

asc.typewrite(
    asc.Colors.CYAN +
    "Do you want to center the image? (1 - yes / 2 - no)\n\n",
    0.02
)
center = "--term-center" if asc.read_int(1,3) == 1 else ""

asc.Clear_all()

# ---------------------------------------------
# SIZE / PROPORTION
# ---------------------------------------------

asc.typewrite(asc.Colors.YELLOW + "Proportion\n\n", 0.02)
asc.typewrite(
    asc.Colors.CYAN +
    "1. Default\n2. Set width and height\n3. Use terminal zoom\n\n",
    0.02
)

choice = asc.read_int(1,4)
proportion = ""

if choice == 2:
    asc.typewrite("Width: ", 0.03)
    w = input()
    asc.typewrite("Height: ", 0.03)
    h = input()
    proportion = f"--size={w}x{h}"
elif choice == 3:
    proportion = "--term-zoom"

asc.Clear_all()
# ---------------------------------------------
# COLORS
# ---------------------------------------------

asc.typewrite(asc.Colors.GREEN + "Colors\n\n", 0.02)
asc.typewrite(
    asc.Colors.CYAN +
    "1. True colors\n2. Black and white\n3. Manual config\n",
    0.02
)

mode = asc.read_int(1,3)

jp2a_cmd = ["jp2a"]

if mode == 1:
    jp2a_cmd += [
        "--colors",
        "--color-depth=24",
        
    ]

elif mode == 2:
    pass 

elif mode == 3:
    asc.typewrite("Red   (default 0.2989): ", 0.03)
    red = input()
    asc.typewrite("Green (default 0.5866): ", 0.03)
    green = input()
    asc.typewrite("Blue  (default 0.1145): ", 0.03)
    blue = input()
    asc.typewrite("Color depth (4 / 8 / 24): ", 0.03)
    depth = input()

    jp2a_cmd += [
        "--colors",
        f"--color-depth={depth}",
        f"--red={red}",
        f"--green={green}",
        f"--blue={blue}",
        
    ]
else:
    print("Invalid option.")
    sys.exit(1)

jp2a_cmd += [
    border,
    char,
    fit,
    proportion,
    back,
    center
]

jp2a_cmd = asc.clean_args(jp2a_cmd)

asc.Clear_all()
print(asc.Colors.RESET + "")

# ---------------------------------------------
# Saving configs
# ---------------------------------------------

FOLDER = "./Gif/Gif_to_asc/Jp2aconfigs"

if os.path.exists(FOLDER):
    shutil.rmtree(FOLDER)
os.makedirs(FOLDER, exist_ok=True)

config = {"jp2a_args": asc.clean_args(jp2a_cmd)}

with open("./Gif/Gif_to_asc/Jp2aconfigs/jp2aconfig.json", "w+",encoding="utf-8") as f:
    json.dump(config,f,indent=4)

# ---------------------------------------------
# INPUT FOLDER
# ---------------------------------------------

FOLDER = "./Gif/Gif_to_asc/Frame in png"

folder = sys.argv[1] if len(sys.argv) > 1 else FOLDER

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
