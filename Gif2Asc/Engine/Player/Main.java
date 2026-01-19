package Gif2Asc.Engine.Player;

import java.io.OutputStream;
import java.nio.file.Path;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        KeyboardListener.enableRawMode();

        Player player = new Player();
        PlayerControl control = new PlayerControl();

        player.startRenderer();
        player.songPlayer();

        OutputStream mpvStdin = null;
        if (player.audioProcess != null) {
            mpvStdin = player.audioProcess.getOutputStream();
        }

        Thread keyboard = new Thread(
                new KeyboardListener(player, control, mpvStdin),
                "keyboard-listener");
        keyboard.setDaemon(true);
        keyboard.start();

        System.out.print("\033[H\033[2J\033[?25l");
        System.out.flush();

        
        List<Path> frames = FrameLoader.loadFrames("Gif2Asc/Engine/MidiaConvertion/Files/TextFrames");

        player.animate(frames, control);

        System.out.print("\033[0m\033[?25h");
        System.exit(0);
    }
}