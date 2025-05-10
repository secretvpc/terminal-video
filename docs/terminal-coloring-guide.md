# 🎨 Terminal File Type Coloring Guide

This document explains how terminal file types get colored using `LS_COLORS`, `dircolors`, and modern tools like `exa` or `lsd`. It also includes ANSI codes and `.cast` compatibility.

---

## 🧪 What Controls File Colors in Terminal?

### 1. `LS_COLORS` Environment Variable

This variable maps file extensions or types to ANSI color codes.

```bash
echo $LS_COLORS
```

### 2. `dircolors` File

This is a configuration file that feeds into `LS_COLORS`. You can generate and customize one:

```bash
dircolors -p > ~/.dircolors
```

Edit entries like:

```text
*.sh=01;32
*.md=01;36
*.jpg=01;35
*.py=01;34
```
Then activate:

```bash
eval "$(dircolors -b ~/.dircolors)"
```

---

## ✅ Modern Alternatives

### `exa`

```bash
exa --color=always --icons
```

- Colors by file type
- Icons with Nerd Fonts

### `lsd`

- Like `exa`, often faster
- Good for use in scripts or `asciinema`

---

## 🎨 Common ANSI Color Codes

| Code   | Color       | Usage                        |
|--------|-------------|------------------------------|
| 01;31  | Bold Red    | Executables, `.bin`          |
| 01;32  | Bold Green  | Scripts, `.sh`               |
| 01;36  | Cyan        | Markdown, `.md`              |
| 01;34  | Blue        | Code, `.py`, `.c`, `.cpp`    |
| 01;35  | Magenta     | Media, `.jpg`, `.mp3`        |

---

## 🖥️ Terminal Settings Matter

Use a 256-color or truecolor compatible terminal (e.g., Windows Terminal, Kitty, Alacritty). Fonts should be monospaced like:

- Fira Code
- JetBrains Mono
- Ubuntu Mono

---

## 🧾 Color in asciinema Recordings

To preserve file colors in `asciinema`:

1. Use color-friendly tools: `exa`, `bat`, `lsd`
2. Ensure terminal supports ANSI codes
3. Run commands with `--color=always`

```bash
exa --color=always -l
bat README.md
```

---

_Last updated: 2025-05-07_