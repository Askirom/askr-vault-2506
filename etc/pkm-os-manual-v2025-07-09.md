---
id: pkm-os-manual-v2025-07-09
aliases: []
tags: []
---

# PKM-OS: Design & Operations Manual

**Version 1.1 (Draft)**  
**Last updated:** 2025-07-09

_This revision folds in the kernel/resource-management analogy and aligns the folder map with an FHS-inspired subset (/etc, /var, /lib, /tmp, /archive, /scripts)._

## 0 · Core Analogy

| **Computer Resource** | **Human Equivalent** | **PKM-OS Component**                                                | **How It Reduces Load**                                      |
| --------------------- | -------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------ |
| **CPU**               | Attention / Focus    | **Scheduler** (Todoist) + **Interrupt Handler** (/var/inb/Inbox.md) | Only one foreground task; distractions parked instantly.     |
| **RAM**               | Working Memory       | **Process Files** (/var/proc/…) + **Action Logs**                   | Off-loads active state so the brain can think, not remember. |
| **Power**             | Will-/Energy         | Clear capture → triage → review loops                               | Fewer meta-decisions, lower stress = more stamina.           |

## 1 · Instruction Set (Primitives)

_(unchanged)_

- **DRAFT · REVIEW · COMMUNICATE · PLAN · DECIDE**

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
entity:
tags: []
---

# Project: <descriptive title>

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
├── etc/            # Templates, system manuals, config lists
│   └── templates/  #   project-template.md, daily-template.md …
├── var/            # Live workspace
│   ├── inb/        #   Inbox.md + loose clips
│   ├── log/        #   dly/, mtg/, dec/, rev/
│   └── proc/       #   <context>/<entity>-<slug>/ project bundles
├── lib/            # Evergreen reference (organised by context/topic)
├── scripts/        # Helper .py / .sh (optional)
├── tmp/            # Disposable scratch
└── archive/        # Completed projects & frozen logs
```

### 4.1 Deterministic Filing Rules

| **Front-matter**                | **Destination**                                 |
| ------------------------------- | ----------------------------------------------- |
| type: reference                 | lib/<context>/<topic>/                          |
| type: project status: active    | var/proc/<context>/<entity>-<slug>/             |
| type: project status: completed | whole folder → archive/proc/<context>/<entity>/ |
| type: daily_log                 | var/log/dly/                                    |
| type: template                  | etc/templates/                                  |

_(Automation optional; manual drag-drop is fine until it hurts ≥3×.)_

## 5 · Scheduler Integration

- Todoist (or equivalent) holds a **single priority queue**.
- Each task's note link (obsidian://open?path=…) loads the matching Process File.
- Done → mark complete; if project ends, switch its YAML to status: completed and archive during review.

## 6 · Kernel-Style Operating Rules

1. **Interrupt → Inbox hot-key** (Ctrl-Alt-I): logs a line in Inbox.md in <2 s.
2. **Time-slice work** (25-min blocks). No mid-slice triage.
3. **Weekly swap-out** (review):
   - Inbox = 0
   - Stale var/proc/ (>30 days untouched) → pause or archive
   - Upcoming deadlines surfaced
4. **Energy reserves**: If Inbox > 50 or projects > 12 active → force triage before adding anything new.

## 7 · Core Workflow

1. **Schedule** – consult Todoist.
2. **Activate** – click deep link → Process File opens.
3. **Execute** – perform a Primitive.
4. **Log** – add a System Call line.
5. **File** – update YAML & move note if needed.
6. **Complete** – mark Todoist task done.

## Appendix A · Quick-Start Checklist

- Create top-level dirs exactly as tree above.
- Enable _Templates_ plugin; store them in /etc/templates/.
- Pin Inbox.md; map "Append to note" hot-key.
- Set Todoist filter to show only today's single top task.

_Run the system for two weeks before adding any automation scripts. Optimise only what breaks flow repeatedly._
