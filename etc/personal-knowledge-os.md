---
id: Personal-Knowledge-OS
aliases: []
tags: []
type: system
---

# PKM-OS: Design & Operations Manual

**Version 1.2 (Draft)**  
**Last updated:** 2025-07-09

_This revision introduces pure UID-based content naming and a domain-based library structure._

## 0 · Core Analogy

| **Computer Resource** | **Human Equivalent** | **PKM-OS Component**                                            | **How It Reduces Load**                                      |
| --------------------- | -------------------- | --------------------------------------------------------------- | ------------------------------------------------------------ |
| **CPU**               | Attention / Focus    | **Scheduler** (Todoist) + **Interrupt Handler** (/var/spool.md) | Only one foreground task; distractions parked instantly.     |
| **RAM**               | Working Memory       | **Process Files** (/var/proc/…) + **Action Logs**               | Off-loads active state so the brain can think, not remember. |
| **Power**             | Will-/Energy         | Clear capture → triage → review loops                           | Fewer meta-decisions, lower stress = more stamina.           |

## 1 · Instruction Set (Primitives)

- **DRAFT · REVIEW · COMMUNICATE · PLAN · DECIDE · MAINTAIN**

## 2 · System Call (Log Entry)

```
[YYYY-MM-DD HH:MM] – PRIMITIVE (Optional Actor): Message
```

## 3 · Process File (Project Note)

```markdown
---
type: project
status: active
context:
uid: 202501091445
tags: []
---

# [[202501091445|Project Title]]

**Goal:**
**Due Date:**
**Stakeholders:**

---

### Action Log

- [{{date:YYYY-MM-DD}} {{time:HH:mm}}] – PRIMITIVE: …
```

## 4 · File-System Layer (FHS-Inspired)

```
/
├── etc/                    # System configuration
│   ├── templates/          #   project-template.md, daily-template.md
│   └── workflows/          #   Standard operating procedures
├── var/                    # Active workspace
│   ├── spool.md            #   System inbox file
│   ├── cache/              #   Generated navigation aids
│   │   └── maps/           #     System-generated MOCs
│   ├── log/                #   Activity logs
│   │   ├── daily/          #     2025-01-09.md, 2025-01-10.md
│   │   └── meetings/       #     202501091445.md, 202501091530.md
│   └── proc/               #   Active processes
├── lib/                    # Reference knowledge library
│   ├── cybersecurity/
│   ├── legal/
│   ├── finance/
│   ├── health/
│   ├── technology/
│   ├── people/
│   ├── productivity/
│   ├── gaming/
│   ├── software-licenses/
│   └── uncategorized/
└── archive/                # Completed processes and old logs
```

### 4.1 Pure UID Content System

- **Content files use UIDs**: `202501091445.md` (YYYYMMDDhhmm format)
- **Daily logs use dates**: `2025-01-09.md` (dates are natural stable identifiers)
- **System files use descriptive names**: `spool.md`, templates, workflows
- **Human readability via aliases**: `[[202501091445|Team Meeting Notes]]`
- **Chronological sorting**: Files/folders automatically sort by creation time
- **Stable references**: UIDs and dates never change, preventing broken links
- **Cross-context linking**: Information lives in one context, linked from others via `[[UID|alias]]`

### 4.2 Deterministic Filing Rules

| **Front-matter**                | **Destination**                                |
| ------------------------------- | ---------------------------------------------- |
| type: reference                 | lib/\<domain>/                                 |
| type: project status: active    | var/proc/\<uid>/                                |
| type: project status: completed | whole folder → archive/proc/\<uid>/            |
| type: daily_log                 | var/log/daily/                                 |
| type: template                  | etc/templates/                                 |

_(Automation optional; manual drag-drop is fine until it hurts ≥3×.)_

## 5 · Scheduler Integration

- Todoist (or equivalent) holds a **single priority queue**.
- Each task contains **UID-based deep link**: `obsidian://open?path=var/proc/professional/202501091445/`
- **Alias in task name**: "ACME Contract Review (202501091445)"
- Done → mark complete; if project ends, switch YAML to status: completed and archive during review.

## 6 · Naming Conventions

### 6.1 Client/Entity Code Standards

Following FHS principles, all client/entity codes use **lowercase** formatting:

- **Folder names**: `ara-gdpr-compliance-consulting/`
- **File aliases**: `["ara gdpr compliance consulting"]`
- **References**: Use `ara` not `ARA`
- **Exception**: System PRIMITIVES remain UPPERCASE (`DRAFT`, `REVIEW`, etc.)

This maintains consistency with UNIX/Linux conventions where directories and identifiers are lowercase.

## 7 · Core Workflow

1. **Schedule** – consult Todoist.
2. **Activate** – click UID-based deep link → Process File opens.
3. **Execute** – perform a Primitive.
4. **Log** – add a System Call line.
5. **File** – update YAML & move note if needed.
6. **Complete** – mark Todoist task done.

## Appendix A · Quick-Start Checklist

- Create top-level dirs exactly as tree above.
- Enable _Templates_ plugin; store them in /etc/templates/.
- Pin spool.md; map "Append to note" hot-key.
- Set Todoist filter to show only today's single top task.
- Configure UID generation (YYYYMMDDhhmm format).

_Run the system for two weeks before adding any automation scripts. Optimise only what breaks flow repeatedly._
