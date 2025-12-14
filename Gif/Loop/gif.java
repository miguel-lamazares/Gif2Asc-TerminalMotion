package Gif.Loop;

import java.io.OutputStream;
import java.nio.charset.StandardCharsets;

import Gif.AscFrames.*;

public class gif {

    private Process renderer;
    private OutputStream rendererIn;

    public void startRenderer() throws Exception {
        renderer = new ProcessBuilder("Gif/Render/Render")
                .redirectOutput(ProcessBuilder.Redirect.INHERIT)
                .start();
        rendererIn = renderer.getOutputStream();
    }

    public void animate(String[] frames, long delay) throws Exception {

        int index = frames.length - 1;

        while (true) {

            rendererIn.write(frames[index].getBytes(StandardCharsets.UTF_8));
            rendererIn.flush();

            Thread.sleep(delay);

            index++;
            if (index >= frames.length) {
                index = 0;
            }
        }
    }

    public static void main(String[] args) throws Exception {

        String[] frames = aray.frames;

        gif player = new gif();

        player.startRenderer();

        System.out.print("\033[H\033[2J");
        System.out.flush();

        player.animate(frames, 142);
    }
}
