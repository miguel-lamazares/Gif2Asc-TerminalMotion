#include <unistd.h>
#include <stdio.h>

int main() {
    char buffer[1 << 16];
    ssize_t n;

    while ((n = read(0, buffer, sizeof(buffer))) > 0) {
        write(1, "\033[2J\033[H", 10);
        write(1, buffer, n);
        fflush(stdout);
    }

    return 0;
}