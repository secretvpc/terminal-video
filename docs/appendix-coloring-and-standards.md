# Appendix – Coloring Schemes and Standards

## Overview

This appendix contains reference material on terminal color theming, directory colorization, and related tooling. It also outlines conventions for CLI session styling and popular tooling choices in terminal video workflows.

---

## Terminal Coloring

### `LS_COLORS`

Use environment variable to colorize output:

```bash
export LS_COLORS="di=1;34:fi=0:ln=36"
```

* `di=1;34` – directories in bold blue
* `ln=36` – symbolic links in cyan

Generate config:

```bash
dircolors -b > ~/.dircolors
```

### Preview Colors

```bash
ls --color=auto
```

Or use specialized visualizers like:

* `vivid` (Rust-based theme manager)
* `pygmentize`, `grc` for command wrapping

---

## Styling Standards

| Element       | Recommendation                        |
| ------------- | ------------------------------------- |
| Font          | Monospace (Fira Code, JetBrains Mono) |
| Shell prompt  | Clean, minimal PS1                    |
| Terminal size | ≥ 160x48 for HD output                |
| Cursor        | Hidden during export                  |

---

## Tools and Utilities

* **`svg-term-cli`** – export `.cast` to `.svg`
* **`asciinema-player`** – HTML player
* **`ffmpeg`** – final video rendering and editing
* **`Puppeteer`/`Playwright`** – browser automation for batch rendering

---

## Color Palettes

Popular themes:

* **Solarized Dark** – soft contrast, eye-friendly
* **Dracula** – saturated, high-impact
* **Monokai Pro** – modern look, high readability

Apply using:

```bash
npx svg-term-cli --profile Dracula
```

---

## Reference

* [LS\_COLORS Wiki](https://github.com/trapd00r/LS_COLORS)
* [asciinema docs](https://asciinema.org/docs)
* [svg-term-cli](https://github.com/marionebl/svg-term-cli)
