# Terminal Video Production Toolkit

## Overview

This project provides a modular pipeline for producing high-quality, stylized video from CLI-based workflows. It leverages `asciinema` recordings, post-processes them with simulated typing behavior, and outputs polished `.svg`, `.mp4`, or `.mov` formats suitable for documentation, tutorials, or video production pipelines.

The entire pipeline is optimized to minimize manual intervention and maximize repeatability across Linux and WSL/Windows environments.

---

## Use Case

* DevOps and SRE teams producing terminal screencasts
* Technical educators generating step-by-step CLI tutorials
* Documentation teams integrating vector terminals into Hugo or MkDocs

---

## Architecture

| Stage    | Tool(s)              | Input             | Output                      |
| -------- | -------------------- | ----------------- | --------------------------- |
| Record   | `asciinema`          | CLI session       | `.cast` file                |
| Simulate | `simulate-typing.py` | raw `.cast`       | guru `.cast`, clean `.cast` |
| Render   | `svg-term`, `ffmpeg` | processed `.cast` | `.svg`, `.mp4`, `.mov`      |

---

## Machines Involved

### Machine 1 – Linux (e.g. Ubuntu Server)

* No graphical UI
* Used for real-time CLI recordings with `asciinema`

### Machine 2 – Windows 11 with WSL2 (Ubuntu)

* Used for editing, simulating, and rendering output
* Recommended tools: VSCode, Python, Node.js, ffmpeg

---

## Documentation

### 🔹 Core Pipeline

* [01 – Recording Terminal Sessions](./docs/01-recording-terminal-sessions.md)
* [02 – Simulate Typing and Optimize](./docs/02-simulate-typing-and-optimize.md)
* [03 – Style and Render Output](./docs/03-style-and-render-output.md)

### 🔹 Appendix

* [Coloring and Standards](./docs/appendix-coloring-and-standards.md)

---

## Quickstart

```bash
# Machine 1 (Linux Server)
sudo apt install asciinema
asciinema rec ./demo.cast

# Machine 2 (WSL2 Ubuntu)
python3 scripts/simulate-typing.py --input demo.cast --output guru.cast
npx svg-term-cli --in guru.cast --out demo.svg
```

---

## License

MIT

## Authors

Maintained by the terminal-video project team.
