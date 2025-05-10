#!/bin/bash
# render-cast-wsl.sh – Render asciinema .cast file to .svg and .mp4 using svg-term + ffmpeg (WSL-compatible)

EP=$1
THEME=${2:-dracula}
FONT=${3:-"JetBrains Mono"}
DURATION=${4:-10}

if [ -z "$EP" ]; then
  echo "Usage: ./render-cast-wsl.sh <episode> [theme] [font] [duration]"
  exit 1
fi

INPUT="ep${EP}.cast"
SVG="ep${EP}.svg"
MP4="ep${EP}.mp4"

# Convert cast to svg
svg-term --in "$INPUT" --out "$SVG" --window --theme "$THEME" --font "$FONT"

# Convert svg to mp4
ffmpeg -loop 1 -i "$SVG" -t "$DURATION" -pix_fmt yuv420p "$MP4"

echo "✔ Rendered: $SVG and $MP4"