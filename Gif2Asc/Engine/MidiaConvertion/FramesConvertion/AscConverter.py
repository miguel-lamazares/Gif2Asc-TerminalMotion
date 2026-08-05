#!/usr/bin/env python3

from __future__ import annotations
import os, sys, json, subprocess, shutil
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
MIDIA_CONVERSION_ROOT = HERE.parent
    
sys.path.insert(0, str(MIDIA_CONVERSION_ROOT))  
sys.path.insert(0, str(HERE))                     

from TermForge.termforge.Terminal import (
    banner, gradient, glitch, box, Spinner, progress,
    arrow_menu, clear, confirm, rgb, RESET, typewriter, confirmJp2a, confirmSize, confirmColors
)
from TermForge.termforge.ROOT import png_dir, text_dir, settings_dir
from Defs.Defs import select_charset, center_ascii_frame

CFG_PATH = settings_dir() / "jp2aconfig.json"

def _ask_int(label: str, default: int, lo=1, hi=400) -> int:
    while True:
        raw = input(rgb(0,220,255) + f"  {label} " + RESET + rgb(120,120,140) + f"[{default}]" + RESET + " > ").strip()
        if not raw: return default
        try:
            v = int(raw)
            if lo <= v <= hi: return v
        except ValueError: pass
        glitch(f"  ✗ invalid (need int between {lo} and {hi})")

def _build_jp2a_args(cfg: dict) -> list[str]:
        """Constrói argumentos jp2a de forma limpa e modular (melhoria da versão nova)"""
        args = [
            f"--width={cfg['width']}", 
            f"--height={cfg['height']}",
            f"--chars={cfg['charset']}"
        ]
        
        if cfg.get("border"): args.append("--border")
        if cfg.get("fit"): args.append("--term-fit")
        if cfg.get("background"): args.append(f"--background={cfg['background']}")
        if cfg.get("proportion"): args.append(cfg["proportion"])
        
        if cfg["color_mode"] == "truecolor":
            args.extend(["--colors", "--color-depth=24"])
        elif cfg["color_mode"] == "manual":
            args.extend([
                "--colors",
                f"--color-depth={cfg['color_depth']}",
                f"--red={cfg['red_weight']}",
                f"--green={cfg['green_weight']}",
                f"--blue={cfg['blue_weight']}",
            ])
         
        return args

def _calculate_smart_size(folder: Path) -> str:
        """Lógica inteligente de tamanho da versão antiga (preservada e isolada)"""
        max_width, max_height = 0, 0
        png_files = sorted(
            (f for f in folder.iterdir() if f.suffix.lower() == ".png"),
            key=lambda x: int(x.stem) if x.stem.isdigit() else 0
        )
        
        for png in png_files:
            with Image.open(png) as img:
                w, h = img.size
                max_width = max(max_width, w)
                max_height = max(max_height, h)
        
        if max_width == 0 or max_height == 0:
            return "--size=80x24"  
        
        term_size = shutil.get_terminal_size()
        term_width, term_height = term_size.columns, term_size.lines
        
        
        ASCII_RATIO = 0.5
        
        img_ratio = max_width / max_height
        term_ratio = term_width / (term_height / ASCII_RATIO)
        
        if img_ratio > term_ratio:  
            smart_width = term_width
            smart_height = int((term_width / img_ratio) * ASCII_RATIO)
        else:  
            smart_height = term_height
            smart_width = int((term_height * img_ratio) / ASCII_RATIO)
        
        return f"--size={smart_width}x{smart_height}"

