---
id: Personal-Knowledge-OS
aliases: []
tags: []
type: system
---

# PKM-OS: Design & Operations Manual

**Last Updated:** 2025-07-09
**Version:** 1.0 (Release)

## 1. Core Philosophy

This system treats personal knowledge management like an operating system. The goal is to manage competing demands on limited resources (attention, memory, time) using proven architectural principles like modularity and clear interfaces. It is a bottom-up design, starting with the most fundamental actions and building context from there.

---

## 2. Layer 0: The Instruction Set (The Primitives)

These are the five fundamental, atomic actions the OS can perform. Every task, personal or professional, is a sequence of these primitives. This list is intentionally minimal and complete.

- **DRAFT:** Creating something new from scratch (text, a list, ideas).
- **REVIEW:** Consuming and assessing existing information (reading, watching, listening).
- **COMMUNICATE:** Interacting with another person (a call, an email, a meeting).
- **PLAN:** Organizing future actions or ideas (outlining, scheduling, structuring).
- **DECIDE:** Making a choice or a final judgment.

---

## 3. Layer 1: The System Call (The Log Entry)

This is the standard format for recording any action performed by the OS. It is the fundamental unit of data capture, creating a chronological, auditable trail of work.

### Canonical Format:

The format is: `[YYYY-MM-DD HH:MM] - PRIMITIVE (Optional Actor): Message`

- **Timestamp:** Precise to the minute. Can be inserted automatically by templates.
- **PRIMITIVE:** One of the five primitives from Layer 0.
- **(Optional Actor):** Used only when logging an action or decision made by someone else. Omitted when the actor is you.
- **Message:** A concise description of the action.

**Examples:**

- `[2025-07-09 16:05] - PLAN: Outline the next steps for the ARA audit.`
- `[2025-07-09 16:05] - DECIDE (Client ARA): Approved the new project scope.`

---

## 4. Layer 2: The Process File (The Container)

A Process File is the container for Log Entries. It is a single note dedicated to a single, cohesive topic, project, goal, or area of inquiry. Its purpose is to provide context for the actions being logged. It is the human-readable equivalent of an OS Process Control Block (PCB).

### Project File Template (v1.0):

A template for a `project` type note. It must contain the necessary YAML frontmatter to be filed correctly by the system.

```markdown
---
type: project
status: active
context:
entity:
tags: []
---

# Project: [Descriptive Title]

**Goal:**
**Due Date:**
**Key Stakeholder(s):**

---

### Action Log

- [{{date:YYYY-MM-DD}} {{time:HH:mm}}] - PRIMITIVE (Optional Entity):
```

---

## 5\. Layer 3: The File System

This layer defines where all notes are stored. It uses a purpose-driven structure inspired by Unix-like operating systems, separating variable data from static libraries and system files. The filing of notes is not arbitrary; it is determined by the note's metadata. All file and folder names should be in `kebab-case`.

### 5.1. Top-Level Directory Structure

```
/
├── var/            # The "Active Workspace" for all variable data.
├── lib/            # The "Reference Library" for static knowledge.
├── sys/            # The "System" configuration files and templates.
├── tmp/            # Temporary scratchpad files.
└── archive/        # "Cold storage" for completed projects.
```

### 5.2. Variable Data (`var/`) Organization

This is the directory where you "live" day-to-day. It contains all active and changing information, separated by function.

```
/var/
├── inb/            # Inbox for new, unprocessed items.
├── log/            # Chronological logs (daily, meetings, etc.).
│   └── dly/
└── proc/           # Active processes (projects).
```

### 5.3. Project (`proc/`) Organization

The `proc/` directory is organized by **encapsulation**. Every project gets its own folder. This structure is hierarchical to allow for Browse by context and entity.

The standard path for a project is: `var/proc/[context]/[ENTITY-CODE]-[descriptive-name]/`

**Example Structure:**

```
var/
└── proc/
    └── professional/
        └── ARA-gdpr-compliance-consulting/
            ├── ara-project.md
            └── compliance-checklist.md
```

### 5.4. Library (`lib/`) Organization

The `lib/` directory is organized by **Context/Role** ("hats"). Inside each context, subfolders can be created for specific topics. Cross-contextual links are handled by Maps of Content (MOCs).

### 5.5. Metadata-Driven Filing Logic

The OS uses YAML frontmatter to file notes deterministically.

**The Rules:**

- **IF `type: reference` THEN** move to `lib/[context]/[topic]/`
- **IF `type: project` AND `status: active` THEN** move to `var/proc/[context]/[ENTITY-CODE]-[descriptive-name]/` (as a new project folder).
- **IF `type: project` AND `status: completed` THEN** move the entire project folder to `archive/proc/[context]/[entity]/`.
- **IF `type: daily_log` THEN** move to `var/log/dly/`
- **IF `type: template` THEN** move to `sys/tpl/`

---

## 6. Layer 4: The Scheduler (The Integration)

This layer determines **what** to work on and **when**. It is handled by a dedicated, external task manager (e.g., Todoist).

- **Principle:** The Scheduler's only job is to manage a prioritized list of tasks. The work itself is executed within the PKM-OS.
- **Integration Method:** Each task in the Scheduler must contain a direct **Obsidian URL** link to the relevant Process File (in `var/proc/` or elsewhere).

---

## Appendix A: Core Workflow

1.  **Schedule:** Consult the **Scheduler** to choose a task.
2.  **Activate:** Click the Obsidian URL in the task to open the corresponding **Process File**.
3.  **Execute:** Perform the work using one of the five **Primitives**.
4.  **Log:** Record the action by adding a new **Log Entry** to the Process File's Action Log.
5.  **File:** If working on a new note from `var/inb/`, update its YAML frontmatter and move it to its correct location according to the filing logic.
6.  **Complete:** Mark the task as done in the Scheduler.
