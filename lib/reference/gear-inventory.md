---
id: gear-inventory
aliases:
  - Gear Inventory
  - Hardware Inventory
tags: []
created: 2025-07-08
topic: systems
type: REFERENCE
---

# ASKIROM GEAR INVENTORY

> Updated for PKM-OS v3.0 - Simplified System  
> Focus: Everything is a file · Descriptive naming · Embedded task management  
> Last Updated: 2025-07-14

## Hardware

| Device                      | Code                | Acquired | Status | Notes             |
| --------------------------- | ------------------- | -------- | ------ | ----------------- |
| MacBook Pro M1 16"          | askr-mac-211020     | 2021-10  | Active | Main workstation  |
| iPhone 15 Pro Max           | askr-iphone-230920  | 2023-09  | Active |                   |
| iPad Pro 4th gen            | askr-ipad-240520    | 2024-05  | Active |                   |
| AirPods Pro 2               | askr-airpods-200320 | 2020-03  | Active |                   |
| SoundBlaster G8             | askr-g8-250320      | 2025-03  | Active | Audio interface   |
| Mangird Tea Pro             | askr-teapro-250320  | 2025-03  | Active | IEMs              |
| Garmin Fenix 8              | askr-fenix-240820   | 2024-08  | Active | Biometric monitor |
| Logitech MX Machanical Mini | askr-keyboard-2507  | —        | Active | Desktop input     |
| Logitech MX Anywhere 3s     | askr-mouse-2507     | —        | Active | Precision nav     |
| Steam Deck with CachyOS     | askr-deck-2506      | —        | Active | Linux / gaming    |
| PS5                         | askr-ps5-201120     | 2020-11  | Active | Gaming            |
| Xbox Series X               | askr-xsx-201120     | 2020-11  | Active | Gaming            |

## Software & Services

| Service           | Code                | Acquired | License    | Status | Renewal    |
| ----------------- | ------------------- | -------- | ---------- | ------ | ---------- |
| Obsidian Vault    | askr-vault-250620   | 2025-06  | Free       | Active | —          |
| Obsidian Sync     | askr-obssync-250620 | 2025-06  | $48/year   | Active | 30.06.2026 |
| 1Password         | askr-passwords-2503 | 2025-03  | 57€/year   | Active | 22.04.2026 |
| Obsidian Tasks    | askr-tasks-250720   | 2025-07  | Free       | Active | -          |
| Fastmail Services | askr-mail-250420    | 2025-05  | 58€/year   | Active | 04.05.2028 |
| iCloud Drive      | askr-cloud-211020   | 2021-10  | 200GB Plan | Active | Monthly    |

## Application Stack

### Personal Stack (macOS)

| Function         | Application           | Rationale                                                                        |
| ---------------- | --------------------- | -------------------------------------------------------------------------------- |
| Email & Calendar | Fastmail Web App      | Native client. Superior architecture (JMAP) & full integration                   |
| Notes & PKM      | Obsidian              | Core "file system" and "memory" of the PKM-OS. Entity-based project organization |
| Tasks & Schedule | Obsidian Tasks Plugin | External Scheduler (Layer 4).                                                    |
| Browser          | Firefox               | Openness and freedom of usage on all plattforms                                  |
| Passwords        | 1Password             | Best-in-class credential manager                                                 |

### Work Stack (macOS)

| Function         | Application            | Rationale                                                  |
| ---------------- | ---------------------- | ---------------------------------------------------------- |
| Email & Calendar | Microsoft Outlook      | Native M365 client. Keeps work context fully sandboxed     |
| Chat & Meetings  | Microsoft Teams        | Fully integrated client for work environment               |
| Browser          | Firefox (Work Profile) | Sandbox for work-related web activity via browser profiles |
| Office           | MS Office 365          | forced by employer                                         |

### Mobile Stack (iOS/iPadOS)

| Function         | Application           | Rationale                                            |
| ---------------- | --------------------- | ---------------------------------------------------- |
| Email & Calendar | Fastmail App          | Unified, native. Prevents context mixing             |
| Work Email       | Outlook App           | Native client for M365. Keeps work context sandboxed |
| Notes & PKM      | Obsidian              | Mobile vault access via Obsidian Sync                |
| Tasks & Schedule | Obsidian Tasks Plugin | Full mobile access                                   |
| Browser          | Firefox App           | Consistent secure browsing across platforms          |
| Passwords        | 1Password             | Cross-platform credential access                     |

## Utility Apps

| Function | Application                | Rationale                                                                                       |
| -------- | -------------------------- | ----------------------------------------------------------------------------------------------- |
| Terminal | Kitty (or Wezterm)         | same config and installation on all plattforms                                                  |
| Editor   | Neovim (considering Emacs) | feels the most reliable and also because of the hype maybe more plugins and problems get solved |
| Shell    | zsh                        | compatibility with scripting                                                                    |
| VPN      | Mullvad                    |                                                                                                 |
| Banking  | C24                        | Mobile only                                                                                     |

# Considerations

- Syncthing or Git integration on mobile(as native as could be)
- if swapping to EMACS then mobile orgmode
