# 🖼️ Transparent Terminal Overlay Workflow (asciinema ➜ DaVinci Resolve)

This guide outlines how to turn an `asciinema` terminal session into a transparent video overlay that can be composited over footage (e.g., a building scene) using DaVinci Resolve or another video editor.

---

## 🎯 Goal

To simulate a floating or embedded terminal on a background video — such as a terminal "projected" onto a wall, monitor, or HUD.

---

## 🧪 Step-by-Step Workflow

### 1. Record Your Terminal Session

```bash
asciinema rec demo.cast
# Run your colorful CLI commands
exit
```

---

### 2. Generate SVG Without Background

```bash
svg-term --in demo.cast --out demo.svg --no-window --padding 20 --theme dracula --font "Fira Code"
```

---

### 3. Convert SVG to PNG (Frame or Sequence)

```bash
inkscape demo.svg --export-type=png --export-filename=frame01.png
```

> For sequences: duplicate SVG frame logic or create custom steps with animation

---

### 4. Convert PNG(s) to Transparent Video (.mov)

```bash
ffmpeg -framerate 30 -i frame%02d.png -c:v prores_ks -profile:v 4 -pix_fmt yuva444p10le terminal-overlay.mov
```

- Uses ProRes 4444 to retain alpha transparency

---

### 5. Import into DaVinci Resolve

- Import `terminal-overlay.mov`
- Add to timeline above main video
- Use `Composite Mode`: Add / Screen / Lighten
- Optionally: mask, track, warp, glow in Fusion

---

## 🧩 Recommended Add-Ons

| Effect              | Tool in Resolve         |
|---------------------|-------------------------|
| Perspective         | Planar Tracker          |
| Glow around text    | Fusion → Soft Glow      |
| Embed in screen     | Polygon Mask + CornerPin|
| CRT/Scanlines       | Overlay PNG with blend  |

---

## ✅ Output

- `.mov` file with alpha channel
- Terminal video usable as overlay in any professional timeline

---

_Last updated: 2025-05-07_