import sys

from termforge.core import RGB, Style, Cursor


def menu(title, options, color=None):
    """Render an interactive menu navigated with ↑/↓ + Enter."""
    color = color or RGB.fg(0, 220, 255)
    selected = 0

    def _getch():
        try:
            import termios, tty
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
                if ch == "\x1b":
                    ch += sys.stdin.read(2)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
            return ch
        except Exception:
            import msvcrt
            ch = msvcrt.getch()
            if ch in (b"\x00", b"\xe0"):
                ch += msvcrt.getch()
            return ch.decode("utf-8", errors="ignore")

    Cursor.hide()
    try:
        while True:
            sys.stdout.write("\r")
            print(f"{Style.BOLD}{color}{title}{Style.RESET}")
            for i, opt in enumerate(options):
                marker = "❯" if i == selected else " "
                line = f" {marker} {opt}"
                if i == selected:
                    line = f"{color}{Style.BOLD}{line}{Style.RESET}"
                print(line)
            key = _getch()
            if key in ("\x1b[A", "\x00H", "\xe0H"):  # up
                selected = (selected - 1) % len(options)
            elif key in ("\x1b[B", "\x00P", "\xe0P"):  # down
                selected = (selected + 1) % len(options)
            elif key in ("\r", "\n"):
                return selected
            # rewind
            Cursor.up(len(options) + 1)
            for _ in range(len(options) + 1):
                Cursor.clear_line()
                Cursor.down(1)
            Cursor.up(len(options) + 1)
    finally:
        Cursor.show()
