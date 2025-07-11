---
id: Personal-Knowledge-OS
aliases: []
tags: []
type: system
---

# PKM-OS: Design & Operations Manual

**Version 2.0 (Final)**
**Last updated:** 2025-07-11

_This revision fully adopts the "Everything is a file" philosophy and a `systemd`-based management layer for maximum resilience and productivity._

---

## 0 · Core Philosophy: "Everything is a File"

This system rigorously applies the Unix philosophy that everything can be represented as a file. Processes, states, external services, and tasks are all exposed as file-like objects on disk. This approach ensures uniform tooling (`grep`, `find`, `git`), zero vendor lock-in, and provides perfect clarity and reviewability for all past work.

---

## 1 · Core Analogy: `systemd`

The system's operational logic is modeled on **`systemd`**, the Linux init system. The projects and responsibilities are treated as **units** with a defined lifecycle, dependencies, and resource constraints. This provides a robust vocabulary for managing work.

| **`systemd` Concept** | **PKM-OS Analogue**                                   | **Purpose**                                                  |
| :-------------------- | :---------------------------------------------------- | :----------------------------------------------------------- |
| **Unit**              | A project, task, or responsibility                    | The fundamental object of work, defined in a `.md` file.     |
| **Service**           | An ongoing responsibility (e.g., "Maintain finances") | A unit with no defined end date.                             |
| **Timer**             | A recurring task (e.g., "Weekly review")              | A unit triggered by a schedule.                              |
| **Slice**             | A category of effort (e.g., `work`, `personal`)       | A mechanism for grouping units to enforce WIP limits.        |
| **Dependency**        | `Requires` / `Wants` fields                           | Explicitly maps the relationships between units for clarity. |

---

## 2 · Instruction Set (Primitives)

These are the fundamental, logged actions performed on a unit.

- **DRAFT · REVIEW · COMMUNICATE · PLAN · DECIDE · MAINTAIN**

---

## 3 · System Call (Log Entry)

All work on a unit is logged in its file using this append-only format.

```
[YYYY-MM-DD HH:MM] – PRIMITIVE (Optional Actor): Message
```

---

## 4 · Unit File (The Core Object)

Every project or responsibility is a single `.md` file with a UID filename (e.g., `202507111600.md`) and the following YAML front-matter.

```yaml
---
# [Unit]
uid: 202507111600
description: "Finalize PKM-OS v2.0 Manual"
aliases: ["pkmos-v2-manual"]
kind: project         # project | service | timer
status: active       # defined | enabled | active | inactive | archived
slice: productivity # work | personal | learning | etc.

# [Dependencies]
requires: []          # Hard dependencies (list of UIDs)
wants: []             # Soft dependencies (list of UIDs)
---

# [[202507111600|Finalize PKM-OS v2.0 Manual]]

**Goal:** Publish the final, unified v2.0 operations manual.
**Due Date:** 2025-07-11

---

### Action Log

- [2025-07-11 16:00] – DRAFT: Assembled all components into the final v2.0 note.
```

---

## 5 · File-System Layer (The Architecture)

The directory structure is inspired by the FHS and built to support the file-only philosophy.

```
/
├── etc/                      # System configuration
│   ├── templates/            #   project-template.md, daily-template.md
│   └── workflows/            #   Standard operating procedures
├── var/                      # Active workspace & volatile data
│   ├── spool.md              # System inbox (FIFO pipe)
│   ├── lib/                  # State files from external services
│   │   ├── todoist/
│   │   │   └── state.json    #   Persistent mirror of tasks
│   │   └── calendar/         #   Directory for mirrored .ics events
│   ├── log/                  # Daily & meeting logs
│   └── units/                # Active projects & services
├── lib/                      # Reference knowledge library
└── archive/                  # Completed units and old logs
```

---

## 6 · Naming Conventions

System constants are `UPPERCASE`; user data is `lowercase`.

- **Primitives**: `DRAFT`, `REVIEW`, `DECIDE`
- **Unit `status`**: `ACTIVE`, `INACTIVE`, `ARCHIVED`
- **Unit `kind`**: `PROJECT`, `SERVICE`, `TIMER`
- **Unit `slice`**: `PROFESSIONAL`, `PERSONAL`
- **File Aliases**: `["acme q3 audit"]`
- **File Names**: `202507111600.md`, `2025-07-11.md`

---

## 7 · Core Workflow (The Lifecycle)

1.  **Capture:** Append a line to `/var/spool.md`.
2.  **Promote:** A nightly `cron` script reads `spool.md` and promotes each line to its correct file type (e.g., a new task in `todoist/state.json`, a new `.ics` file in `calendar/`, or a new unit file in `/var/lib/units/`).
3.  **Plan:** Consult the `/var/lib/todoist/state.json` file (or its frontend app) to select a focus task, respecting WIP limits enforced by a filter.
4.  **Execute:** Open the corresponding unit file via its UID.
5.  **Log:** Add a `PRIMITIVE` line to the unit file's action log.
6.  **Commit:** A daily script commits all changes in the vault to `git`, creating an atomic snapshot of the system's state.
7.  **Archive:** When a unit's `status` is set to `inactive`, a weekly review process moves the file from `/var/lib/units/` to `/archive/`.

---

## 8 · Service Integration

External services like Todoist and Calendar are not primary citizens. They are treated as frontends to their mirrored state files in `/var/lib/`. A script periodically syncs the service state to the local file, ensuring the file on disk is the canonical source for system tools.

---

### Appendix A · Quick-Start Checklist

- Create the directory tree exactly as specified in Section 5.
- Configure Obsidian's _Templates_ plugin to use files from `/etc/templates/`.
- Pin `/var/spool.md` and map a hotkey for quick-append.
- Create a master filter in your task manager to enforce WIP limits (e.g., `(@doing | @focus)`).
- Set up sync scripts to mirror external services to `/var/lib/`.
- Run the system manually for two weeks before automating promotion or archival steps.
