package Gif2Asc.Engine.Player;

public class PlayerControl {
    public volatile int fps = 30;
    public volatile int volume = 50;

    public void increaseFps() {
        fps = Math.min(fps + 2, 120);
    }

    public void decreaseFps() {
        fps = Math.max(fps - 2, 5);
    }

    public void increaseVolume() {
        volume = Math.min(volume + 5, 100);
    }

    public void decreaseVolume() {
        volume = Math.max(volume - 5, 0);
    }
}