---
id: gear-askirom-inventory-v2506
aliases: []
tags: []
created: 2025-07-08
type: moc
---

# ASKIROM GEAR INVENTORY (PKM-OS Aligned)

> Updated for PKM-OS v1.0 - Entity-Based System  
> Focus: Architectural integrity · Entity-driven organization · Frictionless workflows  
> Last Updated: 2025-07-09

## Hardware

| Device                 | Code                | Acquired | Status | Notes            |
| ---------------------- | ------------------- | -------- | ------ | ---------------- |
| MacBook Pro M1 16"     | Askr.Mac-211020     | 2021-10  | Active | Main workstation |
| iPhone 15 Pro Max      | Askr.iPhone-230920  | 2023-09  | Active |                  |
| iPad Pro 4th gen       | Askr.iPad-240520    | 2024-05  | Active |                  |
| AirPods Pro 2          | Askr.AirPods-200320 | 2020-03  | Active |                  |
| SoundBlaster G8        | Askr.G8-250320      | 2025-03  | Active | Audio interface  |
| Mangird Tea Pro        | Askr.TeaPro-250320  | 2025-03  | Active | IEMs             |
| Garmin Fenix 8         | Askr.Fenix-240820   | 2024-08  | Active | Biometric monitor |
| Magic Keyboard TouchID | Askr.Keyboard-2405  | —        | Active | Desktop input    |
| Magic Trackpad         | Askr.Trackpad-2405  | —        | Active | Precision nav    |
| Steam Deck             | Askr.Deck-2506      | —        | Active | Linux / gaming   |
| PS5                    | Askr.PS5-201120     | 2020-11  | Active | Gaming           |
| Xbox Series X          | Askr.XSX-201120     | 2020-11  | Active | Gaming           |

## Software & Services

| Service           | Code                | Acquired | License    | Status | Renewal    |
| ----------------- | ------------------- | -------- | ---------- | ------ | ---------- |
| Obsidian Vault    | Askr.Vault-250620   | 2025-06  | Free       | Active | —          |
| Obsidian Sync     | Askr.ObsSync-250620 | 2025-06  | $48/year   | Active | 30.06.2026 |
| 1Password         | Askr.Passwords-2503 | 2025-03  | 57€/year   | Active | 22.04.2026 |
| Todoist Pro       | Askr.Todoist-250720 | 2025-07  | ~48€/year  | Active | July 2026  |
| Fastmail Services | Askr.Mail-250420    | 2025-05  | 58€/year   | Active | 04.05.2028 |
| iCloud Drive      | Askr.Cloud-211020   | 2021-10  | 200GB Plan | Active | Monthly    |
| Time Machine      | Askr.Backup-211020  | 2021-10  | Free       | Active | —          |

## Application Stack

### Personal Stack (macOS)

| Function         | Application      | Rationale                                                      |
| ---------------- | ---------------- | -------------------------------------------------------------- |
| Email & Calendar | Fastmail Web App | Native client. Superior architecture (JMAP) & full integration |
| Notes & PKM      | Obsidian         | Core "file system" and "memory" of the PKM-OS. Entity-based project organization |
| Tasks & Schedule | Todoist          | External Scheduler (Layer 4). Tasks managed outside vault to prevent complexity |
| Browser          | Brave            | Superior security (sandbox) + built-in privacy                 |
| Passwords        | 1Password        | Best-in-class credential manager                               |

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

## PKM-OS Architecture Overview

### Core Directory Structure

```
/
├── var/proc/        # Active projects organized by entity + descriptive name
├── var/log/dly/     # Daily action logs using PKM-OS format
├── var/inb/         # Inbox for unprocessed items
├── lib/            # Reference materials by context
├── sys/            # Templates, maps, and system files
├── tmp/            # Temporary scratchpad files
└── archive/        # Completed projects and cold storage
```

### Entity-Based Naming Convention

**Format**: `[ENTITY-CODE]-[descriptive-name]`

#### Entity Types:
- **Business Clients**: ARA, CLIFO, EHFREI, EKIBA, EMPIC, FDFRI, FITS, GOSME, INSTO, RBOMN, RCG, SECUD, SOLVE, VEDES, VGALT
- **Personal Self**: PERSONAL (self-initiated projects)
- **External Interruptors**: INSURANCE, APPLE, GOVERNMENT, BANK
- **Relationship Entities**: HIVE, GF, FAMILY, FRIEND
- **Network Organizations**: BVD, MAIBAUM, NETWORK

### PKM-OS Log Entry Format

**Standard Format**: `[YYYY-MM-DD HH:MM] - PRIMITIVE (Optional Entity): Message`

**Primitives**: DRAFT, REVIEW, COMMUNICATE, PLAN, DECIDE

### Active Templates

| Template | Purpose | Alignment |
|----------|---------|-----------|
| `tpl-daily-log.md` | Daily action logging with PKM-OS format | ✅ Updated |
| `tpl-project-client.md` | Entity-based project template | ✅ Updated |
| `tpl-meeting-notes.md` | Structured meeting documentation | ✅ New |
| `tpl-entity-profile.md` | Entity relationship management | ✅ New |
| `tpl-reference.md` | Reference note template | ✅ Maintained |
| `tpl-person.md` | Person contact template | ✅ Maintained |
| `tpl-moc.md` | Map of Content template | ✅ Maintained |

### Integration Points

- **External Task Management**: Todoist with Obsidian URL links
- **File Organization**: Metadata-driven filing using YAML frontmatter
- **Entity Tracking**: Comprehensive entity profiles for all input sources
- **Action Logging**: Standardized log format across all project files
