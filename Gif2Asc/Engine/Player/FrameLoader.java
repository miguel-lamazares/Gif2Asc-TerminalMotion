package Gif2Asc.Engine.Player;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class FrameLoader {
    public static List<Path> loadFrames(String dir) throws Exception {
        return Files.list(Paths.get(dir))
                .filter(p -> p.toString().endsWith(".asc"))
                .sorted()
                .collect(Collectors.toList());
    }
}