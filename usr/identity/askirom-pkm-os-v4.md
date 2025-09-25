## Askirom PKM-OS — V4 Guide

**Version 4** refines the original Askirom OS, evolving it into a more flexible and robust system for project-centric work.  
The core Unix philosophy remains, but workflows are adapted to prioritize self-contained projects and a standardized, portable metadata strategy.

### Core Philosophy

The system is organized like a computer's operating system. Each top-level folder has a distinct purpose.

### Folder Map

- `/etc` → **Templates & Configuration**  
  Note templates, system rules, saved queries.

- `/bin` → **Playbooks & Checklists**  
  Repeatable, "executable" procedures.

- `/var` → **Variable Logs** (fast-moving, chronological, not project-specific)  
  - `/action` → Standalone tasks (one note per task).  
  - `/daily` → Daily notes (`YYYY-MM-DD.md`).  
  - `/meeting` → Non-project meetings (e.g., `1-on-1s.md`, `Internal-Sync.md`).

- `/srv` → **Projects (Served Work)**  
  - `/<CLIENT>/<PROJECT_ID>_<slug>/` → One folder per project.

- `/usr` → **User Knowledge Base**  
  - `/identity` → Personal principles, goals, manifestos.  
  - `/reference` → General knowledge notes (atomic Zettelkasten).  
  - `/standards` → Laws, regulations, style guides.  
  - `rolodex.md` → Central contacts file.

- `/arc` → **Archive**  
  Archived project folders from `/srv` and old logs from `/var`.

- `/tmp` → **Inbox / Scratchpad**  
  Temporary, unsorted notes. Process regularly.

### Metadata: The Hybrid Approach (YAML + Dataview)

#### Principles
1. **YAML Frontmatter** = primary source of truth for core metadata.  
2. **Dataview inline fields** = contextual data inside note bodies.

#### Core Metadata (YAML Template)

```yaml
---
type: project | action | decision | meeting-log | knowledge | standard | daily
status: active | paused | done | proposed | evergreen
client: (Client code, e.g., CLIFO)
project: (Project ID, e.g., CLIFO-25-003)
contact: "[[Person's Name]]"
tags: []
---
```

### **Workflows**

#### **Projects (Core Unit)**
- Files:
	- _index.md → Scope, goals, metadata.
	- meetings.md → Rolling log of meetings.
	- decisions.md → Key project decisions.
	- backlog.md → Tasks and next actions.
	- notes/ → Research, drafts.
	- deliverables/ → Shipped documents.   

Example _index.md:
```yaml
---
type: project
status: active
client: CLIFO
project: CLIFO-25-003
contact: "[[Anna Schmidt]]"
tags: [security, compliance, BIA]
---
```

## PROJECT: Business Impact Analysis (BIA) for CLIFO

- **Scope**: Conduct a full BIA for all critical business units.  
- **Deadline**: 2025-12-15  
- **Key Links**: [[meetings]], [[decisions]], [[backlog]]

### **Meetings & Decisions**

- **Rule**: Store meeting/decision logs inside project folder.
- **Format**: Append-only, reverse-chronological, entries separated by ---.
- **General meetings**: Use /var/meeting/.

**Example decision entry:**

```
### 2025-09-24: Tooling Selection

> type:: decision  
> status:: done  
> decision:: We will use the 'Continuity Pro' software for the BIA interviews.  
> relates:: [[meetings#2025-09-22 BIA Tooling Workshop]]
```

### **Actions (Tasks)**

- **Standalone actions**: /var/action/ (one note each).
- **Project tasks**: checklist items in backlog.md.
- **Completion**: update status:: done, link to deliverable.  

**Example Action Note:**

```
---
type: action
status: active
client: CLIFO
project: CLIFO-25-003
tags: [drafting]
---

# DESC: Draft BIA interview script

The script needs review by [[Anna Schmidt]].

- **Output**: [[../srv/CLIFO/CLIFO-25-003_BIA/deliverables/BIA-Interview-Script-v1.md]]
```

## **Naming Conventions**

- Dates: YYYY-MM-DD
- Projects: <CLIENT-YY-###>_slug (e.g., CLIFO-25-003_BIA)
- Rule: Keep filenames short, descriptive, ASCII-safe.
## **Dataview Example**

**Query: Find all active decisions across projects**
````
```dataview
TABLE project, decision
FROM "/srv"
FLATTEN file.lists AS item
WHERE contains(item.type, "decision") AND contains(item.status, "active")
SORT file.mtime DESC
```
````
