import sys
import time
import os
import requests
import shutil

def Clear_all():
    print("\033[H\033[2J", flush=True)

def wait_enter_clear(prompt="\n\nPress Enter..."):
    input(prompt)
    print("\033[F\033[K", end="")

class Colors():
    RESET = "\u001B[0m";
    BLACK = "\u001B[30m";
    RED = "\u001B[31m";
    GREEN = "\u001B[32m";
    YELLOW = "\u001B[33m";
    BLUE = "\u001B[34m";
    PURPLE = "\u001B[35m";
    CYAN = "\u001B[36m";
    WHITE = "\u001B[37m";


def read_int(Min_value: int,max_value: int) -> int:
    while True:
        user_input = input()

        if not user_input.strip().isdigit():
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            continue

        choice = int(user_input)

        if choice <= Min_value - 1:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            continue

        if choice >= max_value + 1:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            continue

        return choice
    
    
def typewrite(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  

def print_progress_bar(current, total, bar_length=20):

    progress = current / total
    filled_length = int(bar_length * progress)
    bar = '∎' * filled_length + '.' * (bar_length - filled_length)
    por = current / total * 100;
    sys.stdout.write(f'\r[{bar}] {por}% {current}/{total}')
    sys.stdout.flush()
    if current == total:
        print()

def clean_args(cmd):
    return [arg for arg in cmd if arg]

def download(URL, outdir):

    if os.path.exists(outdir):
        shutil.rmtree(outdir)
    os.makedirs(outdir, exist_ok=True)
    
    filename = "gif.gif"
    filepath = os.path.join(outdir, filename)
    headers = {
        "User-Agent": "Mozilla/5.0 (TerminalLib GIF Downloader)"
    }
    
    try: 
        
        r = requests.get(URL, headers=headers,stream=True, timeout=15)
        r.raise_for_status()
        
        with open(filepath, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        return filepath
        
    except Exception as e:
        print(f"{URL} can't be installed: {e}")
        return None
    

def convert_to_png(input_path, output_path):
    from PIL import Image
    i = 0
    img = Image.open(input_path)
    png_path = os.path.splitext(input_path)[0] + ".png"
    img.save(f"{output_path}/frame{i}.png", "PNG")
    return png_path