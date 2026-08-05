<h1 align="center">Gif2Asc - Terminal Motion 🎥✨</h1>

<p align="center">
  <i>Transform GIFs, videos, and images into animated ASCII art — right on your device.</i>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-86%25-3776AB?logo=python&logoColor=white">
  <img alt="Java" src="https://img.shields.io/badge/Java-6%25-ED8B00?logo=openjdk&logoColor=white">
  <img alt="Shell" src="https://img.shields.io/badge/Shell-3%25-4EAA25?logo=gnubash&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-blue.svg">
</p>

---

## 📖 About the project

**Gif2Asc — Terminal Motion** turns your GIFs and videos into animated ASCII art right in your terminal — complete with optional soundtrack and live controls for speed and volume.

It’s a small experiment that mixes image processing, terminal rendering and a bit of nostalgia. Perfect for fun, demos, or just to make your terminal feel a little more alive.

---

## 🌍 Documentation

<div align="center">

<table>
<tr>
<td align="center">
<img src="Midias for Readme/Flags/br.svg" width="40"><br>
<b>Português</b><br>
<a href="Doc/pt/instalacao.md">Instalação</a><br>
<a href="Doc/pt/comoUsar.md">Como usar</a><br>
<a href="Doc/pt/personalizacao.md">Personalização</a><br>
<a href="Doc/pt/comoFunciona.md">Como funciona?</a><br>
<a href="Doc/pt/Contribuicao.md">Contribuição</a>
</td>

<td align="center">
<img src="Midias for Readme/Flags/us.svg" width="40"><br>
<b>English</b><br>
<a href="Doc/en/installation.md">Installation</a><br>
<a href="Doc/en/howToUse.md">How to use</a><br>
<a href="Doc/en/customization.md">Customization</a><br>
<a href="Doc/en/howDoesItWorks.md">How does it work?</a><br>
<a href="Doc/en/Contribution.md">Contribution</a>
</td>

<td align="center">
<img src="Midias for Readme/Flags/es.svg" width="40"><br>
<b>Español</b><br>
<a href="Doc/es/instalacion.md">Instalación</a><br>
<a href="Doc/es/comousar.md">Cómo usar</a><br>
<a href="Doc/es/personalizacion.md">Personalización</a><br>
<a href="Doc/es/comoFunciona.md">¿Cómo funciona?</a><br>
<a href="Doc/es/contribucion.md">Contribución</a>
</td>
</tr>
</table>

</div>

---

## ✨ Features

- 🎞️ Converts **GIFs and media** into animated ASCII art
- 🔊 Plays an **optional soundtrack** in sync with the animation
- ⚙️ **Live controls** for FPS and volume during playback
- 🎨 Customizable character ramps and rendering width
- 🧩 Cross-language core (Python · Java · Shell)
- 🪶 Lightweight and runs in any modern terminal

---

## ⚡ Quick start

```bash
# Clone the repo
git clone https://github.com/miguel-lamazares/Gif2Asc-TerminalMotion.git
cd Gif2Asc-TerminalMotion/Gif2Asc

# Run
python main.py path/to/your.gif
```

> Need detailed setup instructions? Check the [installation guide](Doc/en/installation.md).

---

## 🎮 Controls

While the animation is playing:

 Key | Action |
-----|--------|
 ➡️ | Turn the volume **up** |
 ⬅️ | Turn the volume **down** |
 ⬆️ | Increase **FPS** |
 ⬇️ | Decrease **FPS** |
 ⏎ `Enter` | **Stop / finish** playback |

---

## 🧠 How it works

<div align="center">
  <img src="Midias for Readme/IMG/Diag.svg" alt="Pipeline diagram">
</div>

Here's the magic: each frame gets **resized**, turned into **grayscale**, and then each pixel is turned into an ASCII character based on its **brightness**. These frames are then played back in sequence at a speed you control — and you can even add a soundtrack if you want.

Want the deep dive? See [How does it work?](Doc/en/howDoesItWorks.md).

---

## 🖼️ Gallery

<p align="center">
  <img src="Midias for Readme/Media/Undertale.gif" width="45%">
  <img src="Midias for Readme/Media/BadApple.gif" width="45%">
  <img src="Midias for Readme/Media/CS2 Dance.gif" width="45%">
  <img src="Midias for Readme/Media/Drifting cars.gif" width="45%">
  <img src="Midias for Readme/Media/Hunter.gif" width="45%">
  <img src="Midias for Readme/Media/Law.gif" width="45%">
  <img src="Midias for Readme/Media/Jester dance.gif" width="45%">
  <img src="Midias for Readme/Media/Little car with his back fire.gif" width="45%">
  <img src="Midias for Readme/Media/Nyan cat.gif" width="45%">
  <img src="Midias for Readme/Media/Skull.gif" width="45%">
  <img src="Midias for Readme/Media/Denji.gif" width="45%">
  <img src="Midias for Readme/Media/Alucard.gif" width="45%">
</p>

---

## 🔗 Related projects

- 🟦 [**NT Steam**](https://github.com/miguel-lamazares/Nt-Steam) — turn ASCII art into Steam comments
- 🖥️ [**TermForge**](https://github.com/miguel-lamazares/TerminalLib) — your terminal doesn’t need to be ugly

---

## 🤝 Contributing

Got an idea, a bug fix, or a new feature in mind? Contributions are very welcome!
Check the contribution guide in your language: [PT](Doc/pt/Contribuicao.md) · [EN](Doc/en/Contribution.md) · [ES](Doc/es/contribucion.md).

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

<p align="center">
  Made with ☕ and a lot of <code>printf</code> by <a href="https://github.com/miguel-lamazares"><b>Miguel Lamazares</b></a>.<br>
  <i>Follow me on GitHub for more projects and experiments.</i>
</p>