def _wizard() -> None:
        """Wizard de configuração - usando SEU TermForge para TODA a UI"""
        # === TELA INICIAL (usando SEU TermForge) ===
        banner("⟢ jp2a Wizard", "configure how your PNGs become art")
        
        typewriter("Configure your jp2a\n", 0.04, color=rgb(140,140,160))
        typewriter("Border and text\n\n", 0.02, color=rgb(0,255,0))
        
        border_choice = confirmJp2a("Border?")
        # normalize truthy responses from different implementations
        # accept True/1 as yes, everything else as no
        border = "--border" if bool(border_choice) else ""
        
        clear()
        
        if confirmJp2a("Special characters?") in (1, 0):
            clear()
            name, glyphs = select_charset()
            # ensure at least one glyph is selected and confirm selection with the user
            while not glyphs or confirmJp2a(f"Use charset '{name}'?") not in (1, 0):
                if not glyphs:
                    typewriter("Please select at least one glyph...", 0.02, color=rgb(255,140,0))
                name, glyphs = select_charset()

            print()
            

        clear()
        
        fit = "--term-fit" if confirmJp2a("Frame is big?") in (1, 0) else ""
        
        clear()
        
        bg_choice = confirmJp2a("Light characters on dark background?")
        background = "--background=dark" if bg_choice in (1, 0) else "--background=light"
        
        clear()
        
        user_wants_center = (confirmJp2a("Do you want to center the image?") in (1, 0))
        
        clear()
        
        # === SEÇÃO: PROPORÇÃO/TAMANHO (5 modos da sua versão antiga) ===
        typewriter("Proportion\n\n", 0.02, color=rgb(255,255,0))
        
        choice = confirmSize("what size mode do you want?")
        
        proportion = ""
        full_size_mode = False
        smart_full_size = False
        
        if choice == 0:  # Custom WxH
            typewriter("Width: ", 0.03, color=rgb(0,220,255))
            w_input = input().strip()
            typewriter("Height: ", 0.03, color=rgb(0,220,255))
            h_input = input().strip()
            proportion = f"--size={w_input}x{h_input}"
            print()  # Nova linha após inputs
        elif choice == 1:  # Terminal zoom
            proportion = "--term-zoom"
        elif choice == 2:  # Fullscreen
            full_size_mode = True
        elif choice == 3:  # Smart full size
            smart_full_size = True
        
        # Processa modos especiais de tamanho
        if smart_full_size:
            # Usa a função isolada (mais limpa)
            frames_folder = png_dir()
            proportion = _calculate_smart_size(frames_folder)
        elif full_size_mode:
            # Lógica de fullsize da sua versão antiga (adaptada para TermForge)
            typewriter("Analyzing frames for full size mode...\n", 0.02, color=rgb(0,220,255))
            
            frames_folder = png_dir()
            
            max_width, max_height = 0, 0
            png_files = sorted(
                (f for f in frames_folder.iterdir() if f.suffix.lower() == ".png"),
                key=lambda x: int(x.stem) if x.stem.isdigit() else 0
            )
            
            for png in png_files:
                with Image.open(png) as img:
                    w, h = img.size
                    max_width = max(max_width, w)
                    max_height = max(max_height, h)
            
            if max_width == 0 or max_height == 0:
                proportion = "--size=80x24"  # fallback
                typewriter("No valid PNGs found - using default size\n", 0.02, color=rgb(255,100,100))
            else:
                term_size = shutil.get_terminal_size()
                term_width = term_size.columns
                term_height = (term_size.lines - 2) * 1.7  # Ajuste para linhas de terminal (do seu código antigo)
                
                width_ratio = term_width / max_width if max_width > 0 else 1
                height_ratio = term_height / max_height if max_height > 0 else 1
                scale = min(width_ratio, height_ratio)
                
                # Ajuste específico para ASCII (do seu código antigo)
                ascii_adjustment = 0.5 if scale < 1 else 0.7
                
                if scale < 1:  # Precisa escalar para baixo
                    smart_width = int(max_width * scale)
                    smart_height = int(max_height * scale * ascii_adjustment)
                    proportion = f"--size={smart_width}x{smart_height}"
                    typewriter(f"Scaling to fit terminal: {smart_width}x{smart_height} (scale: {scale:.2f})\n", 
                              0.02, color=rgb(0,255,160))
                else:  # Cabe no terminal (com ajuste ASCII)
                    adjusted_height = int(max_height * ascii_adjustment)
                    proportion = f"--size={max_width}x{adjusted_height}"
                    typewriter(f"Images fit terminal at original size (adjusted for ASCII)\n", 
                              0.02, color=rgb(0,255,160))
        
        clear()
        
        color_mode_choice = confirmColors("what color mode do you want?")
        
        if color_mode_choice == 0:
            color_mode = "truecolor"
            color_depth = red_weight = green_weight = blue_weight = None
        elif color_mode_choice == 1:
            color_mode = "black_andwhite"
            color_depth = red_weight = green_weight = blue_weight = None
        elif color_mode_choice == 2:
            color_mode = "manual"
            typewriter("Red   (default 0.2989): ", 0.03, color=rgb(0,220,255))
            red = input().strip() or "0.2989"
            typewriter("Green (default 0.5866): ", 0.03, color=rgb(0,220,255))
            green = input().strip() or "0.5866"
            typewriter("Blue  (default 0.1145): ", 0.03, color=rgb(0,220,255))
            blue = input().strip() or "0.1145"
            typewriter("Color depth (4 / 8 / 24): ", 0.03, color=rgb(0,220,255))
            depth = input().strip() or "24"
            color_depth = depth
            red_weight = red
            green_weight = green
            blue_weight = blue
            print()  
        else:
            print(glitch("Invalid option."))
            sys.exit(1)
        
        clear()
        
        cfg = {
            "charset_name": name,
            "charset": glyphs,
            "width": 100,  
            "height": 30,  
            "invert": False,  
            "border": bool(border),
            "fit": bool(fit),
            "proportion": proportion if proportion else None,
            "background": background.replace("--background=", ""),  
            "color_mode": color_mode,
            "color_depth": color_depth if color_mode == "manual" else None,
            "red_weight": red_weight if color_mode == "manual" else None,
            "green_weight": green_weight if color_mode == "manual" else None,
            "blue_weight": blue_weight if color_mode == "manual" else None,
            "user_wants_center": user_wants_center
        }
        
        settings_dir().mkdir(parents=True, exist_ok=True)
        CFG_PATH.write_text(json.dumps(cfg, indent=2))
       
        print(box(f"✔ saved → {CFG_PATH.name}", color=(0,255,160)) + "\n")
        
        return cfg


