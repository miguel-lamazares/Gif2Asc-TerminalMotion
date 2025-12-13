package Gif.Loop;

import Gif.Loop.cave.AscFrames.*;;

public class gif {

    public static void animatePingPong(String[] frames, long delay) {

        
        int index = frames.length - 1; 

        while (true) {

            System.out.print("\033[H");
            System.out.flush();

            System.out.println(frames[index]);

            try {
                Thread.sleep(delay);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }

            index++;

            if (index >= frames.length) {
                index = 0; 
            }
        }

    }

    public static void main(String[] args) {

        String[] frames = aray.frames;

        System.out.print("\033[H\033[2J");
        System.out.flush();
        animatePingPong(frames, 142);

    }

}
