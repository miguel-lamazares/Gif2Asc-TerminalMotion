from PIL import Image
import subprocess
import os

import shutil
from TerminalLib import asc

print("\033[H\033[2J", flush=True)

song_output = "./Song"
output_dir = "../PngFrames"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

input_file = input("what's the GIF's address?: ")

if input_file.startswith("https:" or "http:"):
    folder = "./Downloads"
    asc.download(input_file, folder)
    input_file = f"{folder}/gif.gif"

if input_file.endswith(".jpeg" or ".jpg" or ".svg") is True:
    convert_input = asc.convert_to_png(input_file, output_path=output_dir)
    input_file = convert_input
     
    asc.typewrite(asc.Colors.GREEN + "Do you wanna play something with it? (1 - yes / 2 - no)", 0.02)
    song_choice = asc.read_int(1, 2)
    if song_choice == 1:
        asc.typewrite(asc.Colors.GREEN + "What's the song's address? (must be mp3 or mp3)", 0.02)
        song_path = input("-> ")
        if not os.path.exists(song_path):
            asc.typewrite(asc.Colors.RED + "File not found!", 0.02)
            exit()
        subprocess.run(["ffmpeg", "-i", song_path, "-ar", "22050", "-ac", "1", "-f", "mp3", f"{song_output}/song.wav"])
        song_path = "song.mp3"

elif input_file.endswith(".gif" or ".png" or ".webp") is True:
    asc.typewrite(asc.Colors.GREEN + "Do you wanna play something with it? (1 - yes / 2 - no)", 0.02)
    song_choice = asc.read_int(1, 2)
    if song_choice == 1:
        asc.typewrite(asc.Colors.GREEN + "What's the song's address? (must be mp3 or mp3)", 0.02)
        song_path = input("-> ")
        if not os.path.exists(song_path):
            asc.typewrite(asc.Colors.RED + "File not found!", 0.02)
            exit()
        subprocess.run(["ffmpeg", "-i", song_path, "-ar", "22050", "-ac", "1", "-f", "mp3", f"{song_output}/song.wav"])
        song_path = "song.mp3"
                
    gif = Image.open(input_file)
    for i in range(gif.n_frames):
        gif.seek(i)
        gif.save(f"{output_dir}/{i}.png")

        asc.print_progress_bar(i + 1, gif.n_frames)

elif input_file.endswith(".mp4" or ".mov" or ".avi" or ".mkv" or ".webm") is True:
    asc.typewrite(asc.Colors.GREEN + "Do you wanna play the song of this video? (1 - yes / 2 - no: )", 0.02)
    song_choice = asc.read_int(1, 2)
    if song_choice == 1:
            subprocess.run(["ffmpeg", "-nostats", "-i", input_file, f"{output_dir}/%d.png"])
            subprocess.run(["ffmpeg", "-i", input_file, "-ar", "22050", "-ac", "1", "-f", "mp3", f"{song_output}/song.mp3"])
            asc.Clear_all()
    else:
            subprocess.run(["ffmpeg", "-nostats", "-i", input_file, f"{output_dir}/%d.png"])
            asc.Clear_all()
    

else:
    asc.Clear_all()
    asc.typewrite(asc.Colors.RED + "Invalid file format. Please provide a GIF, image file or video file.", 0.02)