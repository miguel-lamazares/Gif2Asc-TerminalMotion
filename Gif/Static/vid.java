package Gif.Static;

import Gif.Static.asc.Frames.*;

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
        
        String[] frames = {
                frame.A,
                frame.b,
                frame.c,
                frame.d,
                frame.e,
                frame.f,
                frame.g,
                frame.h,
                frame.i,
                frame.j,
                frame.k
        };

        animate(frames, 120);

    }
}
