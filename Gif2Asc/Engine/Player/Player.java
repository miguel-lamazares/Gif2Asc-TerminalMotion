package Gif2Asc.Engine.Player;

import java.io.OutputStream;
import java.nio.file.Path;
import java.util.List;

public class Player {
    private Process renderer;
    private OutputStream rendererIn;
    volatile boolean running = true;
    volatile Process audioProcess;

    public void startRenderer() throws Exception {
        renderer = new ProcessBuilder("Gif2Asc/Engine/Render/Render")
                .redirectOutput(ProcessBuilder.Redirect.INHERIT)
                .start();
        rendererIn = renderer.getOutputStream();
    }

    public void animate(List<Path> frames, PlayerControl control) throws Exception {
        int index = 0;

        while (running) {
            long frameTimeNanos = 1_000_000_000L / control.fps;
            long start = System.nanoTime();

            Path frame = frames.get(index);
            byte[] data = java.nio.file.Files.readAllBytes(frame);
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

    public void songPlayer() {
        try {
            List<Path> songs = SongLoader.loadSongs("Gif2Asc/Engine/MidiaConvertion/Files/Song");
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

    public synchronized void stopAll() {
        running = false;
        if (audioProcess != null && audioProcess.isAlive()) {
            audioProcess.destroy();
        }
    }
}