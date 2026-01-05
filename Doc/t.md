# Gif to ASC II 🎥

This simple project makes your terminal show gifs as ASC II arts.

## Architecture 
### What I Used and Why
#### Python 🐍
Responsible for managing files, transforming GIFs into frames, and converting them into ASCII art using JP2A.
#### TerminalLib 🏞️
A custom library used to make the terminal more user-friendly and error-free, avoiding unnecessary prompts (e.g., "how old are you?").

#### Java ☕
The heart of the project. It controls the terminal, orchestrates C, manages screen timing, and shares the correct file with C.

#### C ⚙️
Acts as a graphics engine. It handles the heavy lifting, printing and clearing large strings.

#### Shell 🐚
All commands compiled into three forms:

* Full process: Provide the GIF and configs before starting.
* Just the GIF address: No config needed, uses the last saved config to start.
* Execute only: Runs the GIF in memory (or the last loaded GIF).

#### Docker 🐳
The project image for easier use, including JDK, libraries, Python, GCC, and all necessary commands.

## How it works
<div align="center"  justify-content="center">
<p></p>
  <img src="./Img/howItWorks.svg">
</div>

### Talking a little bit about the libs:

1. JP2A
It's a very famomus by be a great for to convert image in ASC arts.
for more information about this fancy procejt acess: <a href="https://github.com/cslarsen/jp2a">Official GitHub</a>

2. Pilow
a excellent image tool, you can do many things using it, i made a captha solver using it.
for more information about this fancy procejt acess: <a href="https://python-pillow.github.io">Official Site</a>

3. TerminalLib
a simple lib in python and java, i made it thinking, ok this will works on terminal, but doesn't need to be ugly or with input errors.
check it in: <a href="https://github.com/miguel-lamazares/TerminalLib">GitHub</a>

#### Python's pipeline:

* ```FrameExatractor.py```: Responsible for taking the gifs and transform them in frames, each frame is an image in PNG, all frames going to save in a folder, it always clean the folder before to save something.

* ```AscConverter.py or AscConverterNoArgs.py```: both codes are almost the same thing, but after running, the first always save the config that was used and the other use this json for using the last configs. Now the iguals part, they take configs via user or file after it, the JP2A trasforms all frames in ASC arts that are saves in ASC file in a folder, it always clean the folder before to save something.

#### Java and C, the brain and the heart of the project
* ```Player.java```: it controls the frames with C, java's use C by subprocess, it constrols with time with FPS, doesn't touch in the terminal, only shere the strings.
* ```Render.c```: it wait Java's orders, when a string arrives, always it clean the last string and print other.
### Installation

#### Docker
Ensure you have Docker installed on your system.
Pull the Docker image:

```c
docker pull miguel-lamazares/gif2asc-terminalmotion:latest
```
Run the container:

```c
docker run -it miguel-lamazares/gif2asc-terminalmotion:latest
```
#### Git:

* Install everthing in the dependency list befort to use.
* Install the repository on your pc with this below
```c
git clone https https://github.com/miguel-lamazares/Gif2Asc-TerminalMotion.git
```
after it just execute on your pc, please the Dependency list.

### Shell Commands
* Full Process: ./full_process.sh 
* Quick Start: ./quick_start.sh 
* Execute Last: ./execute_last.sh 

### Dependencies
* Python 3.x
* Java JDK 11+
* GCC for C compilation
* JP2A for ASCII conversion
* Custom TerminalLib (included in repo)
* pillow
* Docker (for containerized deployment)
