from PIL import Image
import os
import sys
import shutil


def print_progress_bar(current, total, bar_length=20):
    progress = current / total
    filled_length = int(bar_length * progress)
    bar = '∎' * filled_length + '.' * (bar_length - filled_length)
    sys.stdout.write(f'\r[{bar}] {current}/{total}')
    sys.stdout.flush()
    if current == total:
        print()

xz = input("what's the GIF's address?: ")

output_dir = "Frame in png"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)


gif = Image.open(xz)
for i in range(gif.n_frames):
    gif.seek(i)
    gif.save(f"{output_dir}/frame_{i}.png")
    
    print_progress_bar(i + 1, gif.n_frames)

