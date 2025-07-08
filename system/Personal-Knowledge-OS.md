---
id: Personal-Knowledge-OS
aliases: []
tags: []
---

# PKM-OS: Design & Operations Manual

**Last Updated:** 2025-07-09
**Version:** 0.4

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

**Decision deferred.** The final syntax will be simple and low-friction. Current candidates include:

- **Minimalist Style:** `- DRAFT: Wrote the project outline.`
- **Tag-based Style:** `[2025-07-09] #review Read the new policy.`
- **Emoji Style:** `✍️ Wrote the project outline.`

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
client:
tags: []
---

# Project: [Descriptive Title]

**Goal:**
**Due Date:**
**Key Stakeholder(s):**

---

### Action Log

-
```

---

## 5\. Layer 3: The File System

This layer defines where all notes are stored. It uses a purpose-driven structure inspired by Unix-like operating systems. The filing of notes is not arbitrary; it is determined by the note's metadata.

### 5.1. Top-Level Directory Structure

```
/
├── inbox/            # New items to be processed and filed.
├── journal/          # Personal notes and daily logs.
│   └── daily/
├── workbench/        # All active work-in-progress.
│   └── projects/
├── library/          # Your reference knowledge base.
├── system/           # Your life's "configuration": goals, values, templates.
│   └── templates/
└── scratchpad/       # Fleeting notes to be deleted.
```

### 5.2. Library Organization

The `library/` directory is organized by **Context/Role** ("hats"). This prioritizes the application of knowledge.

- `library/professional/`
- `library/personal/`
- `library/hive/`
- `library/network/`

To handle cross-cutting knowledge, this system uses **Maps of Content (MOCs)** as a form of "symbolic link," allowing a note that lives in one context (e.g., `professional/`) to be referenced in the MOC of another (e.g., `hive/`).

### 5.3. Workbench Organization

The `workbench/` directory is organized by **encapsulation**. Every non-trivial project gets its own dedicated folder to keep all related assets together. This structure is hierarchical to allow for Browse by context and client.

The standard path for a project is: `workbench/projects/[context]/[client]/[ProjectName]/`

**Example Structure:**

```
workbench/
└── projects/
    └── professional/
        └── ARA/  <-- Folder for a specific client
            └── ARA-Q3-Audit/  <-- The encapsulated project folder
                ├── _Project-ARA-Q3-Audit.md  <-- Main Process File
                └── Draft-Final-Report.md
```

### 5.4. Metadata-Driven Filing Logic

The OS uses YAML frontmatter to file notes deterministically. The core metadata fields are `type`, `context`, `topic`, `client`, and `status`.

**The Rules:**

- **IF `type: reference` THEN** move to `library/[context]/[topic]/`
- **IF `type: project` AND `status: active` THEN** move to `workbench/projects/[context]/[client]/` (as a new project folder).
- **IF `type: project` AND `status: completed` THEN** move the entire project folder to `archive/projects/[context]/[client]/`.
- **IF `type: daily_log` THEN** move to `journal/daily/`
- **IF `type: template` THEN** move to `system/templates/`

---

## 6\. Layer 4: The Scheduler (The Integration)

This layer determines **what** to work on and **when**. It is handled by a dedicated, external task manager (e.g., Todoist, Things).

- **Principle:** The Scheduler's only job is to manage a prioritized list of tasks. The work itself is executed within the PKM-OS.
- **Integration Method:** Each task in the Scheduler must contain a direct **Obsidian URL** link to the relevant Process File (in `workbench/projects/` or elsewhere). This creates a frictionless, single-click handoff from deciding on a task to executing the work.

---

## Appendix A: Core Workflow

1.  **Schedule:** Consult the **Scheduler** to choose a task.
2.  **Activate:** Click the Obsidian URL in the task to open the corresponding **Process File**.
3.  **Execute:** Perform the work using one of the five **Primitives**.
4.  **Log:** Record the action by adding a new **Log Entry** to the Process File's Action Log.
5.  **(Optional) File:** If working on a new note from the `inbox/`, update its YAML frontmatter and move it to its correct location according to the filing logic.
6.  **Complete:** Mark the task as done in the Scheduler.
