import sys
import time
import os
import requests
import shutil
import re

#
# CLEAR TERMINAL
#

def Clear_all():
    print("\033[H\033[2J", flush=True)

#
# WAIT ENTER AND CLEAR
#

def wait_enter_clear(prompt="\n\nPress Enter..."):
    input(prompt)
    print("\033[F\033[K", end="")

#
# COLORS
#

class Colors():
    RESET = "\u001B[0m";
    BLACK = "\u001B[30m";
    RED = "\u001B[31m";
    GREEN = "\u001B[32m";
    YELLOW = "\u001B[33m";
    BLUE = "\u001B[34m";
    PURPLE = "\u001B[35m";
    CYAN = "\u001B[36m";
    WHITE = "\u001B[37m";

#
# READ RESPONSE FROM USER
# 

def read_int(Min_value: int,max_value: int) -> int:
    while True:
        user_input = input()

        if not user_input.strip().isdigit():
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            continue

        choice = int(user_input)

        if choice <= Min_value - 1:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            continue

        if choice >= max_value + 1:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            continue

        return choice
    

#    
# TYPEWRITE
#
     
def typewrite(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  


# 
# BAR
#

def print_progress_bar(current, total, bar_length=20):

    progress = current / total
    filled_length = int(bar_length * progress)
    bar = '∎' * filled_length + '.' * (bar_length - filled_length)
    por = current / total * 100;
    sys.stdout.write(f'\r[{bar}] {por}% {current}/{total}')
    sys.stdout.flush()
    if current == total:
        print()

#
# PRINT CENTRALIZED TEXT
#

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

        