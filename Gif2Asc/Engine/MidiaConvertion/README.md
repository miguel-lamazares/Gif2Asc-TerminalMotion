# MidiaConvertion 🎞️ → 🅰️

> The Python half of the engine. It eats GIFs and spits out `.asc` frames that
> the Java `Player` and the C `Render` consume to make terminals do things they
> were never designed to do.

If you're looking for a "professional ASCII art toolkit" — wrong repo. This one
just works on the second try.

---

## What it does

```
  GIF / MP4 / URL
        │
        ▼
   FrameExtractor      ← rips PNGs (+ audio) with ffmpeg
        │
        ▼
   PngTreatment        ← optional: tweak / remove background / mask center
        │
        ▼
   FramesConvertion    ← jp2a wizard → Files/TextFrames/*.asc
        │
        ▼
   Player (Java) / Render (C)
```

Everything lands in `Files/`, neatly sorted, ready for the Player.

---

## Folder tour

```
MidiaConvertion/
├── run.py                          ← the one-command pipeline
├── TerminalLib/                    ← zero-dep ANSI toolkit (spinners, gradients, menus)
├── FramesExtration/
│   └── FrameExtractor.py           ← ffmpeg wrangler (local file or URL)
├── PngTreatment/
│   ├── PNGPersonalizer.py          ← brightness · contrast · sat · scale · invert
│   └── backgroundRemover/
│       ├── removeColor.py          ← knock out a hex color → alpha
│       ├── refineMask.py           ← feather + threshold the alpha
│       ├── keepcenter.py           ← keep middle, drop edges
│       └── Ia-offline.py           ← rembg (offline U²-Net)
├── FramesConvertion/
│   ├── AscConverter.py             ← interactive jp2a wizard (saves a JSON)
│   ├── NoArgsAscConverter.py       ← re-render with the last saved JSON
│   └── Defs/
│       └── Defs.py                 ← 31 curated charsets (single source of truth)
└── Files/
    ├── Downloads/                  ← URL inputs land here
    ├── PngFrames/                  ← extracted / treated PNGs
    ├── TextFrames/                 ← *.asc output for the Player
    ├── Settings/jp2aconfig.json    ← last wizard answers
    └── Song/                       ← extracted audio
```

---

## Quick start

```bash
# system deps (do once)
sudo apt install ffmpeg jp2a

# python deps (only if you'll use treatments / AI bg removal)
python -m pip install Pillow            # PngTreatment
python -m pip install rembg onnxruntime # backgroundRemover/Ia-offline.py

# run the whole show
python run.py
```

`run.py` walks you through the three stages with arrow-key menus:

1. **Extract** — *"Extract frames now?"* → drop a path or URL, get PNGs.
2. **Treat** — *"Want to tweak the PNG frames before converting?"* → pick as
   many treatments as you want, in any order.
3. **Convert** — either re-use the last `jp2aconfig.json` (♻) or run the wizard
   from scratch (⟢).

Prefer running scripts solo? Each one stands on its own:

```bash
python FramesExtration/FrameExtractor.py
python PngTreatment/PNGPersonalizer.py
python PngTreatment/backgroundRemover/Ia-offline.py
python FramesConvertion/AscConverter.py
python FramesConvertion/NoArgsAscConverter.py
```

---

## TerminalLib

Tiny ANSI toolkit used by every script. No `rich`, no `curses`, no excuses.

- `Spinner` — braille spinner with live label updates
- `arrow_menu(title, options)` — ↑/↓ + Enter selection
- `confirm(question)` — Yes/No arrow menu
- `gradient(text)` / `gradient_block(text)` — color ramps
- `glitch(text)` — for when things go wrong stylishly
- `progress(curr, total, label)` — minimal progress bar
- `box(text)` — rounded-corner panels
- `typewriter(text)` — slow-type effect

It also exposes `ROOT.png_dir()`, `text_dir()`, `settings_dir()`, etc., so every
script writes to the same `Files/` regardless of where it's launched from.

---

## Charsets

`FramesConvertion/Defs/Defs.py` ships **31** curated charsets — from a clean
`" .:-=+*#%@"` to full Katakana — selectable with a live arrow menu and a
preview of the actual glyphs.

Edit the `CHARSETS` dict to add your own. They're just strings.

---

## Output format

`Files/TextFrames/000000000.asc` … `Files/TextFrames/000000071.asc`

Plain UTF-8 text frames, zero-padded to 9 digits, ordered. The Java/C player
just walks the directory in order. No metadata, no headers, no nonsense.

---

## Troubleshooting

- **`✗ jp2a not found in PATH`** → install it (`sudo apt install jp2a`).
- **`✗ ffmpeg not in PATH`** → same energy.
- **Arrow menu doesn't react** → you're piping into the script. Run it in a real TTY.
- **`Ia-offline` is slow on the first run** → it's downloading the U²-Net model. Coffee time.

---

## Credits

Built on the shoulders of `ffmpeg`, `jp2a`, `Pillow`, and a stubborn refusal to
use a GUI.
