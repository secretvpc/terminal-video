# Environment Setup for WSL (Windows 11 + Ubuntu)

This guide describes the recommended environment setup for post-processing `.cast` recordings under Windows 11 using WSL2 (Ubuntu), VScode, and supporting tools.

---

## 🧱 System Requirements

- **Host OS**: Windows 11 (64-bit)
- **WSL Version**: WSL2 with Ubuntu 22.04
- **Recommended Shell**: bash or zsh
- **Text Editor**: VSCode with WSL Remote extension

---

## 📦 Required Packages (inside WSL)

Run the following commands in WSL Ubuntu:

```bash
sudo apt update
sudo apt install asciinema python3-pip ffmpeg git
pip3 install rich
npm install -g svg-term-cli
