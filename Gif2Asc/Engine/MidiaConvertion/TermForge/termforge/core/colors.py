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

class RGB:
    @staticmethod
    def fg(r, g, b):  return f"\033[38;2;{r};{g};{b}m"
    @staticmethod
    def bg(r, g, b):  return f"\033[48;2;{r};{g};{b}m"
    @staticmethod
    def fg256(n):     return f"\033[38;5;{n}m"
    @staticmethod
    def bg256(n):     return f"\033[48;5;{n}m"

    @staticmethod
    def hex(hex_str):
        h = hex_str.lstrip('#')
        return RGB.fg(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
