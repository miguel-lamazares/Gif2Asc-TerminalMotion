import sys

class Cursor:
    HIDE      = "\033[?25l"
    SHOW      = "\033[?25h"
    SAVE      = "\033[s"
    RESTORE   = "\033[u"

    @staticmethod
    def up(n=1):    sys.stdout.write(f"\033[{n}A"); sys.stdout.flush()
    @staticmethod
    def down(n=1):  sys.stdout.write(f"\033[{n}B"); sys.stdout.flush()
    @staticmethod
    def right(n=1): sys.stdout.write(f"\033[{n}C"); sys.stdout.flush()
    @staticmethod
    def left(n=1):  sys.stdout.write(f"\033[{n}D"); sys.stdout.flush()
    @staticmethod
    def goto(row, col): sys.stdout.write(f"\033[{row};{col}H"); sys.stdout.flush()
    @staticmethod
    def clear_line(): sys.stdout.write("\033[2K\r"); sys.stdout.flush()
    @staticmethod
    def hide():     sys.stdout.write(Cursor.HIDE); sys.stdout.flush()
    @staticmethod
    def show():     sys.stdout.write(Cursor.SHOW); sys.stdout.flush()

