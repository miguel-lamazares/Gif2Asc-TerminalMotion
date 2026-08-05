
from __future__ import annotations
import sys, os, shutil,re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "TerminalLib"))
from TermForge.termforge.Terminal import arrow_menu, gradient, rgb, RESET, box

CHARSETS: dict[str, str] = {
    "minimal":      " .:-=+*#%@",
    "blocks":       " ░▒▓█",
    "shades":       " ·•◦●",
    "matrix":       " .:-=+*ﾊﾐﾆｻﾜﾈ",
    "ink":          " .,'`^\":;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",
    "newspaper":    " .,:;clodxkO0KXNWM",
    "binary":       " 01",
    "hex":          " 0123456789ABCDEF",
    "dots":         " .·:•●",
    "stars":        " .*+✦★",
    "lines":        " ─━│┃┄┅┆┇┈┉┊┋",
    "arrows":       " ←↑→↓↔↕⇐⇑⇒⇓",
    "math":         " +-×÷=≠≈≡∑∏∫",
    "currency":     " $¢£¥€₹₽",
    "geometric":    " ▲△▼▽◆◇○●□■",
    "playing":      " ♠♣♥♦",
    "music":        " ♩♪♫♬♭♮♯",
    "weather":      " ☀☁☂☃☄",
    "tech":         " ⌘⌥⌃⇧⏎⏏⌫",
    "circle":       " ◐◑◒◓◔◕○●",
    "square":       " ▖▗▘▙▚▛▜▝▞▟",
    "wave":         " ∿〜〰",
    "dash":         " -—–",
    "punct":        " .,;:!?'\"",
    "letters":      " abcdefghijklmnopqrstuvwxyz",
    "letters_up":   " ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "numbers":      " 0123456789",
    "russian":      " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
    "greek":        " αβγδεζηθικλμνξοπρστυφχψω",
    "katakana":     " ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄ",
    "ascii_full":   " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
    
    "Original blocks": " ░▒▓█",
    "Braille gradient": " ⣀⣤⣶⣯⣟⣷⣿",
    "Spaced braille": " ⠁⠃⠇⠏⠟⠿⡿⣿",
    "Half blocks": " ▘▝▖▗▌▐▀▄█",
    "Japanese": " ･｡ｧｨｩｪｫｰｱﾏﾓﾜ",
    "ASCII art basic": " .:;+*?%$@#",
    "Box drawing": " ─│┌┐└┘├┤┬┴┼",
    "Geometric": " ▲▼◀▶◆■○●□△▽◇◊",
    "Dot progression": " ·•∙⦁●◌○◎◉●◯",
    "Quadrants": " ▖▗▘▝▚▞▙▟",
    "Sextants": " 🬀🬁🬂🬃🬄🬅🬆🬇🬈🬉",
    "Technical symbols": " ⌘⌥⎇⏎␣⏏⚙️🔧🛠️",
    "Wedge shapes": " ◢◣◤◥◸◹◺◿",
    "Latin letters": " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "Alphanumeric": " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    "Extra symbols": " ★☆♪♫♥♦♣♠☀☁☂☃",
    "Solid block progression": " █▉▊▋▌▍▎▏",
    "Vertical halves": " ▀▄█",
    "Full-width": " ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ",
    "Digital/circled numbers": " ⓪①②③④⑤⑥⑦⑧⑨",
    "Math symbols": " +−×÷=≠≈±√∞∫∑∏∂",
    "Minimalist small dots": " ·∙∙⸱⸳⸰ꓸ",
    "Mixed density gradient": " .:^~+*xX%&$@#█",
    "Artistic/flow symbols": " ۞۩≋≌∿≈～〰️♪♫♬",
    "Binary/barcode style": " 01█",
    "Vertical bar gradient": " ▏▎▍▌▋▊▉█▇▆▅▄▃▂▁",
    "Asian-inspired": " ╱╲╳┃━┏┓┗┛┣┫┳┻╋",
    "Circle progression": " ◐◑◒◓◔◕◖◗◦◌◍◎●◯",
    "Unique Unicode shapes": " ᗧᗢᗣᗤᗨᗩᗪᗫ",
    "Mixed block types": " ░▒▓▚▞▀▄█",

    "Custom": lambda: input("Characters (min 2): ")
}


def select_charset() -> tuple[str, str]:
        
        predefined = {k: v for k,v in CHARSETS.items() if k != "Custom"}
        names = list(CHARSETS.keys())
        options = []
        for n in names:
            cs = CHARSETS[n]
            
            if callable(cs) and n == "Custom": 
                preview = "[digite custom]"     
            else:
                preview = cs[:14] + ("…" if len(cs) > 14 else "")
            # ================================
            options.append(f"{n:<13} │ {preview}")
        idx = arrow_menu("⟁  Pick your charset (↑/↓ + Enter)", options)
        if idx == len(names) - 1:  # Custom
            name = "Custom"
            charset = CHARSETS[name]()
        else:
            name = names[idx]
            charset = predefined[name]
        
        print()
        print(box(f"Charset: {name}\nGlyphs : {charset}", color=(180, 0, 255)))
        return name, charset


def options_list():
    ter.print_centralizedText(logo)
    ter.print_centralizedText(ter.Colors.YELLOW + menu + ter.Colors.RESET)
    

def center_ascii_frame(ascii_text, terminal_width=None):

    if terminal_width is None:
        terminal_width = shutil.get_terminal_size().columns
    
    lines = [line.rstrip() for line in ascii_text.splitlines()]
    if not lines:
        return ascii_text
    
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    stripped_lines = [ansi_escape.sub('', line) for line in lines]
    
    frame_width = max(len(line) for line in stripped_lines)
    
    if frame_width >= terminal_width:
        return ascii_text

    terminal_height = shutil.get_terminal_size().lines
    frame_height = len(lines)

    top_margin = max(0, (terminal_height - frame_height) // 2)

    vertical_padding = [""] * top_margin
    left_margin = (terminal_width - frame_width) // 2
    
    centered_lines = [(" " * left_margin) + line for line in lines]
    return "\n".join(vertical_padding + centered_lines)

# def center_ascii_frame(text: str) -> str:
#            lines = text.splitlines()
#            if not lines:
#                return text
           
#            term_width = shutil.get_terminal_size().columns
#            max_line_len = max(len(line) for line in lines) if lines else 0
           
#            if max_line_len >= term_width:
#                return text  
           
#            padding = " " * ((term_width - max_line_len) // 2)
#            return "\n".join(padding + line for line in lines)
