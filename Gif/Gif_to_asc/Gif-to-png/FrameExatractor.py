from PIL import Image
import subprocess
import os

import shutil
from TerminalLib import asc

print("\033[H\033[2J", flush=True)

output_dir = "./Gif/Gif_to_asc/Frame in png"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

input_file = input("what's the GIF's address?: ")

if input_file.startswith("https:" or "http:"):
    folder = "Gif/Gif_to_asc/Gif-to-png/Downloads"
    asc.download(input_file, folder)
    input_file = f"{folder}/gif.gif"

if input_file.endswith(".jpeg" or ".jpg" or ".svg") is True:
    convert_input = asc.convert_to_png(input_file, output_path=output_dir)
    input_file = convert_input
    print(convert_input)

elif input_file.endswith(".gif" or ".png" or ".webp") is True:
    gif = Image.open(input_file)
    for i in range(gif.n_frames):
        gif.seek(i)
        gif.save(f"{output_dir}/frame_{i}.png")

        asc.print_progress_bar(i + 1, gif.n_frames)

elif input_file.endswith(".mp4" or ".mov" or ".avi" or ".mkv" or ".webm") is True:
    subprocess.run(["ffmpeg", "-nostats", "-i", input_file, f"{output_dir}/frame_%d.png"])
    asc.Clear_all()

else:
    asc.Clear_all()
    asc.typewrite(asc.Colors.RED + "Invalid file format. Please provide a GIF, image file or video file.", 0.02)