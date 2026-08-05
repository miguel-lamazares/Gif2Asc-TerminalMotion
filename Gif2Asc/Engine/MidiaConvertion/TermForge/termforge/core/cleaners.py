def Clear_all():
    print("\033[H\033[2J", flush=True)


def wait_enter_clear(prompt="\n\nPress Enter..."):
    input(prompt)
    print("\033[F\033[K", end="")