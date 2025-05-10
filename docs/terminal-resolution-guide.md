# 📐 Terminal Resolution for 16:9 Video Production

This guide explains how to configure your terminal to match the 16:9 aspect ratio standard for YouTube and professional video production, ensuring compatibility with `asciinema`, `svg-term`, and video editors.

---

## 🧠 Why 16:9 for Terminal Sessions?

- Matches YouTube and editing timelines (e.g. 1920×1080, 1280×720)
- Avoids black bars (letterboxing/pillarboxing)
- Easier visual centering in `.svg`/`.mp4` exports
- Cleaner visuals in thumbnails and demos

---

## 📊 What is 16:9 in Terminal Dimensions?

| Width (cols) | Height (rows) | Aspect Ratio | Notes           |
|--------------|----------------|---------------|------------------|
| 120          | 67             | ≈ 16:9        | Good default     |
| 128          | 72             | ≈ 16:9        | Excellent match  |
| 100          | 56             | ≈ 16:9        | Tight fit        |
| 80           | 24             | 4:3 (legacy)  | Not recommended  |

> Formula: `rows = columns × (9 / 16)`

---

## 🛠️ How to Set 16:9 Terminal in Different Environments

### ✅ Graphical Terminal (Kitty, Alacritty, Windows Terminal)

**In `alacritty.yml`:**
```yaml
window:
  dimensions:
    columns: 128
    lines: 72
```

**In Windows Terminal JSON:**
```json
"initialCols": 128,
"initialRows": 72
```

---

### ✅ Headless Linux / SSH

Set shell environment:
```bash
export COLUMNS=128
export LINES=72
```
Or use:
```bash
stty cols 128 rows 72
```

> This affects logical terminal size for commands and `asciinema` recordings.

---

## 🖼️ Rendering with `svg-term`

`svg-term` reads dimensions from `.cast`, or you can enforce:

```bash
svg-term --in demo.cast --out demo.svg --width 128 --height 72 --window
```

This ensures exported `.svg` and `.mp4` match video expectations.

---

## ✅ Best Practice Matrix

| Use Case               | Suggested Size |
|------------------------|----------------|
| YouTube HD Video       | `128x72`       |
| Blog Embed             | `100x56`       |
| Compact CLI walkthrough| `80x45`        |
| Classic TUI Style      | `80x24`        |

---

_Last updated: 2025-05-07_