#!/usr/bin/env bash
set -e

ROOT="$(cd "$(dirname "$0")" && pwd)"

# -----------------------------
# Activate virtualenv
# -----------------------------
if [ ! -d "$ROOT/.venv" ]; then
    echo "[!] Virtualenv not found. Run ./setup_env.sh first."
    exit 1
fi

. "$ROOT/.venv/bin/activate"

# -----------------------------
# Python steps
# -----------------------------

PYTHON="$ROOT/.venv/bin/python"

"$PYTHON" "$ROOT/Gif/Gif_to_asc/Gif-to-png/8.py"
"$PYTHON" "$ROOT/Gif/Gif_to_asc/png-to-asc/JP2a.py"


# -----------------------------
# C build
# -----------------------------
echo "[*] Compiling C renderer"
gcc "$ROOT/Gif/Render/Render.c" -O3 -o "$ROOT/Gif/Render/Render"

# -----------------------------
# Java build
# -----------------------------
echo "[*] Compiling Java"
javac "$ROOT/Gif/AscFrames/"*.java
javac "$ROOT/Gif/Loop/gif.java"

# -----------------------------
# Run animation
# -----------------------------
echo "[▶] Running animation"
java Gif.Loop.gif

