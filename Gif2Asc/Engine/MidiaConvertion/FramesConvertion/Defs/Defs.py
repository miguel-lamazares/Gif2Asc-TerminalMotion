"""
Curated jp2a charsets — Single Source of Truth.
31 sets, ordered from minimalist → maximalist.
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "TerminalLib"))
from TerminalLib.Terminal import arrow_menu, gradient, rgb, RESET, box

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
}

def select_charset() -> tuple[str, str]:
    names = list(CHARSETS.keys())
    options = []
    for n in names:
        cs = CHARSETS[n]
        preview = cs[:14] + ("…" if len(cs) > 14 else "")
        options.append(f"{n:<13} │ {preview}")
    idx = arrow_menu("⟁  Pick your charset (↑/↓ + Enter)", options)
    name = names[idx]
    print()
    print(box(f"Charset: {name}\nGlyphs : {CHARSETS[name]}", color=(180, 0, 255)))
    return name, CHARSETS[name]
