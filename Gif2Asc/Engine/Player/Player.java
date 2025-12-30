package Gif2Asc.Engine.Player;

import java.io.OutputStream;
import java.nio.file.*;
import java.util.List;

public class Player {

    private Process renderer;
    private OutputStream rendererIn;
    private volatile boolean running = true;

    public void startRenderer() throws Exception {
        renderer = new ProcessBuilder("/home/dex/Documentos/GitHub/Inutil-things-for-JAVA/Gif2Asc/Engine/Render/Render")
                .redirectOutput(ProcessBuilder.Redirect.INHERIT)
                .start();
        rendererIn = renderer.getOutputStream();
    }

    public void listenForExit() {
        new Thread(() -> {
            try {
                System.in.read();
                running = false;
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

    public static void main(String[] args) throws Exception {

        boolean exitOnEnter = true;
        long FPS = 3;

        Player player = new Player();
        player.startRenderer();

        if (exitOnEnter) {
            player.listenForExit();
        }

        System.out.print("\033[H\033[2J\033[?25l");
        System.out.flush();

        List<Path> frames = loadFrames("/home/dex/Documentos/GitHub/Inutil-things-for-JAVA/Gif2Asc/Engine/TextFrames/");

        player.animate(frames, FPS);

        player.cleanup();
        System.exit(0);
    }
}
