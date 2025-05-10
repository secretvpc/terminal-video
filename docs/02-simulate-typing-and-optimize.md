# 02 – Simulate Typing and Optimize .cast Files

## Overview

This guide covers the post-processing of `.cast` recordings to simulate human typing behavior and optimize them for video rendering. We use Python-based tools to adjust timing, improve flow, and prepare the file for stylistic enhancements.

---

## Target Environment

**Machine 2: Windows 11 + WSL2 with Ubuntu**
Example tools: VSCode, Python 3.10+, asciinema, jq

---

## Step 1: Transfer `.cast` File

Copy from Machine 1:

```bash
scp user@host:/path/to/demo.cast ./assets/raw/demo.cast
```

Or move from shared folder:

```bash
cp /mnt/c/Users/yourname/demo.cast ./assets/raw/demo.cast
```

---

## Step 2: Simulate Human Typing (Guru Mode)

### Tool: `simulate-typing.py`

Custom Python script to inject pauses and typing cadence.

#### Example usage:

```bash
python3 scripts/simulate-typing.py \
  --input ./assets/raw/demo.cast \
  --output ./assets/processed/demo-guru.cast \
  --style guru \
  --min-delay 0.03 \
  --max-delay 0.25
```

### Flags explained:

* `--style guru` – advanced behavior modeling
* `--min-delay`, `--max-delay` – simulate finger speed variation

---

## Step 3: Trim & Clean Events

### Remove unnecessary delays:

```bash
python3 scripts/clean-cast.py --input demo-guru.cast --output demo-clean.cast
```

### Optional: Visual verify

```bash
asciinema play demo-clean.cast
```

---

## Step 4: Output Staging

All final `.cast` files should be staged in:

```
assets/processed/
```

* `*-guru.cast` → simulated typing
* `*-clean.cast` → trimmed + validated

---

## Best Practices

* Validate timing flow visually before exporting to video
* Maintain raw `.cast` files unchanged
* Document simulation params used for reproducibility

---

Next: proceed to [03 – Style and Render Output](./03-style-and-render-output.md)
