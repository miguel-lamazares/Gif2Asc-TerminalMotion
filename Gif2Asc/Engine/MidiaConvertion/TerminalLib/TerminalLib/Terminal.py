"""
TerminalLib v3 — Zero-dep ANSI toolkit
Spinners, gradients, glitches, boxes, arrow menus, progress bars.
"""
from __future__ import annotations
import sys, os, time, threading, shutil, select, tty, termios

# ─── ANSI base ────────────────────────────────────────────────────────────────
ESC   = "\033["
RESET = ESC + "0m"
HIDE  = ESC + "?25l"
SHOW  = ESC + "?25h"
CLR   = ESC + "2J" + ESC + "H"
UP    = lambda n=1: ESC + f"{n}A"
DOWN  = lambda n=1: ESC + f"{n}B"
CLRL  = ESC + "2K"

def rgb(r, g, b, bg=False):
    return f"{ESC}{48 if bg else 38};2;{r};{g};{b}m"

def w(s=""):
    sys.stdout.write(s); sys.stdout.flush()

def hide_cursor(): w(HIDE)
def show_cursor(): w(SHOW)
def clear():       w(CLR)
def term_w():      return shutil.get_terminal_size((80, 24)).columns

# ─── Gradient text ────────────────────────────────────────────────────────────
def gradient(text: str, start=(0, 200, 255), end=(180, 0, 255)) -> str:
    out = []
    n = max(len(text) - 1, 1)
    for i, ch in enumerate(text):
        t = i / n
        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)
        out.append(rgb(r, g, b) + ch)
    return "".join(out) + RESET

def gradient_block(block: str, start=(0,200,255), end=(180,0,255)) -> str:
    lines = block.splitlines()
    n = max(len(lines) - 1, 1)
    out = []
    for i, line in enumerate(lines):
        t = i / n
        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)
        out.append(rgb(r, g, b) + line + RESET)
    return "\n".join(out)

# ─── Typewriter ───────────────────────────────────────────────────────────────
def typewriter(text: str, delay=0.012, color=None):
    if color: w(color)
    for ch in text:
        w(ch); time.sleep(delay)
    if color: w(RESET)
    w("\n")

# ─── Glitch ───────────────────────────────────────────────────────────────────
import random
_GLITCH = "!@#$%&*?/\\|<>=+-_~^"
def glitch(text: str, passes=4, delay=0.04):
    for _ in range(passes):
        scrambled = "".join(random.choice(_GLITCH) if ch != " " else " " for ch in text)
        w("\r" + rgb(255, 60, 80) + scrambled + RESET); time.sleep(delay)
    w("\r" + rgb(255, 80, 100) + text + RESET + "\n")

# ─── Box ──────────────────────────────────────────────────────────────────────
def box(text: str, color=(120, 200, 255), pad=2):
    lines = text.splitlines() or [""]
    width = max(len(l) for l in lines) + pad * 2
    c = rgb(*color)
    top = c + "╭" + "─" * width + "╮" + RESET
    bot = c + "╰" + "─" * width + "╯" + RESET
    body = [c + "│" + RESET + " " * pad + l + " " * (width - pad - len(l)) + c + "│" + RESET for l in lines]
    return "\n".join([top, *body, bot])

# ─── Spinner ──────────────────────────────────────────────────────────────────
class Spinner:
    FRAMES = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    def __init__(self, label="working", color=(0, 220, 255)):
        self.label = label; self.color = color
        self._stop = False; self._thr = None
    def __enter__(self):
        hide_cursor()
        self._thr = threading.Thread(target=self._run, daemon=True); self._thr.start()
        return self
    def __exit__(self, *a):
        self._stop = True
        if self._thr: self._thr.join()
        w("\r" + CLRL); show_cursor()
    def update(self, label): self.label = label
    def _run(self):
        i = 0
        while not self._stop:
            f = self.FRAMES[i % len(self.FRAMES)]
            w("\r" + CLRL + rgb(*self.color) + f + " " + RESET + self.label)
            time.sleep(0.07); i += 1

# ─── Progress bar ─────────────────────────────────────────────────────────────
def progress(curr: int, total: int, label="", width=32, color=(0, 220, 255)):
    pct = curr / max(total, 1)
    filled = int(width * pct)
    bar = rgb(*color) + "█" * filled + RESET + rgb(60, 60, 80) + "░" * (width - filled) + RESET
    w("\r" + CLRL + f"{bar} {int(pct*100):3d}%  {label}")
    if curr >= total: w("\n")

# ─── Arrow menu (TTY) ─────────────────────────────────────────────────────────
def _read_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == "\x1b":
            ch += sys.stdin.read(2)
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

def arrow_menu(title: str, options: list[str], color=(0, 220, 255)) -> int:
    if not sys.stdin.isatty():
        print(title)
        for i, o in enumerate(options): print(f"  {i+1}) {o}")
        while True:
            try:
                v = int(input("> ")) - 1
                if 0 <= v < len(options): return v
            except Exception: pass
    sel = 0
    hide_cursor()
    try:
        first = True
        while True:
            if not first:
                w(UP(len(options) + 2))
            first = False
            w(CLRL + gradient(title) + "\n")
            w(CLRL + "\n")
            for i, opt in enumerate(options):
                if i == sel:
                    w(CLRL + rgb(*color) + " ▸ " + opt + RESET + "\n")
                else:
                    w(CLRL + "   " + rgb(120, 120, 140) + opt + RESET + "\n")
            k = _read_key()
            if k in ("\x1b[A", "k"): sel = (sel - 1) % len(options)
            elif k in ("\x1b[B", "j"): sel = (sel + 1) % len(options)
            elif k in ("\r", "\n"): return sel
            elif k == "\x03": raise KeyboardInterrupt
    finally:
        show_cursor()

# ─── Confirm (yes/no arrow) ───────────────────────────────────────────────────
def confirm(question: str, default_yes=True) -> bool:
    return arrow_menu(question, ["✓ Yes — vai com Deus", "✗ No  — pula essa parte"]) == 0

# ─── Banner helper ────────────────────────────────────────────────────────────
def banner(text: str, sub: str = ""):
    clear()
    print(gradient_block(text))
    if sub:
        print(rgb(140, 140, 160) + sub + RESET)
    print()
