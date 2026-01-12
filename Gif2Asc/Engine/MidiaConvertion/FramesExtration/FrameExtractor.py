from PIL import Image
import subprocess
import os

import shutil
from TerminalLib import Terminal as ter
from TerminalLib import asc

print("\033[H\033[2J", flush=True)

song_output = "Gif2Asc/Engine/MidiaConvertion/FramesExtration/Song"
output_dir = "Gif2Asc/Engine/MidiaConvertion/PngFrames"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

if not os.path.exists(song_output):
                os.makedirs(song_output, exist_ok=True)

asc_files = sorted(f for f in os.listdir(song_output) if f.endswith(".wav"))

for file in asc_files:
    os.remove(os.path.join(song_output, file))


input_file = input("what's the GIF's address?: ")

if input_file.startswith("https:") or input_file.startswith("http:") is True:
    folder = "./Downloads"
    asc.download(input_file, folder)
    input_file = f"{folder}/gif.gif"

if input_file.endswith(".jpeg") or input_file.endswith(".jpg") or input_file.endswith(".svg") is True:
    convert_input = asc.convert_to_png(input_file, output_path=output_dir)
    input_file = convert_input

    ter.typewrite(ter.Colors.GREEN + "Do you wanna play something with it? (1 - yes / 2 - no)", 0.02)
    song_choice = ter.read_int(1, 2)
    if song_choice == 1:
        ter.typewrite(ter.Colors.GREEN + "What's the song's address?", 0.02)
        song_path = input("-> ")
        if not os.path.exists(song_path):
            ter.typewrite(ter.Colors.RED + "File not found!", 0.02)
            exit()
        subprocess.run(["ffmpeg", "-i", song_path, "-ar", "22050", "-ac", "1", "-f", "wav", f"{song_output}/song.wav"])
        song_path = "song.wav"

elif input_file.endswith(".gif") or input_file.endswith(".webp") or input_file.endswith(".png") is True:
    ter.typewrite(ter.Colors.GREEN + "Do you wanna play something with it? (1 - yes / 2 - no)", 0.02)
    song_choice = ter.read_int(1, 2)
    if song_choice == 1:
        ter.typewrite(ter.Colors.GREEN + "What's the song's address? (must be wav or wav)", 0.02)
        song_path = input("-> ")
        if not os.path.exists(song_path):
            ter.typewrite(ter.Colors.RED + "File not found!", 0.02)
            exit()
        subprocess.run(["ffmpeg", "-i", song_path, "-ar", "22050", "-ac", "1", "-f", "wav", f"{song_output}/song.wav"])
        song_path = "song.wav"
                
    gif = Image.open(input_file)
    for i in range(gif.n_frames):
        gif.seek(i)
        gif.save(f"{output_dir}/{i}.png")

        ter.print_progress_bar(i + 1, gif.n_frames)

elif input_file.endswith(".mp4") or input_file.endswith(".mov") or input_file.endswith(".avi") or input_file.endswith(".mkv") or input_file.endswith(".webm") is True:
    ter.typewrite(ter.Colors.GREEN + "Do you wanna play some audio? (1 - yes / 2 - no: )", 0.02)
    song_choice = ter.read_int(1, 2)
    if song_choice == 1:
            ter.typewrite(ter.Colors.GREEN + "Do you wanna play the itself audio or by other file?", 0.02)
            song_choice = ter.read_int(1, 2, "1 - itself audio / 2 - other file: ")
            if song_choice == 1:
                subprocess.run(["ffmpeg", "-nostats", "-i", input_file, f"{output_dir}/%d.png"])
                subprocess.run(["ffmpeg", "-i", input_file, "-ar", "22050", "-ac", "1", "-f", "wav", f"{song_output}/song.wav"])
                ter.Clear_all()
            if song_choice == 2:
                ter.typewrite(ter.Colors.GREEN + "What's the song's address? (must be wav or wav)", 0.02)
                song_path = input("-> ")
                if not os.path.exists(song_path):
                    ter.typewrite(ter.Colors.RED + "File not found!", 0.02)
                    exit()
                subprocess.run(["ffmpeg", "-i", song_path, "-ar", "22050", "-ac", "1", "-f", "wav", f"{song_output}/song.wav"])
                subprocess.run(["ffmpeg", "-nostats", "-i", input_file, f"{output_dir}/%d.png"])
                ter.Clear_all()
    else:
            subprocess.run(["ffmpeg", "-nostats", "-i", input_file, f"{output_dir}/%d.png"])
            ter.Clear_all()
    

else:
    ter.Clear_all()
    ter.typewrite(ter.Colors.RED + "Invalid file format. Please provide a GIF, image file or video file.", 0.02)