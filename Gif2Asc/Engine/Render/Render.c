#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main() {
    char buffer[1 << 16];
    ssize_t n;

    const char *clear = "\033[2J\033[H";
    const char *reset = "\033[0m";

    while ((n = read(0, buffer, sizeof(buffer))) > 0) {
        write(1, clear, strlen(clear));
        write(1, reset, strlen(reset));
        write(1, buffer, n);
        fflush(stdout);
    }

    return 0;
}
