 ## Como instalar

 #### Docker 🐳
Recomendado se você não quer lidar com dependências manualmente.
 ```bash
 https://github.com/miguel-lamazares/Gif2Asc-TerminalMotion.git
 cd Gif2Asc-TerminalMotion/Gif2Asc/Docker
 docker build -t gif2asc .
 docker run -it gif2asc
 ```
 Isso cria o ambiente completo e evita dor de cabeça com versões, Python, Java e afins.

 #### Git 🧬
 Para quem prefere rodar tudo localmente.

 1. Clone o repositório
 ```bash
 https://github.com/miguel-lamazares/Gif2Asc-TerminalMotion.git
 cd Gif2Asc-TerminalMotion
 ```

 2. Instale as dependências Python
```bash
pip install pillow requests
pip install Gif2Asc-TerminalMotion/Gif2Asc/Engine/MidiaConvertion/TerminalLib -e .
```

 3. Instale a dependência do sistema
 - MPV (necessário para reprodução da animação no terminal)
 ```bash
 sudo apt install mpv
 ```

- caso queira instalar todas as dependecias para rodar localmente
```bash
 sudo apt install mpv python java-11-openjdk gcc jp2a git
 ```

- caso queira instalr via docker
```bash
 sudo apt install mpv python java-11-openjdk gcc jp2a git docker
```

ou clone o repositorio e execulte o comando start.sh para instalar todas as dependecias via terminal

4. Execute o projeto

#### shell command list

- Start: Gif2Asc/Starters/Linux/install dependences/start.sh - Instala todas as dependencias de forma automatica. Caso esteja no Kali ou em distros que restringem instalacoes diretas, considere usar uma venv.

- Full Process: Gif2Asc/Starters/Linux/full_process.sh - Faz o processo completo (download, conversao, renderizacao e execucao).
- Quick Start: Gif2Asc/Starters/Linux/quick_start.sh - Executa o processo sem personalizacao, usando a personalizacao da ultima execucao.

- Execute Last: Gif2Asc/Starters/Linux/execute_last.sh - Executa o ultimo arquivo em memoria, incluindo animacao e audio.

## Lista de dependecias

### Python 🐍
 - TerminalLib (ja incluida no projeto)
- Pillow
- Requests

 ### sistema 👨🏼‍💻
- MPV
- Python 3.x
 - Java JDK 11+
- GCC for C compilation
- JP2A for ASCII conversion
 - Docker
 - Git

