# Terminal Video Production Toolkit

## Overview

This repository provides a modular, CLI-first framework for capturing, simulating, and rendering terminal sessions as high-quality video. It is designed for educational content production, technical tutorials, and professional screencasts. The toolkit builds upon `asciinema` and enhances it with automation, styling, and rendering workflows.

---

## Objectives

* Enable consistent, high-fidelity terminal capture across environments
* Provide realistic typing and command simulation ("guru mode")
* Support SVG and video output, including transparent overlays
* Allow integration with Hugo, MkDocs, or other documentation systems

---

## Directory Layout

```text
terminal-video/
├── scripts/         # CLI automation scripts for each workflow stage
├── assets/          # Input and generated output files (cast, svg, mp4)
├── configs/         # Terminal appearance customization (colors, fonts)
├── docs/            # Supplementary guides and technical documentation
```

---

## Functional Modules

| Stage      | Script                         | Input              | Output                       | Location           |
| ---------- | ------------------------------ | ------------------ | ---------------------------- | ------------------ |
| Recording  | `prepare-and-record-cast.sh`   | —                  | `assets/raw/*.cast`          | Shell script       |
| Typing Sim | `simulate-typing.py`           | `raw/*.cast`       | `processed/*.cast`           | Python script      |
| Guru Sim   | `simulate-guru-extended.py`    | `processed/*.cast` | `processed/*.cast`           | Python script      |
| Rendering  | `render-cast-wsl.sh`           | `.cast`            | `.svg`, `.mp4`               | Shell script (WSL) |
| Overlay    | `generate-terminal-overlay.sh` | `.cast`            | `.mov` (ProRes, transparent) | Shell script       |

---

## Terminal Configuration

* **Font**: JetBrains Mono / Fira Code
* **Theme**: Dracula, Nord (via `dircolors`)
* **Resolution**: 128x72 characters (16:9 aspect ratio)
* See: `docs/terminal-resolution-guide.md`, `configs/LS_COLORS.sh`

---

## Documentation

The following guides are available under `docs/`:

* `asciinema-complete-guide.md`
* `simulate-typing-guide.md`
* `simulate-guru-extended-guide.md`
* `convert-cast-to-mp4.md`
* `terminal-coloring-guide.md`
* `terminal-overlay-workflow.md`
* `terminal-resolution-guide.md`
* `asciinema-coloring-guide.md`
* `asciinema-integration-guide.md`

---

## Dependencies

* asciinema
* svg-term-cli
* ffmpeg (w/ libx264, ProRes)
* Python 3.x + rich
* bash / WSL / POSIX-compliant shell

---

## License

MIT License.

---

## Authors

Developed by the `terminal-video` project contributors.

For contributions, see `CONTRIBUTING.md` (if present).
