# 🖥️ Terminal Video Production Toolkit

A modular, CLI-first toolkit for professional terminal recording, simulation, and video rendering based on `asciinema`.

---

## 📂 Project Structure

```text
terminal-video/
├── scripts/         # All core automation scripts
├── assets/          # Input/output artifacts
├── configs/         # Terminal appearance configs
├── docs/            # Usage guides and references
```

---

## 🚀 Features

- Typing + Tab-complete simulation (guru mode)
- Full `.cast` → `.svg` → `.mp4` / `.mov`
- Transparent overlays for DaVinci Resolve
- Hugo/MkDocs embed support

---

## 🧵 Workflow Overview

| Stage       | Script                        | Input              | Output                | Dir           |
|-------------|-------------------------------|---------------------|------------------------|---------------|
| 🎥 Record    | `prepare-and-record-cast.sh`  | —                   | `raw/*.cast`           | `assets/raw/` |
| ⌨️ Typing    | `simulate-typing.py`          | `raw/*.cast`        | `processed/*.cast`     | `assets/processed/` |
| 🧠 Guru      | `simulate-guru-extended.py`   | `processed/*.cast`  | `processed/*.cast`     | —             |
| 🎨 Render    | `render-cast-wsl.sh`          | `*.cast`            | `visuals/*.svg` + `captures/*.mp4` | `assets/` |
| 🖼️ Overlay   | `generate-terminal-overlay.sh`| `*.cast`            | `captures/*.mov`       | —             |

---

## 🛠️ Terminal Setup

- Font: `JetBrains Mono` / `Fira Code`
- Theme: Dracula / Nord
- Resolution: 128×72 (16:9 aspect) → see [terminal-resolution-guide.md](docs/terminal-resolution-guide.md)

---

## 📘 Docs

See full guides in `docs/`:

- [asciinema-complete-guide.md](docs/asciinema-complete-guide.md)
- [simulate-typing-guide.md](docs/simulate-typing-guide.md)
- [simulate-guru-extended-guide.md](docs/simulate-guru-extended-guide.md)
- [convert-cast-to-mp4.md](docs/convert-cast-to-mp4.md)
- [terminal-coloring-guide.md](docs/terminal-coloring-guide.md)
- [asciinema-coloring-guide.md](docs/asciinema-coloring-guide.md)
- [terminal-resolution-guide.md](docs/terminal-resolution-guide.md)
- [terminal-overlay-workflow.md](docs/terminal-overlay-workflow.md)
- [asciinema-integration-guide.md](docs/asciinema-integration-guide.md)
