# 03 – Style and Render Output

## Overview

This document describes how to convert `.cast` terminal recordings into polished video or vector outputs. It focuses on styling, resolution, transparency, and post-production readiness for different use cases (vector, alpha-channel, full video).

---

## Target Output Types

| Format | Use Case                               | Features                               |
| ------ | -------------------------------------- | -------------------------------------- |
| `.svg` | Embeddable docs, lightweight tutorials | Vector-based, static or animated       |
| `.mp4` | Standard video publishing              | High compatibility, no transparency    |
| `.mov` | Post-production pipelines              | Alpha channel (transparency), editable |

---

## Step 1: Define Output Parameters

### Color Profile & Font

Customize using `configs/colors.json`, `fonts/`, or embedded CSS if exporting to HTML/SVG.

### Screen Geometry

Ensure consistent terminal resolution:

```bash
stty cols 160 rows 48
```

---

## Step 2: Render Tools

### Option A: `agg` + `svg-term`

```bash
npx svg-term-cli \
  --in assets/processed/demo-clean.cast \
  --out assets/processed/demo.svg \
  --window \
  --no-cursor \
  --profile Seti \
  --padding 20
```

### Option B: `asciinema-player` + screen capture

Run in browser:

```bash
asciinema-player demo-clean.cast > player.html
```

Capture using OBS, ffmpeg, or automated browser rendering (Puppeteer).

---

## Step 3: Convert to Video

### Using ffmpeg

```bash
ffmpeg -i demo.mov \
  -c:v libx264 -preset slow -crf 18 \
  -pix_fmt yuv420p demo.mp4
```

### Optional: Resize, Add Padding

```bash
ffmpeg -i demo.mp4 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" demo-padded.mp4
```

---

## Best Practices

* Maintain alpha-channel versions for editing workflows
* Use preset color/font schemes for brand consistency
* Avoid excessive length or idle time in final cut

---

Next: consult [appendix-coloring-and-standards.md](./appendix-coloring-and-standards.md) for theme and tooling options.
