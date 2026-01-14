import sys
import time
import os
import requests
import shutil
import re



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





