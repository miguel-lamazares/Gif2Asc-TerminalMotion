## How to Install

#### Docker 🐳
Recommended if you do not want to deal with dependencies manually.
 
```bash
git clone https://github.com/miguel-lamazares/Gif2Asc-TerminalMotion.git
cd Gif2Asc-TerminalMotion/Gif2Asc/Docker
docker build -t gif2asc .
docker run -it gif2asc
```

This creates the complete environment and avoids headaches with versions,
Python, Java, and related dependency chaos.

#### Git 🧬
For those who prefer to run everything locally.

1. Clone the repository
```bash
https://github.com/miguel-lamazares/Gif2Asc-TerminalMotion.git
cd Gif2Asc-TerminalMotion
```

2. Install Python dependencies
```bash
pip install pillow requests
pip install Gif2Asc-TerminalMotion/Gif2Asc/Engine/MidiaConvertion/TerminalLib -e .
```

3. Install system dependency
- MPV (required to play animation in the terminal)
```bash
sudo apt install mpv
```

- If you want to install all dependencies to run locally
```bash
sudo apt install mpv python java-11-openjdk gcc jp2a git
```

- If you want to install using Docker
```bash
sudo apt install mpv python java-11-openjdk gcc jp2a git docker
```

Or clone the repository and run start.sh to install all dependencies automatically via terminal.

4. Run the project

### Troubleshooting
* Permission error with pip? Use `pip install --user ...` or a virtual environment
   (`python -m venv venv && source venv/bin/activate`).
* `mpv` command not found? Verify the package installation and PATH.
* Java dependency issues? Confirm the installed version with `java -version`.

#### Shell command list

- Start:
   Gif2Asc/Starters/Linux/install dependences/start.sh
   Automatically installs all dependencies.
   If you are on Kali or restrictive distros, consider using a venv.

- Full Process:
  Gif2Asc/Starters/Linux/full_process.sh
  Executes the complete process (download, conversion, rendering, execution).

- Quick Start:
  Gif2Asc/Starters/Linux/quick_start.sh
  Executes the process without customization, using the last configuration.

 - Execute Last:
   Gif2Asc/Starters/Linux/execute_last.sh
   Executes the last file in memory, including animation and audio.

## Dependency List

### Python 🐍

| Dependency   | Required For                                  | Installation Method |
|--------------|-----------------------------------------------|---------------------|
| Pillow       | Image processing (open, manipulate, save)     | pip install pillow |
| Requests     | HTTP requests (e.g., download files)          | pip install requests |
| TerminalLib  | Terminal graphics library (project component) | pip install Gif2Asc-TerminalMotion/Gif2Asc/Engine/MidiaConvertion/TerminalLib -e . |

### System 👨🏼‍💻

| Dependency     | Required For                                | Installation Method |
|----------------|---------------------------------------------|---------------------|
| MPV            | Play audio in terminal                      | sudo apt install mpv |
| Python 3.x     | Execute Python code                         | sudo apt install python |
| Java JDK 11+   | Compile and run Java engine components      | sudo apt install openjdk-11-jdk |
| GCC            | Compile engine components                   | sudo apt install gcc |
| JP2A           | Convert animation frames                    | sudo apt install jp2a |
| Git            | Manage repositories                         | sudo apt install git |
| Docker (Optional) | Isolate the entire environment           | sudo apt install docker.io |

