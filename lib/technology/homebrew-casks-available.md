---
kind: project
status: active
slice: personal
description: "Homebrew Casks Available"
aliases: ["homebrew-casks-available"]
requires: []
wants: []
uid: 202507102317
uuid: 202507102317
---

# Askirom's Complete System Brewfile
Command: 
```bash
ls /Applications | while read app; do`
  `echo "Checking: $app"`
  `brew search --cask "${app%.*}" 2>/dev/null || echo "  → Not available in Homebrew"`
done > ~/Desktop/brew_audit.txt
```

# Generated from audit - comprehensive software stack migration

# Essential taps
tap "1password/tap"]
tap "homebrew/cask"]
tap "homebrew/core"]

# CLI Tools (existing)
brew "guile"]
brew "p11-kit"]
brew "unbound"]
brew "gnutls"]
brew "cask"]
brew "python@3.10"]
brew "streamlink"]
brew "zsh-autosuggestions"]
brew "zsh-completions"]
brew "zsh-you-should-use"]
brew "zzz"]
brew "teamookla/speedtest/speedtest"]

# Security & Password Management
cask "1password"]
cask "1password-cli"]
cask "strongbox"]
cask "yubico-authenticator"]
cask "yubico-yubikey-manager"]

# Creative Suite
cask "affinity-designer"]
cask "affinity-photo"]
cask "affinity-publisher"]

# Development & Text Editors
cask "sublime-text"]
cask "sublime-merge"]
cask "iterm2"]

# Productivity & Organization
cask "obsidian"]
cask "todoist-app"]
cask "maccy"  # Clipboard manager
cask "alt-tab"  # Window switching
cask "raycast"  # Launcher

# Communication
cask "discord"]
cask "telegram"]
cask "signal"]
cask "whatsapp"]
cask "zoom"]

# Microsoft Office Suite
cask "microsoft-excel"]
cask "microsoft-word"]
cask "microsoft-powerpoint"]
cask "microsoft-outlook"]
cask "microsoft-onenote"]
cask "microsoft-teams"]

# Browsers
cask "firefox"]
cask "mullvad-browser"]
cask "tor-browser"]

# Media & Entertainment
cask "iina"  # Video player
cask "plex"]
cask "steam"]
cask "league-of-legends"]

# File Management & Utilities
cask "keka"  # Archive utility
cask "appcleaner"]
cask "daisydisk"]
cask "onedrive"]

# System Enhancement
cask "betterdisplay"]
cask "stats"  # System monitor
cask "steermouse"]
cask "steelseries-gg"]

# AI & Modern Tools
cask "claude"]
cask "chatgpt"]
cask "ollama"]

# Document & PDF
cask "pdf-expert"]
cask "naps2"]

# Virtualization
cask "parallels"]

# Cloud Storage & File Tools
cask "deepl"  # Translation
cask "textsniper"  # OCR
cask "cleanshot"  # Screenshots

# Financial & Banking
cask "moneymoney"]

# Specialized Tools
cask "beyond-compare"]
cask "latest"  # Update checker
cask "citrix-workspace"]
cask "mullvad-vpn"]
# Apps NOT available in Homebrew (keep manual):
# - 2FAS - Two Factor Authentication
# - CARROTweather
# - Canary Mail
# - GPG Keychain
# - Logic Pro
# - Perplexity
# - Things3
# - MindNode Next
# - Working Hours
# - Simple Color Palette
# - Riot Client
# - Various German tax software (SteuerMac)

# Installation Instructions:
# 1. Save this as "Brewfile" in your home directory
# 2. Run: brew bundle install
# 3. Manually uninstall apps that are now managed by Homebrew
# 4. For clean future setups: brew bundle install --file=Brewfile
