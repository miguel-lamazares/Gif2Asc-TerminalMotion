## Cómo instalar

#### Docker 🐳
Recomendado si no quieres manejar dependencias manualmente.

```bash
git clone https://github.com/miguel-lamazares/Gif2Asc-TerminalMotion.git
cd Gif2Asc-TerminalMotion/Gif2Asc/Docker
docker build -t gif2asc .
docker run -it gif2asc
```

Esto crea el entorno completo y evita problemas con versiones,
Python, Java y dependencias en general.

#### Git 🧬
Para quienes prefieren ejecutar todo localmente.

1. Clonar el repositorio
 ```bash
https://github.com/miguel-lamazares/Gif2Asc-TerminalMotion.git
cd Gif2Asc-TerminalMotion
```

2. Instalar dependencias de Python
```bash
pip install pillow requests
pip install Gif2Asc-TerminalMotion/Gif2Asc/Engine/MidiaConvertion/TerminalLib -e .
```

3. Instalar dependencia del sistema
- MPV (necesario para reproducir la animación en la terminal)
```bash
sudo apt install mpv
```

- Para instalar todas las dependencias localmente
```bash
sudo apt install mpv python java-11-openjdk gcc jp2a git
```

- Para instalar usando Docker
```bash
 sudo apt install mpv python java-11-openjdk gcc jp2a git docker
```

O clona el repositorio y ejecuta start.sh para instalar todo automáticamente.

4. Ejecutar el proyecto

### Solución de problemas
* ¿Error de permisos en pip? Usa `pip install --user ...` o un entorno virtual.
* ¿No se encuentra el comando `mpv`? Verifica la instalación y el PATH.
* ¿Problemas con Java? Confirma la versión con `java -version`.

#### Lista de comandos shell

- Start:
  Instala todas las dependencias automáticamente.

- Full Process:
  Ejecuta todo el proceso completo.

- Quick Start:
  Ejecuta el proceso sin personalización.

- Execute Last:
  Ejecuta el último archivo en memoria con animación y audio.

## Lista de dependencias

### Python 🐍
(idéntica funcionalmente a la sección EN-US)

### Sistema 👨🏼‍💻
(idéntica funcionalmente a la sección EN-US)
