package Gif.Static;

import Gif.AscFrames.*;

public class vid {
    public static void animate(String[] frames, long delay) {
        for (String frame : frames) {
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println(frame);
            try {
                Thread.sleep(delay);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }

    public static void main(String[] args) {

        String[] frames = aray.frames;

        animate(frames, 120);

    }
}
