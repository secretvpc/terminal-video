# 🧠 simulate-typing.py – Simulate Human Typing in asciinema .cast Files

This script takes an asciinema `.cast` file and transforms "pasted" chunks of text into character-by-character events, mimicking the speed and rhythm of real human typing.

---

## 🧭 Purpose

`asciinema` records pasted blocks of text instantly. This can look unrealistic in playback. This tool simulates natural typing by breaking such blocks into single characters with small time delays.

---

## 🛠️ Usage

```bash
./simulate-typing.py input.cast output.cast
```

- `input.cast` – Original recording
- `output.cast` – Modified version with simulated typing

---

## ⚙️ Features

- Detects output (`"o"`) events longer than one character
- Splits them into single characters
- Adds delay between characters (`~50ms` by default)
- Keeps header and metadata unchanged

---

## 📦 Output Example

### Before

```json
["0.10", "o", "echo Hello world"]
```

### After

```json
["0.10", "o", "e"],
["0.15", "o", "c"],
["0.20", "o", "h"],
["0.25", "o", "o"],
["0.30", "o", " "],
...
```

---

## 📘 Use Cases

- More natural playback for demos/tutorials
- Better flow in `svg-term` / `.mp4` renders
- Avoid "instant text" from pasted blocks

---

_Last updated: 2025-05-07_