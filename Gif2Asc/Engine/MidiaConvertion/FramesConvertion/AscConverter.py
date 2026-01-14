import os
import subprocess
import sys
import PIL.Image as Image
from TerminalLib import Terminal as ter
from TerminalLib import asc
import json
import shutil
from Defs import Defs
from TerminalLib import ROOT

# ---------------------------------------------
# UI — BASIC OPTIONS
# ---------------------------------------------
ter.Clear_all()

ter.typewrite(ter.Colors.PURPLE + "Configure your jp2a\n", 0.04)
ter.typewrite(ter.Colors.GREEN + "Border and text\n\n", 0.02)

ter.typewrite(ter.Colors.CYAN + "Border? (1 - yes / 2 - no)\n", 0.02)
border = "--border" if ter.read_int(1,3) == 1 else ""

ter.Clear_all()
ter.typewrite(ter.Colors.CYAN + "Special characters? (1 - yes / 2 - no)\n", 0.02)
if ter.read_int(1,3) == 1:
    ter.Clear_all()

    Defs.options_list()

    options = ter.read_int(1, 32)
  
    if options == 1:
        chars = "--chars="" ░▒▓█"""  # Original blocks
    elif options == 2:
        chars = "--chars="" ⣀⣤⣶⣯⣟⣷⣿"""  # Braille gradient
    elif options == 3:
        chars = "--chars="" ⠁⠃⠇⠏⠟⠿⡿⣿"""  # Spaced braille
    elif options == 4:
        chars = "--chars="" ▘▝▖▗▌▐▀▄█"""  # Half blocks
    elif options == 5:
        chars = "--chars="" ･｡ｧｨｩｪｫｰｱﾏﾓﾜ"""  # Japanese
    elif options == 6:
        ter.Clear_all()
        ter.typewrite(ter.Colors.RED + "Characters (min 2):\n")
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

else:
    chars = ""

ter.Clear_all()

ter.typewrite(ter.Colors.CYAN + "Frame is big? (1 - yes / 2 - no)\n", 0.02)
fit = "--term-fit" if ter.read_int(1,3) == 1 else ""

ter.Clear_all()

ter.typewrite(
    ter.Colors.CYAN +
    "Light characters on dark background? (1 - yes / 2 - no)\n",
    0.02
)
back = "--background=dark" if ter.read_int(1,3) == 1 else "--background=light"
ter.Clear_all()

ter.typewrite(
    ter.Colors.CYAN +
    "Do you want to center the image? (1 - yes / 2 - no)\n\n",
    0.02
)
center = "--term-center" if ter.read_int(1,3) == 1 else ""
ter.Clear_all()

# ---------------------------------------------
# SIZE / PROPORTION
# ---------------------------------------------

ter.typewrite(ter.Colors.YELLOW + "Proportion\n\n", 0.02)
ter.typewrite(
    ter.Colors.CYAN +
    "1. Default\n2. Set width and height\n3. Use terminal zoom\n4. Fullscreen\n5. Smart full size \n\n",
    0.02
)

choice = ter.read_int(1,5)
proportion = ""
full_size_mode = False
smart_full_size = False


if choice == 2:
    ter.typewrite("Width: ", 0.03)
    w = input()
    ter.typewrite("Height: ", 0.03)
    h = input()
    proportion = f"--size={w}x{h}"
elif choice == 3:
    proportion = "--term-zoom"
elif choice == 4:
    full_size_mode = True
elif choice == 5:
    smart_full_size = True

if smart_full_size:
    max_image_width = 0
    max_image_height = 0
    FOLDER = ROOT.Addresses.PngFrames

    folder = sys.argv[1] if len(sys.argv) > 1 else FOLDER

    png_files = sorted(
        (f for f in os.listdir(folder) if f.endswith(".png")),
        key=lambda x: int(os.path.splitext(x)[0])
    )

    for file in png_files:
        path = os.path.join(folder, file)
        with Image.open(path) as img:
            width, height = img.size
            max_image_width = max(max_image_width, width)
            max_image_height = max(max_image_height, height)

    term = shutil.get_terminal_size()

    
    ASCII_RATIO = 0.5

    
    term_width = term.columns
    term_height = term.lines

    
    img_ratio = max_image_width / max_image_height
    term_ratio = term_width / (term_height / ASCII_RATIO)

    if img_ratio > term_ratio:
        
        smart_width = term_width
        smart_height = int((term_width / img_ratio) * ASCII_RATIO)
    else:
        
        smart_height = term_height
        smart_width = int((term_height * img_ratio) / ASCII_RATIO)

    proportion = f"--size={smart_width}x{smart_height}"


