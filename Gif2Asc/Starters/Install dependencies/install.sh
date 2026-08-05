#!/bin/bash

set -e

echo "Installing dependencies..."

# Update repositories only once
sudo apt-get update

# System dependencies
DEPENDENCIES=(
    python3
    python3-venv
    openjdk-11-jdk
    gcc
    jp2a
    docker.io
    mpv
)

# Python packages
PYTHON_PACKAGES=(
    pillow
    requests
    numpy
)

# Install system packages
echo "Installing system dependencies..."
sudo apt-get install -y "${DEPENDENCIES[@]}"

# Create virtual environment if it doesn't exist
VENV_PATH="Gif2Asc-TerminalMotion/Gif2Asc/venv"

if [ ! -d "$VENV_PATH" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_PATH"
fi

# Activate virtual environment
source "$VENV_PATH/bin/activate"

# Upgrade pip
python -m pip install --upgrade pip

# Install Python dependencies
echo "Installing Python packages..."
pip install "${PYTHON_PACKAGES[@]}"

# Install TermForge in editable mode
TERMFORGE_PATH="Gif2Asc-TerminalMotion/Gif2Asc/Engine/MidiaConvertion/TermForge"

if [ -d "$TERMFORGE_PATH" ]; then
    echo "Installing TermForge..."
    pip install -e "$TERMFORGE_PATH"
else
    echo "Warning: TermForge directory not found:"
    echo "$TERMFORGE_PATH"
fi

echo "All dependencies installed successfully!"