import sys 
import time
import random
import math
import shutil

from termforge.core import RGB, Style, Cursor, Clear_all, get_terminal_width

def typewrite(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  

def gradient_text(text, start_rgb=(255, 0, 128), end_rgb=(0, 200, 255)):
    """Render text with a smooth RGB gradient between two colors."""
    out = ""
    n = max(len(text) - 1, 1)
    for i, ch in enumerate(text):
        t = i / n
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * t)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * t)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * t)
        out += f"{RGB.fg(r, g, b)}{ch}"
    return out + Style.RESET


def rainbow_text(text):
    """Classic rainbow text using HSV → RGB."""
    out = ""
    for i, ch in enumerate(text):
        h = (i / max(len(text), 1)) * 360
        r, g, b = _hsv_to_rgb(h, 1, 1)
        out += f"{RGB.fg(r, g, b)}{ch}"
    return out + Style.RESET


def _hsv_to_rgb(h, s, v):
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c
    if   0 <= h < 60:   r, g, b = c, x, 0
    elif 60 <= h < 120: r, g, b = x, c, 0
    elif 120 <= h < 180:r, g, b = 0, c, x
    elif 180 <= h < 240:r, g, b = 0, x, c
    elif 240 <= h < 300:r, g, b = x, 0, c
    else:               r, g, b = c, 0, x
    return int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)

def glitch(text, duration=1.5, intensity=0.3):
    """Glitch effect — randomly swaps characters before settling on the real text."""
    glitch_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
    end = time.time() + duration
    Cursor.hide()
    while time.time() < end:
        out = "".join(random.choice(glitch_chars) if random.random() < intensity else c for c in text)
        sys.stdout.write("\r" + RGB.fg(0, 255, 120) + out + Style.RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\r" + text + " " * 4 + "\n")
    Cursor.show()


def shake(text, duration=1.0):
    """Horizontal shake effect."""
    end = time.time() + duration
    Cursor.hide()
    while time.time() < end:
        offset = random.randint(0, 4)
        sys.stdout.write("\r" + " " * offset + text + " " * (4 - offset))
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write("\r" + text + "    \n")
    Cursor.show()


def wave(text, cycles=2, speed=0.05):
    """Sine-wave coloring effect that animates across the text."""
    Cursor.hide()
    for frame in range(int(cycles * 30)):
        out = ""
        for i, ch in enumerate(text):
            phase = (i + frame) * 0.3
            r = int(127 + 127 * math.sin(phase))
            g = int(127 + 127 * math.sin(phase + 2))
            b = int(127 + 127 * math.sin(phase + 4))
            out += f"{RGB.fg(r, g, b)}{ch}"
        sys.stdout.write("\r" + out + Style.RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print()
    Cursor.show()


def fade_in(text, speed=0.04):
    """Fade text in character by character with brightness ramp."""
    Cursor.hide()
    for i in range(1, len(text) + 1):
        sys.stdout.write("\r" + text[:i])
        sys.stdout.flush()
        time.sleep(speed)
    print()
    Cursor.show()


def matrix_rain(duration=3.0, width=None, density=0.02):
    """Cinematic Matrix-style falling characters."""
    if width is None:
        width = get_terminal_width()
    height = shutil.get_terminal_size().lines - 2
    drops = [0] * width
    chars = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄ01"
    Cursor.hide()
    Clear_all()
    end = time.time() + duration
    try:
        while time.time() < end:
            for i in range(width):
                if random.random() < density or drops[i] > 0:
                    drops[i] = (drops[i] + 1) % height
                    Cursor.goto(drops[i] + 1, i + 1)
                    sys.stdout.write(RGB.fg(0, 255, 80) + random.choice(chars))
                    Cursor.goto(max(drops[i] - 4, 1), i + 1)
                    sys.stdout.write(" ")
            sys.stdout.flush()
            time.sleep(0.05)
    finally:
        sys.stdout.write(Style.RESET)
        Cursor.show()
        Clear_all()


def blend_text(text, colors):
    """
    Render text blending through multiple RGB colors.

    Example:
        print(blend_text("TerminalLib", [(255, 0, 0), (0, 255, 0), (0, 0, 255)]))

    Also accepts hex:
        print(blend_text("TerminalLib", ["#ff0000", "#00ff00", "#0000ff"]))
    """

    if not text:
        return ""

    if not colors or len(colors) < 2:
        raise ValueError("colors must contain at least two colors")

    PRESET_COLORS = {
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "blue": (0, 0, 255),
    "purple": (180, 0, 255),
    "cyan": (0, 255, 255),
    "white": (255, 255, 255),
}

    def normalize_color(c):
        # HEX
        if isinstance(c, str) and c.startswith("#"):
            h = c.lstrip("#")
            return (
                int(h[0:2], 16),
                int(h[2:4], 16),
                int(h[4:6], 16),
            )

        # PRESET (string tipo "red")
        if isinstance(c, str):
            if c.lower() in PRESET_COLORS:
                return PRESET_COLORS[c.lower()]
            raise ValueError(f"Unknown color preset: {c}")

        # RGB tuple
        if isinstance(c, tuple) and len(c) == 3:
            return c

        raise ValueError(f"Invalid color: {c}")

    colors = [normalize_color(c) for c in colors]

    out = ""
    n = max(len(text) - 1, 1)
    segments = len(colors) - 1

    for i, ch in enumerate(text):
        t = i / n
        segment = min(int(t * segments), segments - 1)
        local_t = (t * segments) - segment

        c1 = colors[segment]
        c2 = colors[segment + 1]

        r = int(c1[0] + (c2[0] - c1[0]) * local_t)
        g = int(c1[1] + (c2[1] - c1[1]) * local_t)
        b = int(c1[2] + (c2[2] - c1[2]) * local_t)

        out += f"{RGB.fg(r, g, b)}{ch}"

    return out + Style.RESET