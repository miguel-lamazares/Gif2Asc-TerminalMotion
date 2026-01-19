package Gif2Asc.Engine.Player;

import java.io.OutputStream;

public class KeyboardListener implements Runnable {
    private final Player player;
    private final PlayerControl control;
    private final OutputStream mpvStdin;

    public KeyboardListener(Player player, PlayerControl control, OutputStream mpvStdin) {
        this.player = player;
        this.control = control;
        this.mpvStdin = mpvStdin;
    }

    @Override
    public void run() {
        try {
            while (player.running) {
                int ch = System.in.read();

                if (ch == '\n' || ch == '\r') {
                    player.stopAll();
                    break;
                }

                if (ch == 27 && System.in.read() == '[') {
                    int code = System.in.read();
                    switch (code) {
                        case 'A' -> control.increaseFps();
                        case 'B' -> control.decreaseFps();
                        case 'C' -> {
                            control.increaseVolume();
                            sendVolume();
                        }
                        case 'D' -> {
                            control.decreaseVolume();
                            sendVolume();
                        }
                    }
                }
            }
        } catch (Exception ignored) {
        }
    }

    private void sendVolume() {
        try {
            if (mpvStdin != null) {
                mpvStdin.write(("set volume " + control.volume + "\n").getBytes());
                mpvStdin.flush();
            }
        } catch (Exception ignored) {
        }
    }

    public static void enableRawMode() {
        try {
            new ProcessBuilder("sh", "-c", "stty -icanon -echo < /dev/tty")
                    .inheritIO()
                    .start();
        } catch (Exception ignored) {
        }
    }
}