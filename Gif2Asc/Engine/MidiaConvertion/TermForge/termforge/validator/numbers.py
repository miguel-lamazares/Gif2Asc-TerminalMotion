import sys

def onlyNumbers() -> int:
    while True:
        user_input = input()

        if not user_input.strip().isdigit():
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            continue

        choice = int(user_input)

        return choice
        
def numbersBetween(Min_value: int, max_value: int) -> int:
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