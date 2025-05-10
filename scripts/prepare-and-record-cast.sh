#!/bin/bash
# prepare-and-record-cast.sh – Setup colors + record asciinema session (Linux headless)

CAST_NAME=${1:-demo}

echo "📦 Installing tools if missing..."
sudo apt update
sudo apt install -y asciinema exa bat coreutils

echo "🎨 Setting up LS_COLORS and aliases..."
# Generate .dircolors if missing
if [ ! -f ~/.dircolors ]; then
  dircolors -p > ~/.dircolors
fi

# Activate dircolors in shell
if ! grep -q 'dircolors' ~/.bashrc; then
  echo 'eval "$(dircolors -b ~/.dircolors)"' >> ~/.bashrc
  echo 'alias ls="ls --color=always"' >> ~/.bashrc
  echo 'alias exa="exa --color=always"' >> ~/.bashrc
  echo 'alias bat="bat --color=always"' >> ~/.bashrc
fi

source ~/.bashrc

echo "🧪 Starting asciinema recording: ${CAST_NAME}.cast"
asciinema rec "${CAST_NAME}.cast"