// why not java?
// 'cause it's an old version of the player, it's a .rs file for doesn't broke the java


package Gif2Asc.Engine.Player;


import java.io.OutputStream;
import java.nio.file.*;
import java.util.List;

public class Player {

    private Process renderer;
    private OutputStream rendererIn;
    private volatile boolean running = true;

    public void startRenderer() throws Exception {
        renderer = new ProcessBuilder("Gif2Asc/Engine/Render/Render")
                .redirectOutput(ProcessBuilder.Redirect.INHERIT)
                .start();
        rendererIn = renderer.getOutputStream();
    }

    public void listenForExit() {
        new Thread(() -> {
            try {
                int r;
                while ((r = System.in.read()) != -1) {
                    if (r == '\n' || r == '\r') {
                        stopSong();
                        break;
                    }
                }
            } catch (Exception ignored) {
            }
        }, "exit-listener").start();
    }

    private void busyWaitUntil(long targetTimeNanos) {
        while (System.nanoTime() < targetTimeNanos) {
            Thread.onSpinWait();
        }
    }

    public void animate(List<Path> frames, long FPS) throws Exception {

        int index = 0;

        long frameTimeNanos = 1_000_000_000L / FPS;
        long nextFrameTime = System.nanoTime();

        while (running) {
            Path frame = frames.get(index);

            byte[] data = Files.readAllBytes(frame);
            rendererIn.write(data);
            rendererIn.flush();

            nextFrameTime += frameTimeNanos;
            busyWaitUntil(nextFrameTime);

            index = (index + 1) % frames.size();
        }
    }

    private static List<Path> loadFrames(String dir) throws Exception {
        return Files.list(Paths.get(dir))
                .filter(p -> p.toString().endsWith(".asc"))
                .sorted()
                .toList();
    }

    private void cleanup() {
        try {
            if (rendererIn != null)
                rendererIn.close();
        } catch (Exception ignored) {
        }

        if (renderer != null)
            renderer.destroy();

        System.out.print("\033[0m\033[?25h");
        System.out.flush();
    }

    private volatile Process audioProcess;

    private static List<Path> loadSongs(String dir) throws Exception {
        Path songDir = Paths.get(dir);
        if (!Files.exists(songDir) || !Files.isDirectory(songDir))
            return List.of();
        return Files.list(songDir)
                .filter(p -> {
                    String s = p.toString().toLowerCase();
                    return s.endsWith(".wav") || s.endsWith(".mp3") || s.endsWith(".ogg") || s.endsWith(".flac")
                            || s.endsWith(".aac");
                })
                .sorted()
                .toList();
    }

    private void songPlayer() {
        try {
            List<Path> songs = loadSongs("Gif2Asc/Engine/MidiaConvertion/Files/Song");
            if (songs.isEmpty()) {
                System.err.println(
                        "Nenhuma música encontrada em Gif2Asc/Engine/MidiaConvertion/Files/Song — pulando reprodução.");
                return;
            }
            Path song = songs.get(0);
            audioProcess = new ProcessBuilder(
                    "mpv",
                    "--no-video",
                    song.toAbsolutePath().toString())
                    .redirectOutput(ProcessBuilder.Redirect.INHERIT)
                    .redirectError(ProcessBuilder.Redirect.INHERIT)
                    .start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private synchronized void stopSong() {
        if (audioProcess != null && audioProcess.isAlive()) {
            audioProcess.destroy();
        }
        running = false;
    }

    


    public static void main(String[] args) throws Exception {

        boolean exitOnEnter = true;
        long FPS = 30;

        Player player = new Player();
        player.startRenderer();

        if (exitOnEnter) {
            player.listenForExit();
        }

        System.out.print("\033[H\033[2J\033[?25l");
        System.out.flush();

        List<Path> frames = loadFrames("Gif2Asc/Engine/MidiaConvertion/Files/TextFrames");

        player.songPlayer();
        player.animate(frames, FPS);

        player.cleanup();
        player.stopSong();
        System.exit(0);
    }
}