elif full_size_mode:
    max_image_width = 0
    max_image_height = 0
    
    ter.typewrite(ter.Colors.CYAN + "Analyzing frames for full size mode...\n", 0.02)
    
    FOLDER = ROOT.Addresses.PngFrames

    folder = sys.argv[1] if len(sys.argv) > 1 else FOLDER

    png_files = sorted(
        (f for f in os.listdir(folder) if f.endswith(".png")),
        key=lambda x: int(os.path.splitext(x)[0])
    )

    for i, file in enumerate(png_files):
        path = os.path.join(folder, file)
        with Image.open(path) as img:
            width, height = img.size
            max_image_width = max(max_image_width, width)
            max_image_height = max(max_image_height, height)
    
    ter.typewrite(f"Max dimensions found: {max_image_width}x{max_image_height}\n", 0.02)
    
    term_size = shutil.get_terminal_size()
    term_width = term_size.columns
    
    term_height = (term_size.lines - 2) * 1.7
    
    width_ratio = term_width / max_image_width if max_image_width > 0 else 1
    height_ratio = term_height / max_image_height if max_image_height > 0 else 1
    scale = min(width_ratio, height_ratio)
    
    ascii_adjustment = 0.5 if scale < 1 else 0.7
    
    if scale < 1:
       
        smart_width = int(max_image_width * scale)
        smart_height = int(max_image_height * scale * ascii_adjustment)
        proportion = f"--size={smart_width}x{smart_height}"
        ter.typewrite(f"Scaling to fit terminal: {smart_width}x{smart_height} (scale: {scale:.2f})\n", 0.02)
        full_size_mode = False  
    else:
        adjusted_height = int(max_image_height * ascii_adjustment)
        proportion = f"--size={max_image_width}x{adjusted_height}"
        ter.typewrite(f"Images fit terminal at original size (adjusted for ASCII)\n", 0.02)

ter.Clear_all()

# ---------------------------------------------
# COLORS
# ---------------------------------------------

ter.typewrite(ter.Colors.GREEN + "Colors\n\n", 0.02)
ter.typewrite(
    ter.Colors.CYAN +
    "1. True colors\n2. Black and white\n3. Manual config\n",
    0.02
)

mode = ter.read_int(1,3)

jp2a_cmd = ["jp2a"]

if mode == 1:
    jp2a_cmd += [
        "--colors",
        "--color-depth=24",
        
    ]

elif mode == 2:
    pass 

elif mode == 3:
    ter.typewrite("Red   (default 0.2989): ", 0.03)
    red = input()
    ter.typewrite("Green (default 0.5866): ", 0.03)
    green = input()
    ter.typewrite("Blue  (default 0.1145): ", 0.03)
    blue = input()
    ter.typewrite("Color depth (4 / 8 / 24): ", 0.03)
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

ter.Clear_all()
print(ter.Colors.RESET + "")

# ---------------------------------------------
# Saving configs
# ---------------------------------------------

FOLDER = ROOT.Addresses.Settings

if os.path.exists(FOLDER):
    shutil.rmtree(FOLDER)
os.makedirs(FOLDER, exist_ok=True)

config = {"jp2a_args": asc.clean_args(jp2a_cmd)}

with open(ROOT.Addresses.Settings / "jp2aconfig.json", "w+",encoding="utf-8") as f:
    json.dump(config,f,indent=4)

# ---------------------------------------------
# INPUT FOLDER
# ---------------------------------------------

FOLDER = ROOT.Addresses.PngFrames

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
    ter.print_progress_bar(i + 1, total)

# ---------------------------------------------
#  CLEANING OLD FRAMES
# ---------------------------------------------
out = ROOT.Addresses.TextFrames

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