def _load_config() -> dict:
        """Carrega configuração salva do arquivo JSON"""
        if not CFG_PATH.exists():
            print(glitch(f"  ✗ configuration not found: {CFG_PATH}"))
            print("  Please run the wizard first to generate a configuration.")
            sys.exit(1)
        
        try:
            return json.loads(CFG_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            print(glitch(f"  ✗ failed to load configuration: {e}"))
            sys.exit(1)

def jp2a_args(cfg: dict) -> list[str]:
    args = [f"--width={cfg['width']}", f"--height={cfg['height']}",
            f"--chars={cfg['charset']}"]
    if cfg.get("invert"): args.append("--invert")
    if cfg.get("color"):  args.append("--color")
    return args

def render(cfg: dict):
        """Renderização de frames - usando SEU TermForge para UI e lógica"""
        
        if not shutil.which("jp2a"):
            print(glitch("  ✗ jp2a not found in PATH — install it first."))
            sys.exit(1)
         
        png_folder = png_dir()   
        asc_folder = text_dir()  
        
        asc_folder.mkdir(parents=True, exist_ok=True)
        
        pngs = sorted(
            (p for p in png_folder.iterdir() if p.suffix.lower() == ".png"),
            key=lambda p: int(p.stem) if p.stem.isdigit() else 0
        )
        
        if not pngs:
            print(glitch(f"  ✗ no PNGs in {png_folder}"))
            sys.exit(1)
        
        jp2a_args = _build_jp2a_args(cfg)
        
        print(gradient(f"\n⟶ rendering {len(pngs)} frames\n"))
        
        # ensure output folder exists and clean old .asc files before writing new ones
        asc_folder.mkdir(parents=True, exist_ok=True)

        if asc_folder.exists():
            for old_file in asc_folder.glob("*.asc"):
                try:
                    old_file.unlink()
                except PermissionError:
                    pass

        for i, png in enumerate(pngs, 1):
            out = asc_folder / f"{i-1:09d}.asc"
            
            result = subprocess.run(
                ["jp2a", *jp2a_args, str(png)],
                capture_output=True,
                text=True
            )
            
            processed_output = (
                center_ascii_frame(result.stdout) 
                if cfg["user_wants_center"] 
                else result.stdout
            )
            
            out.write_text(processed_output, encoding="utf-8")
            
            progress(i, len(pngs), label=png.name)
        
        print(box(f"✔ wrote {len(pngs)} .asc → {asc_folder.name}", color=(0,255,160)) + "\n")
    
if __name__ == "__main__":
     if CFG_PATH.exists() and confirm("\nUse existing configuration? (y/n) [y]: "):
            cfg = _load_config()
            render(cfg)
     else:
         cfg = _wizard()
         render(cfg)

   


