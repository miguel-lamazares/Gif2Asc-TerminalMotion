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
    asc.typewrite(asc.Colors.YELLOW + 
                 "1 - Blocks\n" +
                 "2 - Unicode (Braille)\n" + 
                 "3 - Spaced Unicode\n" +
                 "4 - Half Blocks\n" +
                 "5 - Japanese\n" +
                 "6 - Custom\n" +
                 "7 - ASCII Only\n" +
                 "8 - Border Characters\n" +
                 "9 - Geometric Shapes\n" +
                 "10 - Dot Patterns\n" +
                 "11 - Quadrant Blocks\n" +
                 "12 - Sextants (6-part)\n" +
                 "13 - Technical Symbols\n" +
                 "14 - Wedge Shapes\n" +
                 "15 - Latin Letters\n" +
                 "16 - Alphanumeric\n" +
                 "17 - Extra Symbols\n" +
                 "18 - Solid Blocks\n" +
                 "19 - Vertical Halves\n" +
                 "20 - Wide Characters\n" +
                 "21 - Digital/7-Segment\n" +
                 "22 - Math Symbols\n" +
                 "23 - Minimalist Dots\n" +
                 "24 - Mixed Density\n" +
                 "25 - Artistic Flow\n" +
                 "26 - Binary/Barcode\n" +
                 "27 - Vertical bar gradient\n" +
                 "28 - Asian-inspired\n" +
                 "29 - Circle progression\n" +
                 "30 - Unique Unicode shapes\n" +
                 "31 - Mixed block types\n" +
                 "32 - It's up to you <3 \n\n", 0.02)
    
    options = asc.read_int(1, 33) 
    
    if options == 1:
        chars = "--chars="" ░▒▓█"""  # Original blocks
    elif options == 2:
        chars = "--chars="" ⣀⣤⣶⣯⣟⣷⣿"""  # Braille gradient
    elif options == 3:
        chars = "--chars="" ⠁⠃⠇⠏⠟⠿⡿⣿"""  # Spaced braille
    elif options == 4:
        chars = "--chars="" ▘▝▖▗▌▐▀▄█"""  # Half blocks
    elif options == 5:
        chars = "--chars="" .。、・ヲァィゥェォおまえはもう死んでいる"""  # Japanese
    elif options == 6:
        asc.typewrite(asc.Colors.RED + "Characters (min 2):\n")
        chars = f"--chars={input()}"
    elif options == 7:
        chars = "--chars="" .:;+*?%$@#"""  # ASCII art basic
    elif options == 8:
        chars = "--chars="" ─│┌┐└┘├┤┬┴┼"""  # Box drawing
    elif options == 9:
        chars = "--chars="" ▲▼◀▶◆■○●□△▽◇◊"""  # Geometric
    elif options == 10:
        chars = "--chars="" ·•∙⦁●◌○◎◉●◯"""  # Dot progression
    elif options == 11:
        chars = "--chars="" ▖▗▘▝▚▞▙▟"""  # Quadrants
    elif options == 12:
        chars = "--chars="" 🬀🬁🬂🬃🬄🬅🬆🬇🬈🬉"""  # Sextants
    elif options == 13:
        chars = "--chars="" ⌘⌥⎇⏎␣⏏⚙️🔧🛠️"""  # Technical symbols
    elif options == 14:
        chars = "--chars="" ◢◣◤◥◸◹◺◿"""  # Wedge shapes
    elif options == 15:
        chars = "--chars="" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"""  # Latin letters
    elif options == 16:
        chars = "--chars="" ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"""  # Alphanumeric
    elif options == 17:
        chars = "--chars="" ★☆♪♫♥♦♣♠☀☁☂☃"""  # Extra symbols
    elif options == 18:
        chars = "--chars="" █▉▊▋▌▍▎▏"""  # Solid block progression
    elif options == 19:
        chars = "--chars="" ▀▄█"""  # Vertical halves
    elif options == 20:
        chars = "--chars="" ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"""  # Full-width
    elif options == 21:
        chars = "--chars="" ⓪①②③④⑤⑥⑦⑧⑨"""  # Digital/circled numbers
    elif options == 22:
        chars = "--chars="" +−×÷=≠≈±√∞∫∑∏∂"""  # Math symbols
    elif options == 23:
        chars = "--chars=""  ·∙∙⸱⸳⸰ꓸ"""  # Minimalist small dots
    elif options == 24:
        chars = "--chars=""  .:^~+*xX%&$@#█"""  # Mixed density gradient
    elif options == 25:
        chars = "--chars=""  ۞۩≋≌∿≈～〰️♪♫♬"""  # Artistic/flow symbols
    elif options == 26:
        chars = "--chars=""  01█"""  # Binary/barcode style
    elif options == 27:
         chars = "--chars="" ▏▎▍▌▋▊▉█▇▆▅▄▃▂▁"""  # Vertical bar gradient
    
    elif options == 28:
         chars = "--chars="" ╱╲╳┃━┏┓┗┛┣┫┳┻╋"""  # Asian-inspired
    
    elif options == 29:
        chars = "--chars="" ◐◑◒◓◔◕◖◗◦◌◍◎●◯"""  # Circle progression
    
    elif options == 30:
         chars = "--chars="" ᗧᗢᗣᗤᗨᗩᗪᗫ"""  # Unique Unicode shapes
    
    elif options == 31:
        chars = "--chars="" ░▒▓▚▞▀▄█"""  # Mixed block types
    elif options == 32:
        asc.typewrite(asc.Colors.RED + "Characters (min 2):\n")
        chars = f"--chars={input()}"
else:
    chars = ""

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
    chars,
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

FOLDER = "../JP2ASettings"

if os.path.exists(FOLDER):
    shutil.rmtree(FOLDER)
os.makedirs(FOLDER, exist_ok=True)

config = {"jp2a_args": asc.clean_args(jp2a_cmd)}

with open("../JP2ASettings/jp2aconfig.json", "w+",encoding="utf-8") as f:
    json.dump(config,f,indent=4)

# ---------------------------------------------
# INPUT FOLDER
# ---------------------------------------------

FOLDER = "../PngFrames"

folder = sys.argv[1] if len(sys.argv) > 1 else FOLDER

png_files = sorted(
    (f for f in os.listdir(folder) if f.endswith(".png")),
    key=lambda x: int(os.path.splitext(x)[0])
)

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
out = "Gif2Asc/Engine/TextFrames"

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