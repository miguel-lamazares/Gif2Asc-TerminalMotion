
python ./Gif/Gif_to_asc/8.py
python ./Gif/Gif_to_asc/JP2a.py

gcc Gif/AscFramesInC/Render.c -o Render
javac Gif/AscFrames/*.java Gif/Loop/gif.java

java Gif.Loop.gif
