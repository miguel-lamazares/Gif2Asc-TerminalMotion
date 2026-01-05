#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

RENDER_C="$PROJECT_ROOT/Engine/Render/Render.c"
RENDER_OUT="$PROJECT_ROOT/Engine/Render/Render"
PLAYER_JAVA="$PROJECT_ROOT/Engine/Player/Player.java"

gcc "$RENDER_C" -O3 -o "$RENDER_OUT"

javac "$PLAYER_JAVA"

cd "$PROJECT_ROOT"
java Gif2Asc/Engine/Player/Player
