import sys
import time
import os
import requests
import shutil
import re
import random
import math
import threading
import itertools

from termforge.core import (
    RGB,
    Style,
    Cursor,
    Clear_all,
    hr,
    box,
)
from termforge.animation import (
    rainbow_text,
    gradient_text,
    typewrite,
    glitch,
    wave,
    Spinner,
)



def _demo():
    Clear_all()
    print(rainbow_text("✦ TerminalLib · Python · v2 ✦"))
    print(hr("─", RGB.fg(80, 80, 80)))
    print(box("Your terminal\ndoesn't need to be ugly.", style="rounded", color=RGB.fg(0, 220, 255)))
    typewrite(gradient_text("Loading awesome features..."))
    with Spinner("Crunching numbers", style="dots"):
        time.sleep(1.5)
    glitch("SYSTEM ONLINE", duration=1.2)
    wave("~ have fun ~", cycles=2)


if __name__ == "__main__":
    _demo()
