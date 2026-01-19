package Gif2Asc.Engine.Player;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class SongLoader {
    public static List<Path> loadSongs(String dir) throws Exception {
        Path songDir = Paths.get(dir);
        if (!Files.exists(songDir))
            return List.of();

        return Files.list(songDir)
                .filter(p -> p.toString().matches(".*\\.(mp3|wav|ogg|flac|aac)$"))
                .sorted()
                .collect(Collectors.toList());
    }
}