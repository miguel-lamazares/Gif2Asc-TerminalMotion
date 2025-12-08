import os
import subprocess

folder = "/home/dex/Documentos/GitHub/Inutil-things-for-JAVA/Gif/Gif to frames/Frame in png"

png_files = [f for f in sorted(os.listdir(folder)) if f.endswith(".png")]

asc_frames = []

for filename in png_files:
    path = os.path.join(folder, filename)

    result = subprocess.run(['jp2a', path], capture_output=True, text=True)
    asc_frames.append(result.stdout)



with open("/home/dex/Documentos/GitHub/Inutil-things-for-JAVA/Gif/Loop/AscFrames/Frames.java", "w", encoding="utf-8") as f:
    f.write("package Gif.Loop.cave.AscFrames;\n\npublic class art {\n\n")
    
    for i, frame in enumerate(asc_frames):
        
        escaped = frame.replace("\\", "\\\\").replace("\"", "\\\"")
        lines = escaped.splitlines()
        
        if not lines:  
            f.write(f"    public static String frame{i} = \"\";\n\n")
            continue
            
        
        if len(lines) == 1:
            f.write(f"    public static String frame{i} = \"{lines[0]}\";\n\n")
        else:
            
            f.write(f"    public static String frame{i} = \"\"\"\n")
            f.write(frame.replace("\\", "\\\\"))  
            f.write("\"\"\";\n\n")
    
    f.write("}\n")

print("Arquivo Frames.java gerado com sucesso!")