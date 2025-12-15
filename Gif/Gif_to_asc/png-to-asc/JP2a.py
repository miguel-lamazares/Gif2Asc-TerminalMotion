import os
import subprocess
import sys
from TerminalLib import asc

# ---------------------------------------------
# UI — BASIC OPTIONS
# ---------------------------------------------
asc.Clear_all()

asc.typewrite(asc.Colors.PURPLE + "Configure your jp2a\n", 0.04)
asc.typewrite(asc.Colors.GREEN + "Border and text\n\n", 0.02)

asc.typewrite(asc.Colors.CYAN + "Border? (0 - yes / 1 - no)\n", 0.02)
border = "--border" if asc.read_int(2) == 0 else ""

asc.Clear_all()

asc.typewrite(asc.Colors.CYAN + "Special characters? (0 - yes / 1 - no)\n", 0.02)
if asc.read_int(2) == 0:
    asc.typewrite(asc.Colors.RED + "Characters (min 2):\n")
    char = f"--chars={input()}"
else:
    char = ""

asc.Clear_all()

asc.typewrite(asc.Colors.CYAN + "Frame is big? (0 - yes / 1 - no)\n", 0.02)
fit = "--term-fit" if asc.read_int(2) == 0 else ""

asc.Clear_all()

asc.typewrite(
    asc.Colors.CYAN +
    "Light characters on dark background? (0 - yes / 1 - no)\n",
    0.02
)
back = "--background=dark" if asc.read_int(2) == 0 else "--background=light"

asc.Clear_all()

asc.typewrite(
    asc.Colors.CYAN +
    "Do you want to clear the terminal before starting? (0 - yes / 1 - no)\n\n",
    0.02
)
clear = "--clear" if asc.read_int(2) == 0 else ""

asc.Clear_all()

asc.typewrite(
    asc.Colors.CYAN +
    "Do you want to center the image? (0 - yes / 1 - no)\n\n",
    0.02
)
center = "--term-center" if asc.read_int(2) == 0 else ""

asc.Clear_all()

# ---------------------------------------------
# SIZE / PROPORTION
# ---------------------------------------------

asc.typewrite(asc.Colors.YELLOW + "Proportion\n\n", 0.02)
asc.typewrite(
    asc.Colors.CYAN +
    "0. Default\n1. Set width and height\n2. Use terminal zoom\n\n",
    0.02
)

choice = asc.read_int(3)
proportion = ""

if choice == 1:
    asc.typewrite("Width: ", 0.03)
    w = input()
    asc.typewrite("Height: ", 0.03)
    h = input()
    proportion = f"--size={w}x{h}"
elif choice == 2:
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

mode = asc.read_int(3)

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
    clear,
    center
]

jp2a_cmd = asc.clean_args(jp2a_cmd)

asc.Clear_all()
print(asc.Colors.RESET + "")

# ---------------------------------------------
# INPUT FOLDER
# ---------------------------------------------

FOLDER = "/home/dex/Documentos/GitHub/Inutil-things-for-JAVA/Gif/Gif_to_asc/Frame in png"

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
out = "/home/dex/Documentos/GitHub/Inutil-things-for-JAVA/Gif/AscFrames"

asc_files = sorted(f for f in os.listdir(out) if f.endswith(".asc"))

for file in asc_files:
    os.remove(os.path.join(out, file))

# ---------------------------------------------
# WRITING ASC FRAMES
# ---------------------------------------------

os.makedirs(out, exist_ok=True)

for i, frame in enumerate(frames):
    path = os.path.join(out, f"{i:04d}.asc")
    with open(path, "w", encoding="utf-8") as f:
        f.write(frame)

print("Finish with sucess, java starting")
