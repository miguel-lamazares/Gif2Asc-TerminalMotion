#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

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
