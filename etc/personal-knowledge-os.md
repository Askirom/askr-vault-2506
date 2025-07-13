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

Simple, descriptive organization that supports the workflow:

```
/
├── projects/                 # Active projects and ongoing work
├── notes/                    # Reference knowledge and meeting notes
├── templates/                # Project and note templates
├── archive/                  # Completed projects and old material
└── inbox.md                  # Quick capture for processing later
```

---

## 3 · Project Files

Each project is a single `.md` file with descriptive naming and embedded tasks.

**File naming:** Use descriptive names like `project-alpha-planning.md`.

**Example file structure:**

```markdown
# Project Alpha Planning

**Status:** Active  
**Category:** Work  
**Goal:** Launch new product feature by Q3

## Tasks

- [ ] Research competitor features 📅 2025-07-15
- [ ] Draft initial requirements ⏫
- [x] Meet with stakeholders ✅ 2025-07-12

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

Tasks use the Obsidian Tasks plugin syntax for powerful querying and management.

**Task formats:**

- `- [ ] Basic task`
- `- [ ] Task with due date 📅 2025-07-15`
- `- [ ] High priority task ⏫`
- `- [ ] Recurring task 🔁 every week`

**Master task view:**
Create a `TASKS.md` file with queries to see all open work:

````markdown
# All Tasks

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
```

## High Priority

```tasks
not done
priority is high
```
````

---

## 5 · Daily Workflow

**Intentional planning approach** - you choose your focus rather than being driven by automated systems.

1. **Weekly Review:** Check `TASKS.md` to see all open work
2. **Daily Planning:** Consciously select 2-3 tasks for today
3. **Execution:** Work from your chosen tasks, log progress
4. **Capture:** Quick thoughts go to `inbox.md` for later processing
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

## 8 · What This Eliminates

**Removed complexity from v2.0:**

- ❌ UID-based file naming (use descriptive names)
- ❌ External service mirroring (`/var/lib/todoist/`)
- ❌ Automated promotion scripts (capture directly to right place)
- ❌ Complex folder hierarchy (simplified to 4 main folders)
- ❌ systemd terminology (use plain language)
- ❌ Rigid status lifecycles (just active/archived)
- ❌ Separate daily logs (log in project files)

**What remains:**

- ✅ Everything as files
- ✅ Git version control
- ✅ Action logging
- ✅ Project-based organization
- ✅ Cross-platform accessibility

---

## 9 · Setup Checklist

- [ ] Install Obsidian and Tasks plugin
- [ ] Create folder structure in git repository
- [ ] Set up `TASKS.md` with task queries
- [ ] Configure Obsidian mobile app
- [ ] Create project and note templates
- [ ] Test git sync workflow

**Philosophy:** Start simple, add complexity only when you prove you need it.
