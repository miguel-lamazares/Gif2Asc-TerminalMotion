package Gif.Loop;

import Gif.Loop.cave.AscFrames.*;;

public class gif {

    public static void animatePingPong(String[] frames, long delay) {
        int index = 0;
        int direction = 1;

        while (true) {

            System.out.print("\033[H\033[2J");
            System.out.flush();

            System.out.println(frames[index]);

            try {
                Thread.sleep(delay);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }

            index += direction;

            if (index >= frames.length - 1) {
                index = frames.length - 1;
                direction = -1;
            }

            if (index <= 0) {
                index = 0;
                direction = 1;
            }
        }
    }

    public static void main(String[] args) {
        String[] frames = aray.frames;

        animatePingPong(frames, 120);
    }

}
