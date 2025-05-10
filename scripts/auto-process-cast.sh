#!/usr/bin/env bash
# auto-process-cast.sh
# End-to-end automation for processing a .cast file into .svg, .mp4, and .mov

set -euo pipefail

INPUT="$1"  # path to raw .cast file
BASENAME=$(basename "$INPUT" .cast)
PROCESSED="assets/processed/${BASENAME}.cast"
SVG="assets/visuals/${BASENAME}.svg"
MP4="assets/captures/${BASENAME}.mp4"
MOV="assets/captures/${BASENAME}.mov"

# Check tools
for cmd in python3 ffmpeg svg-term asciinema; do
  command -v $cmd >/dev/null 2>&1 || {
    echo "Error: $cmd is not installed." >&2
    exit 1
  }
done

echo "[1/5] Simulating human typing..."
python3 scripts/simulate-typing.py "$INPUT" > "$PROCESSED"

echo "[2/5] Applying guru-level enhancements..."
python3 scripts/simulate-guru-extended.py "$PROCESSED" > "$PROCESSED.tmp" && mv "$PROCESSED.tmp" "$PROCESSED"

echo "[3/5] Generating SVG via svg-term-cli..."
svg-term --in "$PROCESSED" --out "$SVG" --window --padding 10 --no-cursor --frame --theme "dracula"

echo "[4/5] Rendering MP4..."
ffmpeg -y -loop 1 -i "$SVG" -c:v libx264 -t 10 -pix_fmt yuv420p "$MP4"

echo "[5/5] Generating transparent MOV overlay..."
bash scripts/generate-terminal-overlay.sh "$PROCESSED" "$MOV"

echo "✅ All outputs generated:"
echo " - $PROCESSED"
echo " - $SVG"
echo " - $MP4"
echo " - $MOV"
