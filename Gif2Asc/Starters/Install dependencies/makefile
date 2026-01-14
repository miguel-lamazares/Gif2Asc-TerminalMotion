#!/bin/bash

echo "Installing dependencies..."

python3 -m venv Gif2Asc-TerminalMotion/Gif2Asc/venv
source Gif2Asc-TerminalMotion/Gif2Asc/venv/bin/activate

# Dependencies
DEPENDENCIES=(
    "python"
    "java-11-openjdk"
    "gcc"
    "jp2a"
    "docker"
    "mpv"
)

# Python packages
PYTHON_PACKAGES=(
    "pillow"
    "requests"
    "numpy"
)

# Install system dependencies
for dep in "${DEPENDENCIES[@]}"; do
    echo "Installing $dep..."
	sudo apt-get update
    sudo apt-get install -y "$dep"
	sudo apt-get install -y docker
done

# Install Python packages
echo "Installing Python packages..."
pip install "${PYTHON_PACKAGES[@]}"

pip install Gif2Asc-TerminalMotion/Gif2Asc/Engine/MidiaConvertion/TerminalLib -e .

echo "All dependencies installed!"