# 🔗 asciinema Integration Guide: DaVinci Resolve, PowerPoint, Hugo, MkDocs

This document describes how to integrate `asciinema` terminal recordings into various production environments such as video editors, presentation software, and static site generators.

---

## 🎬 Integration with DaVinci Resolve

### ✅ Workflow

1. **Record** with asciinema:
   ```bash
   asciinema rec scripts/demo.cast
   ```

2. **Convert `.cast` to `.svg`** using `svg-term-cli`:
   ```bash
   svg-term --in scripts/demo.cast --out visuals/demo.svg --font "JetBrains Mono" --theme "dracula" --window
   ```

3. **Convert `.svg` to `.mp4`** with `ffmpeg`:
   ```bash
   ffmpeg -loop 1 -i visuals/demo.svg -t 10 -pix_fmt yuv420p captures/demo.mp4
   ```

4. **Import `.mp4` into Resolve** timeline, sync with narration or music.

> Bonus: Add zoom, pan, highlight using Fusion effects.

---

## 📊 Integration with PowerPoint / Keynote

### Option 1: Static `.svg` (Slide)

- Export `.svg` as described above
- Insert into slide (Insert → Picture)
- Add annotations / bullet points

### Option 2: Animated `.mp4`

- Convert `.cast` → `.mp4`
- Insert (Insert → Video → File)
- Set to autoplay on slide transition

> Perfect for command walkthroughs in tech presentations.

---

## 📚 Integration with MkDocs + Material Theme

### Embed using HTML block

```markdown
!!! example "Live Terminal Demo"
    <asciinema-player src="/assets/demo.cast" cols="80" rows="20" preload></asciinema-player>
```

### Requirements

- Install `asciinema-player` JS/CSS in `extra_javascript` and `extra_css`
- Place `.cast` in `docs/assets/`

---

## 🌐 Integration with Hugo + Docsy Theme

### Option 1: Embed `.svg`

1. Convert `.cast` → `.svg`
2. Place SVG under `/static/images/demo.svg`
3. Embed in Markdown content:

```markdown
![Terminal Demo](/images/demo.svg)
```

### Option 2: Embed YouTube/MP4 (if hosted externally)

- Use shortcodes or raw HTML in content:

```markdown
{{< figure src="https://example.com/demo.mp4" >}}
```

---

## 🛠️ Makefile Automation Example

```makefile
asciinema-to-mp4:
	asciinema rec scripts/ep03.cast
	svg-term --in scripts/ep03.cast --out visuals/ep03.svg --font "Fira Code" --theme "solarized-dark"
	ffmpeg -loop 1 -i visuals/ep03.svg -t 8 -pix_fmt yuv420p captures/ep03.mp4
```

---

## ✅ Best Practices

- Use monospaced fonts: `JetBrains Mono`, `Fira Code`, `Cascadia Code`
- Stick to 80–100 columns width for terminal
- Dark background (`#0f172a`), padding for readability
- MP4s work across all platforms if SVG embedding is limited

---

_Last updated: 2025-05-07_

# 🧬 Vector-Based Videos: Concept and Use in Terminal Recording

This section explains what vector videos are, how they differ from raster video, and how they apply in terminal-based tutorials using `asciinema` and `svg-term`.

---

## 🧠 What is a Vector Video?

Vector videos are animations composed of geometric shapes, text, and paths defined mathematically. Unlike raster videos (which are pixel grids), vector videos scale perfectly at any resolution.

| Feature        | Vector Video                   | Raster Video (.mp4, .mov)         |
|----------------|----------------------------------|-----------------------------------|
| 🔍 Scalable     | Yes, without quality loss        | No, can become pixelated          |
| 📦 File Size    | Small for simple graphics        | Larger even for basic content     |
| ✍️ Text Clarity | Excellent for code, diagrams     | May blur or compress text         |
| 🎞️ Realism      | Not ideal for photo/video scenes | Ideal for GUI, screencasts        |

---

## 🛠️ How to Create Vector Videos from Terminal Sessions

1. **Record session** with asciinema:
   ```bash
   asciinema rec scripts/demo.cast
   ```

2. **Convert to SVG animation**:
   ```bash
   svg-term --in scripts/demo.cast --out visuals/demo.svg      --window --padding 10 --font "Fira Code" --theme "dracula"
   ```

3. **Optional: Convert to `.mp4`** while preserving clarity:
   ```bash
   ffmpeg -loop 1 -i visuals/demo.svg -t 10 -pix_fmt yuv420p captures/demo.mp4
   ```

---

## 🔠 Fonts & Themes

| Font             | Purpose                          |
|------------------|-----------------------------------|
| JetBrains Mono   | Readable monospace for code       |
| Fira Code        | Ligatures and clarity             |
| Cascadia Code    | Default in Windows Terminal       |
| Ubuntu Mono      | Balanced look                     |

Recommended theme: `Dracula`, `Solarized Dark`, `Nord`

---

## 💡 Best Use Cases for Vector Videos

- Technical videos with code or terminal commands
- Blog-ready SVG animations
- Presentation-grade motion content (PowerPoint, Keynote)
- Embedded Hugo/MkDocs educational materials

---

## 🧩 Tools That Use or Export Vector Videos

| Tool            | Usage                                  |
|------------------|----------------------------------------|
| svg-term-cli     | asciinema → SVG animation              |
| Rive             | UI/UX vector animations                |
| Lottie (JSON)    | Web vector scenes exported from AE     |
| ffmpeg + SVG     | Create readable `.mp4` from `.svg`     |
| After Effects    | Motion graphics with vector layers     |

---

_Last updated: 2025-05-07_