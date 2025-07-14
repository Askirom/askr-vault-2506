---
type: REFERENCE
topic: systems
aliases: ["Gear Inventory", "Hardware Inventory"]
created: 2025-07-08
---

# ASKIROM GEAR INVENTORY

> Updated for PKM-OS v3.0 - Simplified System  
> Focus: Everything is a file · Descriptive naming · Embedded task management  
> Last Updated: 2025-07-14

## Hardware

| Device                 | Code                | Acquired | Status | Notes             |
| ---------------------- | ------------------- | -------- | ------ | ----------------- |
| MacBook Pro M1 16"     | askr-mac-211020     | 2021-10  | Active | Main workstation  |
| iPhone 15 Pro Max      | askr-iphone-230920  | 2023-09  | Active |                   |
| iPad Pro 4th gen       | askr-ipad-240520    | 2024-05  | Active |                   |
| AirPods Pro 2          | askr-airpods-200320 | 2020-03  | Active |                   |
| SoundBlaster G8        | askr-g8-250320      | 2025-03  | Active | Audio interface   |
| Mangird Tea Pro        | askr-teapro-250320  | 2025-03  | Active | IEMs              |
| Garmin Fenix 8         | askr-fenix-240820   | 2024-08  | Active | Biometric monitor |
| Magic Keyboard TouchID | askr-keyboard-2405  | —        | Active | Desktop input     |
| Magic Trackpad         | askr-trackpad-2405  | —        | Active | Precision nav     |
| Steam Deck             | askr-deck-2506      | —        | Active | Linux / gaming    |
| PS5                    | askr-ps5-201120     | 2020-11  | Active | Gaming            |
| Xbox Series X          | askr-xsx-201120     | 2020-11  | Active | Gaming            |

## Software & Services

| Service           | Code                | Acquired | License    | Status | Renewal    |
| ----------------- | ------------------- | -------- | ---------- | ------ | ---------- |
| Obsidian Vault    | askr-vault-250620   | 2025-06  | Free       | Active | —          |
| Obsidian Sync     | askr-obssync-250620 | 2025-06  | $48/year   | Active | 30.06.2026 |
| 1Password         | askr-passwords-2503 | 2025-03  | 57€/year   | Active | 22.04.2026 |
| Todoist Pro       | askr-todoist-250720 | 2025-07  | ~48€/year  | Active | July 2026  |
| Fastmail Services | askr-mail-250420    | 2025-05  | 58€/year   | Active | 04.05.2028 |
| iCloud Drive      | askr-cloud-211020   | 2021-10  | 200GB Plan | Active | Monthly    |
| Time Machine      | askr-backup-211020  | 2021-10  | Free       | Active | —          |

## Application Stack

### Personal Stack (macOS)

| Function         | Application      | Rationale                                                                        |
| ---------------- | ---------------- | -------------------------------------------------------------------------------- |
| Email & Calendar | Fastmail Web App | Native client. Superior architecture (JMAP) & full integration                   |
| Notes & PKM      | Obsidian         | Core "file system" and "memory" of the PKM-OS. Entity-based project organization |
| Tasks & Schedule | Todoist          | External Scheduler (Layer 4). Tasks managed outside vault to prevent complexity  |
| Browser          | Brave            | Superior security (sandbox) + built-in privacy                                   |
| Passwords        | 1Password        | Best-in-class credential manager                                                 |

### Work Stack (macOS)

| Function         | Application          | Rationale                                                  |
| ---------------- | -------------------- | ---------------------------------------------------------- |
| Email & Calendar | Microsoft Outlook    | Native M365 client. Keeps work context fully sandboxed     |
| Chat & Meetings  | Microsoft Teams      | Fully integrated client for work environment               |
| Browser          | Brave (Work Profile) | Sandbox for work-related web activity via browser profiles |

### Mobile Stack (iOS/iPadOS)

| Function         | Application  | Rationale                                            |
| ---------------- | ------------ | ---------------------------------------------------- |
| Email & Calendar | Fastmail App | Unified, native. Prevents context mixing             |
| Work Email       | Outlook App  | Native client for M365. Keeps work context sandboxed |
| Notes & PKM      | Obsidian     | Mobile vault access via Obsidian Sync                |
| Tasks & Schedule | Todoist App  | Full mobile access + robust notifications            |
| Browser          | Brave App    | Consistent secure browsing across platforms          |
| Passwords        | 1Password    | Cross-platform credential access                     |
