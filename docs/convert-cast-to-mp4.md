# 🔁 Converting Asciinema `.cast` to `.mp4`

This guide explains how to convert terminal recordings made with `asciinema` into `.mp4` format, suitable for use in technical YouTube videos.

---

## 🧰 Requirements

Make sure the following tools are installed:

- [`svg-term-cli`](https://github.com/marionebl/svg-term-cli)
  ```bash
  npm install -g svg-term-cli
  ```
- [`ffmpeg`](https://ffmpeg.org/)
  ```bash
  sudo apt install ffmpeg
  ```

---

## 📄 Script: `convert-cast-to-mp4.sh`

This script converts a `.cast` file to `.svg` and then into a `.mp4` file.

### ✅ Usage

```bash
./convert-cast-to-mp4.sh <file.cast> <episode_number>
```

### Example

```bash
./convert-cast-to-mp4.sh ssh-demo.cast 02
```

This will produce:

- `assets/visuals/ep02-terminal.svg`
- `assets/captures/ep02-cast.mp4`

---

## 📁 Integration in Project Structure

```
assets/
├── visuals/
│   └── ep02-terminal.svg
└── captures/
    └── ep02-cast.mp4
```

You can then import `ep02-cast.mp4` into your video timeline and align it with the narration.

---

_Last updated: 2025-05-07_