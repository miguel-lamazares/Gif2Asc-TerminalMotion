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

"$PYTHON" "$ROOT/Gif/Gif_to_asc/Gif-to-png/FrameExatractor.py"
"$PYTHON" "$ROOT/Gif/Gif_to_asc/png-to-asc/AscConverter.py"


# -----------------------------
# C build
# -----------------------------
gcc "$ROOT/Gif/Render/Render.c" -O3 -o "$ROOT/Gif/Render/Render"

# -----------------------------
# Java build
# -----------------------------
javac "$ROOT/Gif/Player/Player.java"

# -----------------------------
# Run animation
# -----------------------------
java Gif.Player.Player

