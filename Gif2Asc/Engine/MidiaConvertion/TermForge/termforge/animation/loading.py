import sys

def print_progress_bar(current, total, bar_length=20):

    progress = current / total
    filled_length = int(bar_length * progress)
    bar = '∎' * filled_length + '.' * (bar_length - filled_length)
    por = current / total * 100;
    sys.stdout.write(f'\r[{bar}] {por:.2f}% {current}/{total} :) ')
    sys.stdout.flush()
    if current == total:
        print()
