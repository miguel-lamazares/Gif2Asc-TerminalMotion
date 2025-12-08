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
        String[] frames = {
                art.frame0,
                art.frame1,
                art.frame2,
                art.frame3,
                art.frame4,
                art.frame5,
                art.frame6,
                art.frame7,
                art.frame8,
                art.frame9,
                art.frame10,
                art.frame11,
                art.frame12,
                art.frame13,
                art.frame14,
                art.frame15,
                art.frame16,
                art.frame17,
                art.frame18,
                art.frame19,
                art.frame20,
                art.frame21,
                art.frame22,
                art.frame23,
                art.frame24,
                art.frame25,
                art.frame26,
                art.frame27,
                art.frame28,
                art.frame29,
                art.frame30,
                art.frame31,
                art.frame32,
                art.frame33,
                art.frame34,
                art.frame35,
                art.frame36,
                art.frame37,
                art.frame38,
                art.frame39,
                art.frame40,
                art.frame41,
                art.frame42,
                art.frame43,
                art.frame44,
                art.frame45,
                art.frame46,
                art.frame47,
                art.frame48,
                art.frame49,
                art.frame50,
                art.frame51,
                art.frame52,
                art.frame53,
                art.frame54,
                art.frame55,
                art.frame56,
                art.frame57,
                art.frame58
        };

        animatePingPong(frames, 180);
    }

}
