# 🎬 Professional Guide to Terminal Video Production with asciinema

This document is a complete reference for using `asciinema` as a foundation for terminal-based video production. It presents a modern, professional-grade workflow tailored for faceless YouTube content based on CLI demonstrations.

---

## 🧭 Concept: Why asciinema?

`asciinema` is a CLI recording tool that captures terminal sessions as structured text events (not pixels). This makes it ideal for:

- High-precision terminal demos (DevOps, sysadmin, Linux tools)
- Blog-friendly embeds and SVG/MP4 conversion
- Re-editable, low-bandwidth assets
- AI-enhanced transformations

> asciinema is to terminal what vector is to image.

---

## ⚙️ Installation

```bash
# Debian / Ubuntu
sudo apt install asciinema

# macOS (Homebrew)
brew install asciinema
```

Optional tools:

```bash
npm install -g svg-term-cli  # For SVG rendering
sudo apt install ffmpeg      # For MP4 conversion
```

---

## ▶️ How It Works

### 🎥 Recording a Session

```bash
asciinema rec demo.cast
```

- Records input/output from current shell
- Outputs a `.cast` file (JSON-based format)
- Stops recording with `Ctrl+D` or `exit`

### 🔁 Playback Locally

```bash
asciinema play demo.cast
```

### 🌐 Share or Embed

```bash
asciinema upload demo.cast
# Link or embed in blogs/docs
```

---

## 🔄 Workflow Overview

| Step                    | Tool            | Output                         |
|-------------------------|------------------|----------------------------------|
| Record CLI session      | asciinema        | `.cast` file                     |
| Convert to SVG          | svg-term-cli     | `.svg` animation                 |
| Convert to MP4          | ffmpeg           | `.mp4` ready for editing         |
| Import to editor        | DaVinci Resolve  | Timeline with voiceover          |
| Publish                 | YouTube / Blog   | Final video or embedded session  |

---

## ✂️ Pre-processing `.cast`

### Manual editing

You can open `.cast` in a text editor to:

- Remove sensitive output (e.g. passwords)
- Trim pauses or idle lines
- Restructure sequences for clarity

### Automated tools

- `svg-term-cli`:
  ```bash
  svg-term --in demo.cast --out demo.svg --window --padding 10
  ```

- `agg` (alternative cast-to-mp4):
  ```bash
  cargo install agg
  agg render demo.cast -o demo.mp4
  ```

---

## 🤖 AI Tools for Enhancement

| Tool              | Purpose                      | Notes                            |
|-------------------|------------------------------|-----------------------------------|
| ffmpeg            | Render SVG to MP4            | Add overlays, transitions         |
| ElevenLabs / VO   | AI narration sync            | Align voiceover to cast sequence  |
| OpenAI GPT        | Auto-generate cast narration | Based on `.cast` content          |
| AI Subtitles (Resolve Studio) | Auto-captioning | Enriches accessibility            |

---

## 🔗 Software Integrations

| Tool / Platform     | Integration Point                   |
|----------------------|-------------------------------------|
| DaVinci Resolve      | Import `.mp4` into video timeline   |
| Hugo / MkDocs        | Embed asciinema player or SVG       |
| OBS Studio           | Overlay `.mp4` playback             |
| ChatGPT              | Script generation / summarization   |

---

## 🎨 Fonts, Colors, Scaling

- **Monospace fonts**: JetBrains Mono, Fira Code, Ubuntu Mono
- **Terminal background**: Dark slate (`#0f172a`) or light theme
- **Font size**: 16–20pt (for 1080p)
- **Color schemes**: Solarized Dark, Dracula, Nord
- **Scaling in SVG**: Use `--padding` or adjust width for responsive fit

---

## 💡 Best Practices

- Record **clean shell**, no prompt clutter
- Disable PS1 extras:
  ```bash
  export PS1="$ "
  ```
- Use real demos, not mock commands
- Add pauses for narration or voiceover sync
- Keep sessions short (<3 min) per video part

---

## ⚙️ Automation Strategies

| Task                     | Tool               | Automation Method               |
|--------------------------|--------------------|----------------------------------|
| Record & label cast      | Makefile / Script  | `make record-cast EP=03`         |
| Convert to MP4           | Shell script       | `convert-cast-to-mp4.sh`         |
| Sync VO + visuals        | DaVinci Macros     | Track templates in Resolve       |
| Auto-blog export         | Hugo / script      | Embed `.svg` or upload link      |

---

## 🆚 Alternatives to asciinema

| Tool             | Type           | Comparison                          |
|------------------|----------------|--------------------------------------|
| **ttyrec / ttygif** | CLI recorder  | Rawer, less structured               |
| **Terminalizer** | Node-based     | SVG+GIF exporter, heavier            |
| **Peek**         | GUI recorder   | Quick GIFs, not for long sessions    |
| **OBS Studio**   | Screen recorder| Full pixel-based video, not CLI-only |

---

## 📁 Folder Usage in Project

```
assets/
├── captures/               # asciinema-to-mp4 output
├── visuals/                # terminal.svg if SVG used
scripts/
├── epXX-script.md          # voiceover matches CLI demo
```

---

_Last updated: 2025-05-07_