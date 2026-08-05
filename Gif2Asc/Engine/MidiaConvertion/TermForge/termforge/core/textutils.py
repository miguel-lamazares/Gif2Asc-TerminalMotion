import sys
import os
import re

class Style:
    RESET     = "\033[0m"
    BOLD      = "\033[1m"
    DIM       = "\033[2m"
    ITALIC    = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK     = "\033[5m"
    REVERSE   = "\033[7m"
    HIDDEN    = "\033[8m"
    STRIKE    = "\033[9m"


BOX_STYLES = {
    "single":  "┌─┐│└─┘│",
    "double":  "╔═╗║╚═╝║",
    "rounded": "╭─╮│╰─╯│",
    "heavy":   "┏━┓┃┗━┛┃",
    "ascii":   "+-+|+-+|",
}


def box(text, style="rounded", padding=1, color=None):
    """Wrap multiline text in a decorative box."""
    s = BOX_STYLES.get(style, BOX_STYLES["rounded"])
    tl, h, tr, r, bl, _, br, l = s
    lines = text.split("\n")
    width = max(len(strip_ansi_codes(ln)) for ln in lines)
    pad = " " * padding
    color = color or ""
    rst = Style.RESET if color else ""

    top    = f"{color}{tl}{h * (width + padding * 2)}{tr}{rst}"
    bottom = f"{color}{bl}{h * (width + padding * 2)}{br}{rst}"
    body = []
    for ln in lines:
        clean_len = len(strip_ansi_codes(ln))
        body.append(f"{color}{l}{rst}{pad}{ln}{' ' * (width - clean_len)}{pad}{color}{r}{rst}")
    return "\n".join([top, *body, bottom])


def hr(char="─", color=None):
    """Horizontal rule across the terminal."""
    w = get_terminal_width()
    line = char * w
    return f"{color}{line}{Style.RESET}" if color else line

def table(headers, rows, color_header=None):
    """Pretty ASCII table with auto column widths."""
    cols = len(headers)
    widths = [len(str(h)) for h in headers]
    for row in rows:
        for i in range(cols):
            widths[i] = max(widths[i], len(str(row[i])))

    def fmt_row(row):
        return "│ " + " │ ".join(str(row[i]).ljust(widths[i]) for i in range(cols)) + " │"

    sep_top = "┌─" + "─┬─".join("─" * w for w in widths) + "─┐"
    sep_mid = "├─" + "─┼─".join("─" * w for w in widths) + "─┤"
    sep_bot = "└─" + "─┴─".join("─" * w for w in widths) + "─┘"

    header_line = fmt_row(headers)
    if color_header:
        header_line = color_header + header_line + Style.RESET

    return "\n".join([sep_top, header_line, sep_mid, *(fmt_row(r) for r in rows), sep_bot])

def get_terminal_width():
    return os.get_terminal_size().columns

def strip_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B\[[0-9;]*[A-Za-z]')
    return ansi_escape.sub('', text)

def print_centralizedText(text):
    terminal_width = get_terminal_width()
    lines = text.split('\n')
    
    for line in lines:

        clean_line = strip_ansi_codes(line)
        line_length = len(clean_line)

        padding = max(0, (terminal_width - line_length) // 2)
 
        print(' ' * padding + line)

def beep():
    """Terminal bell."""
    sys.stdout.write("\a")
    sys.stdout.flush()