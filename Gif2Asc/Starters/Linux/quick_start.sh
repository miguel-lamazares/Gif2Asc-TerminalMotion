#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

# -----------------------------
# Activate virtualenv
# -----------------------------
if [ ! -d "$PROJECT_ROOT/.venv" ]; then
    echo "[!] Virtualenv not found. Run ./setup_env.sh first."
    exit 1
fi

. "$PROJECT_ROOT/.venv/bin/activate"

# -----------------------------
# Python steps
# -----------------------------

PYTHON="$PROJECT_ROOT/.venv/bin/python"

"$PYTHON" "$PROJECT_ROOT/Gif/Gif_to_asc/Gif-to-png/FrameExatractor.py"
"$PYTHON" "$PROJECT_ROOT/Gif/Gif_to_asc/png-to-asc/AscConverterNoArgs.py"

# -----------------------------
# C build
# -----------------------------
RENDER_C="$PROJECT_ROOT/Gif/Render/Render.c"
RENDER_OUT="$PROJECT_ROOT/Gif/Render/Render"
gcc "$RENDER_C" -O3 -o "$RENDER_OUT"

# -----------------------------
# Java build
# -----------------------------
PLAYER_JAVA="$PROJECT_ROOT/Gif/Player/Player.java"
javac "$PLAYER_JAVA"

# -----------------------------
# Run animation
# -----------------------------
cd "$PROJECT_ROOT"
java Gif.Player.Player
