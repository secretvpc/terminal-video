# Terminal Video Production – Workflow Overview

This document outlines the complete processing pipeline used in the `terminal-video` project. It describes each phase, required inputs, expected outputs, and the tools/scripts involved.

---

## 🧭 Workflow Stages

| Stage          | Description                                                  | Script                          | Input               | Output                      |
|----------------|--------------------------------------------------------------|----------------------------------|----------------------|-----------------------------|
| 1. Record      | Start terminal capture with optimal size, colors, aliasing   | `prepare-and-record-cast.sh`    | —                    | `assets/raw/*.cast`        |
| 2. Simulate    | Add realistic typing or guru-level automation                | `simulate-typing.py` / `simulate-guru-extended.py` | `raw/*.cast` | `processed/*.cast`         |
| 3. Render SVG  | Convert cast to styled vector graphics (WSL-aware)           | `render-cast-wsl.sh`            | `.cast`              | `assets/visuals/*.svg`     |
| 4. Encode MP4  | Create high-resolution videos for playback or distribution   | ffmpeg (called in render script)| `.svg`               | `assets/captures/*.mp4`    |
| 5. Overlay MOV | Optional: Create transparent overlays for video editors      | `generate-terminal-overlay.sh`  | `.cast`              | `assets/captures/*.mov`    |

---

## 💡 Notes on Recording

- Preferred environment: headless Linux VM or container
- Set resolution to `128x72` characters
- Use preconfigured `LS_COLORS.sh` and `dircolors`
- Avoid mouse interaction or GUI dependencies

---

## 🔁 Automation Goals

- Every script is designed to run from CLI with minimal arguments
- Intermediate outputs are organized under `assets/`
- The full process is compatible with Makefile-style chaining

---

## 🔗 Next Steps

- See [terminal-resolution-guide.md](terminal-resolution-guide.md)
- See [simulate-typing-guide.md](simulate-typing-guide.md)
- See [convert-cast-to-mp4.md](convert-cast-to-mp4.md)

