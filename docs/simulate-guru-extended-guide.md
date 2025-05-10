# 🧠 simulate-guru-extended.py – Advanced CLI Simulation for asciinema

This script extends the standard `.cast` post-processor to simulate advanced terminal behavior — mimicking a "Linux guru" using autocomplete (`Tab`), smart command entry, and advanced tools like Docker, Kubernetes, and Git.

---

## ✅ Supported Command Simulations

| Command Pattern         | Simulated Behavior                        |
|-------------------------|-------------------------------------------|
| `apt install ...`       | Types `apt ins`, then `Tab`, then `tall` |
| `git checkout main`     | Types `gco`, `Tab`, then ` checkout main` |
| `docker run ...`        | Uses `Tab` after `dock`, types full run   |
| `kubectl get pods`      | Autocomplete `kubectl` + `po` to `pods -A`|
| `kubeadm init ...`      | Types `kube`, `Tab`, then full init flags |
| `grep ...`              | Autocomplete `gr` to `grep`, then full cmd|

---

## 🛠️ Usage

```bash
./simulate-guru-extended.py input.cast output.cast
```

- `input.cast`: your original terminal session
- `output.cast`: enhanced version with realistic command flow

---

## 📦 Features

- Adds delays and timing to simulate keystrokes
- Injects `\t` to represent Tab completion
- Handles multiple known command patterns
- Preserves original `.cast` header

---

## 📽️ Playback Options

- Use `asciinema play output.cast` to preview
- Use `svg-term` + `ffmpeg` to render `.svg` / `.mp4`

---

## 💡 Example Output (Git)

```json
["0.10", "o", "g"],
["0.15", "o", "c"],
["0.20", "o", "o"],
["0.25", "o", "\t"],
["0.35", "o", " checkout main"],
["0.60", "o", "\r"]
```

---

_Last updated: 2025-05-07_