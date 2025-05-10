# 01 – Recording Terminal Sessions with asciinema

## Overview

This guide outlines how to capture high-quality terminal sessions using `asciinema` in a headless Linux environment (e.g. Ubuntu Server), suitable for professional video production workflows. The focus is on maximizing terminal resolution, color fidelity, and reproducibility.

---

## Target Environment

**Machine 1: Linux-based CLI-only server**
Example: Ubuntu 22.04 LTS (no graphical UI)

### Required Tools

* `asciinema`
* `stty`, `tput`
* Terminal emulator settings (optional: `tmux`)

Install asciinema:

```bash
sudo apt update && sudo apt install asciinema
```

---

## Step-by-Step Recording Procedure

### 1. Setup Terminal Environment

```bash
# Ensure maximum lines and columns
stty cols 160 rows 48

# Optional: configure your shell prompt
export PS1="\u@\h:\w\$ "
```

### 2. Calibrate terminal colors

Use `dircolors` and `LS_COLORS` to define semantic highlighting:

```bash
eval $(dircolors -b)
export LS_COLORS="$LS_COLORS:di=1;34:fi=0:ln=36"
```

Preview effect with:

```bash
ls --color=auto
```

### 3. Start asciinema session

```bash
asciinema rec -i 2 -c "bash" ./demo.cast
```

Flags:

* `-i 2` sets idle time limit to 2s
* `-c` wraps bash inside

### 4. Run your CLI workflow

Execute all relevant steps (e.g. kubectl, docker, system commands).

### 5. End session

Press `Ctrl+D` or type `exit`

---

## Best Practices

* Always test screen size with `tput cols && tput lines`
* Use a clean prompt and hide unnecessary system output
* Prefer monospaced fonts when previewing in browser or video tools

---

## Output

* File: `demo.cast`
* Format: JSON-based terminal event capture

Next step: proceed to [02 – Simulate Typing and Optimize](./02-simulate-typing-and-optimize.md)
