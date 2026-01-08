 ## Como instalar

 #### Docker 🐳
Recomendado se você não quer lidar com dependências manualmente.
 ```bash
 git clone https://github.com/miguel-lamazares/Gif2Asc-TerminalMotion.git
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

### Solução de Problemas
*   **Erro de permissão no pip?** Use `pip install --user ...` ou um ambiente virtual (`python -m venv venv && source venv/bin/activate`).
*   **O comando `mpv` não encontrado?** Verifique se o pacote foi instalado corretamente e se está no seu `PATH`.
*   **Problemas com dependências Java?** Confirme a versão instalada com `java -version`.

#### shell command list

- Start: Gif2Asc/Starters/Linux/install dependences/start.sh - Instala todas as dependencias de forma automatica. Caso esteja no Kali ou em distros que restringem instalacoes diretas, considere usar uma venv.

- Full Process: Gif2Asc/Starters/Linux/full_process.sh - Faz o processo completo (download, conversao, renderizacao e execucao).
- Quick Start: Gif2Asc/Starters/Linux/quick_start.sh - Executa o processo sem personalizacao, usando a personalizacao da ultima execucao.

- Execute Last: Gif2Asc/Starters/Linux/execute_last.sh - Executa o ultimo arquivo em memoria, incluindo animacao e audio.

## Lista de dependecias

### Python 🐍

| Dependência | Necessária Para | Método de Instalação |
| :--- | :--- | :--- |
| **Pillow** | Processamento de imagens (abrir, manipular e salvar diferentes formatos de imagem) | `pip install pillow ` |
| **Requests** | Fazer requisições HTTP (por exemplo, para baixar arquivos da web) | `pip install requests` |
| **TerminalLib** | Biblioteca que fornece funcionalidades gráficas para o terminal (parte do projeto) | `pip install Gif2Asc-TerminalMotion/Gif2Asc/Engine/MidiaConvertion/TerminalLib -e .` Nota: Execute a partir da raiz do projeto. |

 ### sistema 👨🏼‍💻

| Dependência | Necessária Para | Método de Instalação |
| :--- | :--- | :--- |
| **MPV** | Reproduzir áudio no terminal | `sudo apt install mpv` |
| **Python 3.x** | Interpretador Python para executar o código. | `sudo apt install python` |
| **Java JDK 11+** | Compilar e executar componentes do motor escritos em Java. | `sudo apt install openjdk-11-jdk` |
| **GCC** | Compilar componentes do motor | `sudo apt install gcc` |
| **JP2A** | Converter quadros da animação | `sudo apt install jp2a` |
| **Git** | Gerenciar diretorios | `sudo apt install git` |
| **Docker (Opcional)** | Isolar todo o ambiente | `sudo apt install docker.io` |


