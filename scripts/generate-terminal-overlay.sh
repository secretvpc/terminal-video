#!/bin/bash
# generate-terminal-overlay.sh – asciinema ➜ transparent .mov overlay

CAST=$1
THEME=${2:-dracula}
FONT=${3:-"JetBrains Mono"}
DURATION=${4:-10}
FPS=${5:-30}

if [ -z "$CAST" ]; then
  echo "Usage: ./generate-terminal-overlay.sh <demo.cast> [theme] [font] [duration] [fps]"
  exit 1
fi

BASE=$(basename "$CAST" .cast)
SVG="${BASE}.svg"
PNG="frame01.png"
MOV="${BASE}-overlay.mov"

# Step 1: Generate SVG without background
svg-term --in "$CAST" --out "$SVG" --no-window --padding 20 --theme "$THEME" --font "$FONT"

# Step 2: Export PNG (single frame for now)
inkscape "$SVG" --export-type=png --export-filename="$PNG"

# Step 3: Convert to transparent video (ProRes 4444)
ffmpeg -loop 1 -i "$PNG" -c:v prores_ks -profile:v 4 -pix_fmt yuva444p10le -t "$DURATION" -r "$FPS" "$MOV"

echo "✔ Overlay video created: $MOV"