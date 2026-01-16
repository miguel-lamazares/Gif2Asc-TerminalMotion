package Gif2Asc.Engine.Player;

import java.io.OutputStream;
import java.nio.file.*;
import java.util.List;

public class Player {

    private Process renderer;
    private OutputStream rendererIn;
    volatile boolean running = true;
    volatile Process audioProcess;

    /*
     * =========================
     * RENDER
     * =========================
     */

    public void startRenderer() throws Exception {
        renderer = new ProcessBuilder("Gif2Asc/Engine/Render/Render")
                .redirectOutput(ProcessBuilder.Redirect.INHERIT)
                .start();
        rendererIn = renderer.getOutputStream();
    }

    /*
     * =========================
     * ANIMATION LOOP
     * =========================
     */

    public void animate(List<Path> frames, PlayerControl control) throws Exception {
        int index = 0;

        while (running) {
            long frameTimeNanos = 1_000_000_000L / control.fps;
            long start = System.nanoTime();

            Path frame = frames.get(index);
            byte[] data = Files.readAllBytes(frame);
            rendererIn.write(data);
            rendererIn.flush();

            index = (index + 1) % frames.size();

            long elapsed = System.nanoTime() - start;
            long sleep = frameTimeNanos - elapsed;

            if (sleep > 0) {
                busyWaitUntil(System.nanoTime() + sleep);
            }
        }
    }

    private void busyWaitUntil(long targetTimeNanos) {
        while (System.nanoTime() < targetTimeNanos) {
            Thread.onSpinWait();
        }
    }

    /*
     * =========================
     * AUDIO
     * =========================
     */

    private static List<Path> loadSongs(String dir) throws Exception {
        Path songDir = Paths.get(dir);
        if (!Files.exists(songDir))
            return List.of();

        return Files.list(songDir)
                .filter(p -> p.toString().matches(".*\\.(mp3|wav|ogg|flac|aac)$"))
                .sorted()
                .toList();
    }

    public void songPlayer() {
        try {
            List<Path> songs = loadSongs("Gif2Asc/Engine/MidiaConvertion/Files/Song");
            if (songs.isEmpty()) {
                System.err.println("Nenhuma música encontrada — seguindo sem áudio.");
                return;
            }

            audioProcess = new ProcessBuilder(
                    "mpv",
                    "--input-terminal=yes",
                    "--no-video",
                    songs.get(0).toAbsolutePath().toString()).inheritIO().start();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    synchronized void stopAll() {
        running = false;
        if (audioProcess != null && audioProcess.isAlive()) {
            audioProcess.destroy();
        }
    }

    /*
     * =========================
     * FRAMES
     * =========================
     */

    private static List<Path> loadFrames(String dir) throws Exception {
        return Files.list(Paths.get(dir))
                .filter(p -> p.toString().endsWith(".asc"))
                .sorted()
                .toList();
    }

    /*
     * =========================
     * CONTROL
     * =========================
     */

    public static class PlayerControl {
        public volatile int fps = 30;
        public volatile int volume = 50;

        void increaseFps() {
            fps = Math.min(fps + 2, 120);
        }

        void decreaseFps() {
            fps = Math.max(fps - 2, 5);
        }

        void increaseVolume() {
            volume = Math.min(volume + 5, 100);
        }

        void decreaseVolume() {
            volume = Math.max(volume - 5, 0);
        }
    }

    /*
     * =========================
     * KEYBOARD
     * =========================
     */

    public static class KeyboardListener implements Runnable {

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

                    // ENTER encerra tudo
                    if (ch == '\n' || ch == '\r') {
                        player.stopAll();
                        break;
                    }

                    // Setas do teclado
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
                // silêncio absoluto, como todo bom bug em produção
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

        /*
         * =========================
         * TERMINAL
         * =========================
         */

        private static void enableRawMode() {
            try {
                new ProcessBuilder("sh", "-c", "stty -icanon -echo < /dev/tty")
                        .inheritIO()
                        .start();
            } catch (Exception ignored) {
            }
        }

        /*
         * =========================
         * MAIN
         * =========================
         */

        public static void main(String[] args) throws Exception {

            enableRawMode();

            Player player = new Player();
            PlayerControl control = new PlayerControl();

            player.startRenderer();
            player.songPlayer();

            OutputStream mpvStdin = null;
            if (player.audioProcess != null) {
                mpvStdin = player.audioProcess.getOutputStream();
            }

            Thread keyboard = new Thread(
                    new KeyboardListener(player, control, mpvStdin),
                    "keyboard-listener");
            keyboard.setDaemon(true);
            keyboard.start();

            System.out.print("\033[H\033[2J\033[?25l");
            System.out.flush();

            List<Path> frames = loadFrames("Gif2Asc/Engine/MidiaConvertion/Files/TextFrames");

            player.animate(frames, control);

            System.out.print("\033[0m\033[?25h");
            System.exit(0);
        }
    }
}
