from PIL import Image

gif = Image.open("/home/dex/Documentos/GitHub/Inutil-things-for-JAVA/Gif/Gif to frames/gif.gif")
for i in range(gif.n_frames):
    gif.seek(i)
    gif.save(f"/home/dex/Documentos/GitHub/Inutil-things-for-JAVA/Gif/Gif to frames/Frame in png/frame_{i}.png")
