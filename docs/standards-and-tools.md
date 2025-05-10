# Standards and Tooling Landscape for Terminal Video Production

This document surveys existing standards, tools, and projects that inform the design of the `terminal-video` pipeline. It aims to align with best practices, leverage open-source tools, and avoid unnecessary reinvention.

---

## 🎞️ Cast Recording: `asciinema`

- **Standard format**: JSON-based `.cast` (v2) with timestamps
- **Advantages**:
  - Open and portable
  - CLI-native
  - Excellent for headless environments
- **Alternatives**:
  - `ttyrec`, `termrec`, `script` (less portable, harder to post-process)

**Recommendation**: ✅ continue using `asciinema` as canonical input format.

---

## 🖼 Cast-to-Image: `svg-term-cli`

- Converts `.cast` files into `SVG` terminal renderings
- Maintains timing and color fidelity
- Supports themes: `dracula`, `nord`, `solarized-dark`, etc.
- Node.js-based, CLI-friendly

**Limitations**:
- No audio support
- Not optimized for large terminal dimensions

**Alternatives**:
- `svg-term` (browser-based)
- `asciicast2gif` (generates gifs, not vector-friendly)

**Recommendation**: ✅ keep `svg-term-cli` as default image renderer.

---

## 🎥 Video Encoding: `ffmpeg`

- Supports `.svg` to `.mp4` via rasterization
- Optional: create `.mov` with ProRes + alpha transparency for overlays
- Requires font embedding + fixed resolution for quality

**Key Flags**:
- `-filter_complex` for background transparency
- `-profile:v 3` for ProRes compatibility

**Recommendation**: ✅ retain `ffmpeg` as final step, with shell wrappers.

---

## 🧠 Simulation Layer

- `simulate-typing.py`: adds human-like typing pauses
- `simulate-guru.py`: adds tab-completion, error simulation, etc.

**Future Enhancements**:
- Probabilistic delays
- Error + correction realism
- Typing profiles (fast/dev/slow/etc.)

---

## 🧪 Comparative Projects

| Project              | Domain              | Remarks                                     |
|----------------------|---------------------|---------------------------------------------|
| `asciinema-player`   | Web playback        | Good for embed, not for offline rendering   |
| `asciicast2gif`      | GIF export          | Lacks transparency + vector fidelity        |
| `vhs` by charm.sh    | Go-based recorder   | Innovative, closed ecosystem, less flexible |

---

## ✅ Summary Recommendations

| Layer             | Chosen Tool          | Justification                              |
|------------------|----------------------|---------------------------------------------|
| Capture           | `asciinema`          | Portable, open, CLI-friendly                |
| Visualization     | `svg-term-cli`       | Vector-friendly, scriptable                 |
| Encoding          | `ffmpeg`             | Widely supported, performant                |
| Simulation        | Python (custom)      | Flexible, extendable, human control         |

---

## 📚 References

- https://github.com/asciinema/asciinema
- https://github.com/marionebl/svg-term-cli
- https://ffmpeg.org
- https://github.com/charmbracelet/vhs
