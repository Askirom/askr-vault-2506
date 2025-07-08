---
id: Personal-Knowledge-OS
aliases: []
tags: []
---

# PKM-OS: Design & Operations Manual

**Last Updated:** 2025-07-08
**Version:** 0.1

## 1. Core Philosophy

This system treats personal knowledge management like an operating system. The goal is to manage competing demands on limited resources (attention, memory, time) using proven architectural principles like modularity and clear interfaces. It is a bottom-up design, starting with the most fundamental actions and building context from there.

---

## Layer 0: The Instruction Set (The Primitives)

These are the five fundamental, atomic actions the OS can perform. Every task, personal or professional, is a sequence of these primitives. This list is intentionally minimal and complete.

- **DRAFT:** Creating something new from scratch (text, a list, ideas).
- **REVIEW:** Consuming and assessing existing information (reading, watching, listening).
- **COMMUNICATE:** Interacting with another person (a call, an email, a meeting).
- **PLAN:** Organizing future actions or ideas (outlining, scheduling, structuring).
- **DECIDE:** Making a choice or a final judgment.

---

## Layer 1: The System Call (The Log Entry)

This is the standard format for recording any action performed by the OS. It is the fundamental unit of data capture, creating a chronological, auditable trail of work.

### Canonical Format:

`[YYYY-MM-DD HH:MM] :: <PRIMITIVE> - <A short, descriptive sentence of the action taken.>`

### Examples:

- `[2025-07-08 22:30] :: REVIEW - Read ISO 27001 controls A.9.1 through A.9.4.`
- `[2025-07-08 22:30] :: DRAFT - Wrote summary of findings for control A.9.1.`
- `[2025-07-08 22:30] :: DECIDE - Marked control A.9.1 as 'non-compliant'.`
- `[2025-07-08 22:30] :: PLAN - Outlined next steps for the Globex Corp audit.`
- `[2025-07-08 22:30] :: COMMUNICATE - Emailed John Smith regarding the non-compliance.`

---

## Layer 2: The Process File (The Container)

A Process File is the container for Log Entries. It is a single note dedicated to a single, cohesive topic, project, goal, or area of inquiry. Its purpose is to provide context for the actions being logged. It is the human-readable equivalent of an OS Process Control Block (PCB).

### Process File Template (v1.0):

Copy this template to create any new Process File.

```markdown
# Title: [Descriptive Title of the Project/Goal]

**Status:** In Progress / On Hold / Completed
**Key Stakeholder(s):** **Due Date:**

---

### Action Log

[YYYY-MM-DD HH:MM] :: <PRIMITIVE> - <Description of action>
```
