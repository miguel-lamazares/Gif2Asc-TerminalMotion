import sys
import time

def Clear_all():
    print("\033[H\033[2J", flush=True)

def wait_enter_clear(prompt="\n\nPress Enter..."):
    input(prompt)
    print("\033[F\033[K", end="")

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


def read_int(max_value: int) -> int:
    while True:
        user_input = input()

        if not user_input.strip().isdigit():
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            continue

        choice = int(user_input)

        if choice >= max_value:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            continue

        return choice
    
    
def typewrite(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  