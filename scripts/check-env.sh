#!/usr/bin/env bash
# check-env.sh
# Check for required tools and directories for terminal-video pipeline

set -euo pipefail

REQUIRED_CMDS=("asciinema" "ffmpeg" "svg-term" "python3")
REQUIRED_DIRS=("assets/raw" "assets/processed" "assets/visuals" "assets/captures")

echo "🔍 Checking required commands..."
for cmd in "${REQUIRED_CMDS[@]}"; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "❌ Missing command: $cmd"
    MISSING=true
  else
    echo "✅ $cmd found"
  fi
done

echo
echo "📁 Checking required directories..."
for dir in "${REQUIRED_DIRS[@]}"; do
  if [[ ! -d "$dir" ]]; then
    echo "⚠️ Missing directory: $dir"
    mkdir -p "$dir"
    echo "🛠 Created: $dir"
  else
    echo "✅ $dir exists"
  fi
done

if [[ "${MISSING:-false}" == "true" ]]; then
  echo "❗ Environment check failed. Please install missing commands."
  exit 1
fi

echo
echo "✅ Environment check passed."
