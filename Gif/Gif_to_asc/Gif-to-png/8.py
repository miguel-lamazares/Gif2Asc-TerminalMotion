from PIL import Image
import os
import sys
import shutil
from TerminalLib import asc

print("\033[H\033[2J", flush=True)
xz = input("what's the GIF's address?: ")

output_dir = "/home/dex/Documentos/GitHub/Inutil-things-for-JAVA/Gif/Gif_to_asc/Frame in png"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)


gif = Image.open(xz)
for i in range(gif.n_frames):
    gif.seek(i)
    gif.save(f"{output_dir}/frame_{i}.png")
    
    asc.print_progress_bar(i + 1, gif.n_frames)

