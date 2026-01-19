#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

# -----------------------------
# Activate virtualenv
# -----------------------------
if [ ! -d "$PROJECT_ROOT/Gif2Asc/venv" ]; then
    echo "[!] Virtualenv not found. Run ./setup_env.sh first."
    exit 1
fi

. "$PROJECT_ROOT/Gif2Asc/venv/bin/activate"

# -----------------------------
# Python steps
# -----------------------------

PYTHON="$PROJECT_ROOT/Gif2Asc/venv/bin/python"

"$PYTHON" "$PROJECT_ROOT/Gif2Asc/Engine/MidiaConvertion/FramesExtration/FrameExtractor.py"
"$PYTHON" "$PROJECT_ROOT/Gif2Asc/Engine/MidiaConvertion/PngTreatment/PNGPersonalizer.py"
"$PYTHON" "$PROJECT_ROOT/Gif2Asc/Engine/MidiaConvertion/FramesConversion/AscConverter.py"

# -----------------------------
# C build
# -----------------------------
RENDER_C="$PROJECT_ROOT/Gif2Asc/Engine/Render/Render.c"
RENDER_OUT="$PROJECT_ROOT/Gif2Asc/Engine/Render/Render"
gcc "$RENDER_C" -O3 -o "$RENDER_OUT"

# -----------------------------
# Java build
# -----------------------------
PLAYER_JAVA="$PROJECT_ROOT/Gif2Asc/Engine/Player/*.java"
javac "$PLAYER_JAVA"

# -----------------------------
# Run animation
# -----------------------------
cd "$PROJECT_ROOT"
java Gif2Asc.Engine.Player.Main
