---
id: Personal-Knowledge-OS
aliases: []
tags: []
type: system
---

# PKM-OS: Design & Operations Manual

**Version 3.0 (Simplified)**
**Last updated:** 2025-07-13

_This revision simplifies the system by eliminating over-engineered components while preserving the core "Everything is a file" philosophy._

---

## 0 · Core Philosophy: "Everything is a File"

This system applies the Unix philosophy that everything can be represented as a file. Projects, tasks, and knowledge are all stored as plain text files on disk. This approach ensures uniform tooling (`grep`, `find`, `git`), zero vendor lock-in, and provides perfect clarity and reviewability for all past work.

---

## 1 · Core Components

The system consists of three simple, well-integrated tools:

| **Tool**                    | **Purpose**                                    | **Why This Tool**                                                    |
| :-------------------------- | :--------------------------------------------- | :------------------------------------------------------------------- |
| **Obsidian + Tasks Plugin** | Project management, task tracking, note-taking | Native markdown support, powerful task queries, excellent mobile app |
| **Google Calendar**         | Time-based scheduling, appointments, reminders | Best-in-class calendar features, reliable notifications              |
| **Git**                     | Version control, sync, backup                  | Universal, reliable, works with any platform                         |

---

## 2 · File Structure

Unix-inspired organization that supports systematic knowledge management:

```
/
├── etc/                      # System configuration
│   ├── templates/            #   Project and note templates
│   └── workflows/            #   Standard operating procedures
├── var/                      # Active workspace & volatile data
│   ├── tasks.md              #   System task overview dashboard
│   ├── spool.md              #   System inbox for quick capture
│   ├── lib/                  #   (simplified - no external service mirrors)
│   ├── log/                  #   Daily & meeting logs
│   └── units/                #   Active projects & services
├── lib/                      # Reference knowledge library
├── archive/                  # Completed projects and old material
```

---

## 3 · Project Files

Each project is a single `.md` file with descriptive naming and embedded tasks.

**File naming:** Use descriptive names like `project-alpha-planning.md`, not UIDs.

**Example project file with full task capabilities:**

```markdown
# Project Alpha Planning

**Status:** Active  
**Category:** Work  
**Goal:** Launch new product feature by Q3

## Tasks

- [ ] TODO Research competitor features 🛫 2025-07-14 📅 2025-07-15 ⏫
- [ ] TODO Draft initial requirements ⏳ 2025-07-16 📅 2025-07-18
- [ ] TODO Weekly stakeholder check-in 🔁 every week ⏳ 2025-07-15
- [x] TODO Meet with stakeholders ✅ 2025-07-12

## Notes

Initial meeting went well. Key requirements identified:

- Mobile-first design
- Integration with existing API

## Action Log

- [2025-07-12 14:00] – PLAN: Outlined project scope and timeline
- [2025-07-13 09:00] – COMMUNICATE: Stakeholder meeting completed
```

---

## 4 · Task Management

Tasks use the Obsidian Tasks plugin with `TODO` as the global filter to distinguish work tasks from casual checklists.

**Task format with full capabilities:**

```markdown
- [ ] TODO Task description 🛫 2025-07-14 📅 2025-07-15 ⏫ 🔁 every week
```

**All available task attributes:**

- **Basic task:** `- [ ] TODO Research competitor features`
- **Due date:** `📅 2025-07-15` (when it must be completed)
- **Scheduled:** `⏳ 2025-07-14` (when you plan to work on it)
- **Start date:** `🛫 2025-07-13` (when task becomes actionable)
- **Priority:** `⏫` (high) `🔼` (medium) `🔽` (low) `⏬` (lowest)
- **Recurrence:** `🔁 every week` / `🔁 every month` / `🔁 every 3 days`
- **Created:** `➕ 2025-07-13` (auto-added by plugin)
- **Done:** `✅ 2025-07-13` (auto-added when completed)

**Global filter setup:**
Set Tasks plugin global filter to: `TODO`

This means:

- `- [ ] Buy groceries` → ignored by Tasks plugin (casual checklist)
- `- [ ] TODO Draft project proposal 📅 2025-07-15` → managed by Tasks plugin

**Master task view:**
Create `/var/tasks.md` with queries to see all work:

````markdown
# Task Overview

## Overdue

```tasks
not done
due before today
```

## Due This Week

```tasks
not done
due after yesterday
due before in 7 days
sort by due
```

## High Priority

```tasks
not done
priority is high
sort by priority, due
```

## No Due Date

```tasks
not done
no due date
sort by priority
```

## Scheduled for Today

```tasks
not done
scheduled on today
```
````

---

## 5 · Daily Workflow

**Intentional planning approach** - you choose your focus rather than being driven by automated systems.

1. **Weekly Review:** Check `/var/tasks.md` to see all open work
2. **Daily Planning:** Consciously select 2-3 tasks for today
3. **Execution:** Work from your chosen tasks, log progress in `/var/units/` files
4. **Capture:** Quick thoughts go to `/var/spool.md` for later processing
5. **Sync:** Commit changes to git regularly

---

## 6 · Action Logging

Log significant work using a simple, consistent format:

```
- [YYYY-MM-DD HH:MM] – ACTION: Description
```

**Actions:** PLAN, DRAFT, REVIEW, COMMUNICATE, DECIDE, MAINTAIN

This creates a searchable history of all work across projects.

---

## 7 · Mobile Workflow

- **Obsidian mobile app:** Full access to all files and tasks
- **Google Calendar:** Appointments and time-based reminders
- **Git sync:** Changes sync automatically across devices

---

**Philosophy:** Start simple, add complexity only when you prove you need it.
