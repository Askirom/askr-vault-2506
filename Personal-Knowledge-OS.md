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

{{needs to be implemented yet}}

### Examples:

---

## Layer 2: The Process File (The Container)

A Process File is the container for Log Entries. It is a single note dedicated to a single, cohesive topic, project, goal, or area of inquiry. Its purpose is to provide context for the actions being logged. It is the human-readable equivalent of an OS Process Control Block (PCB).

### Process File Template (v1.0):

{{not yet defined}}

## Layer 3: The File System

```
/
├── inbox/            # New items to be processed and filed.
├── journal/          # Personal notes and daily logs.
│   └── daily/
├── workbench/        # All active work-in-progress.
│   └── projects/
├── library/          # Your reference knowledge base.
├── system/           # Your life's "configuration": goals, values, templates.
└── scratchpad/       # Fleeting notes to be deleted.
```
