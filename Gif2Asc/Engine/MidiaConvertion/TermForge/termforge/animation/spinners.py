import sys
import time
import threading
import itertools

from termforge.core import RGB, Style, Cursor, Clear_all

SPINNER_FRAMES = {
    "dots":     ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
    "line":     ["-", "\\", "|", "/"],
    "arrows":   ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"],
    "moon":     ["🌑","🌒","🌓","🌔","🌕","🌖","🌗","🌘"],
    "bouncing": ["[    ]","[=   ]","[==  ]","[=== ]","[ ===]","[  ==]","[   =]","[    ]"],
    "pulse":    ["•", "●", "◉", "●", "•"],
}


class Spinner:
    def __init__(self, message="Loading", style="dots", color=None):
        self.frames = SPINNER_FRAMES.get(style, SPINNER_FRAMES["dots"])
        self.message = message
        self.color = color or RGB.fg(0, 200, 255)
        self._stop = threading.Event()
        self._thread = None

    def _run(self):
        Cursor.hide()
        for frame in itertools.cycle(self.frames):
            if self._stop.is_set():
                break
            sys.stdout.write(f"\r{self.color}{frame}{Style.RESET} {self.message}")
            sys.stdout.flush()
            time.sleep(0.08)
        Cursor.clear_line()
        Cursor.show()

    def start(self):
        self._stop.clear()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()
        return self

    def stop(self, final_message=None):
        self._stop.set()
        if self._thread:
            self._thread.join()
        if final_message:
            print(final_message)

    def __enter__(self): return self.start()
    def __exit__(self, *a): self.stop()
