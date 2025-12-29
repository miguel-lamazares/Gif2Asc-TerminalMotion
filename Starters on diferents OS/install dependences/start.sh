set -e

ROOT="$(cd "$(dirname "$0")" && pwd)"

if [ ! -d "$ROOT/.venv" ]; then
    echo "[!] Virtualenv not found. Run ./setup_env.sh first."
    exit 1
fi

DEPENDENCIES=("python3" "openjdk-11-jdk" "gcc" "jp2a" "docker.io")
for dep in "${DEPENDENCIES[@]}"; do
    echo "Installing $dep..."
    sudo apt-get install -y "$dep"
done

# Then setup Python environment
. "$ROOT/.venv/bin/activate"
pip install --upgrade pip
pip install -r requirements.txt

echo "All dependencies installed!"
