---
id: CLAUDE
aliases: []
tags: []
---

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian vault - a personal knowledge management system using markdown files. It follows a structured organizational framework for personal productivity, professional work, and knowledge management using a gamified quest-based approach.

## Key Architecture

### Folder Structure

The vault uses a numerical prefix system for organization:

- `00_To_Sort/` - Temporary holding for unorganized content (Inbox for quick capture)
- `01_Nexus/` - Central command and high-level coordination
- `02_Daily/` - Daily log files with date-based naming (YYYY-MM-DD.md), archived monthly
- `10_Library/` - Organized reference materials (Hive, Network, Personal, Professional, Templates)
- `11_Attachments/` - File attachments organized by content type (Professional, Personal, Backups, Templates)
- `20_Quests/` - Quest-based project organization (Hive, Network, Personal, Professional)
- `30_Atlas/` - High-level system documentation and personal framework files. This is where Wisdom gets generated.

### Linking Strategy

Uses simple wikilinks for connections:

- **Person references**: `[[Name]]` format creates bidirectional connections automatically
- **Person notes**: Store in `10_Library/Network/`
- **Direct file linking**: `[[filename]]` for related documents
- **No complex tagging**: Folder structure provides organization

### Active Plugins

- `dataview` - Database-like queries for dynamic content
- `obsidian-tasks-plugin` - Task management with scheduling
- `table-editor-obsidian` - Enhanced table editing
- `obsidian-icon-folder` - Visual folder organization
- `obsidian-git` - Git version control integration

### Technical Environment

**Primary Tools:**

- **Neovim**: Main environment for writing, thinking, and automation scripts
- **obsidian.nvim**: Seamless vault access without leaving terminal
- **WezTerm**: Terminal-first workflow for focused sessions

**Use Cases:**

- **Writing & Thinking**: Notes, daily logs, quest documentation (primary)
- **Automation**: Scripts for workflow optimization, task management
- **Integration**: Terminal-based tools (Taskwarrior, Git, custom scripts)

## Quest-Based Project Management ("The Campaign of My Life")

The vault uses a gamified quest system for organizing all work and life activities:

### Quest Types

- **Main Quests**: Personal development and core life objectives (Askirom Evolution)
- **Guild Quests**: Professional client work organized by company (Professional folder)
- **Side Quests**: Network activities, learning, community work (Network folder)
- **Hive Quests**: Relationship with girlfriend (special sacred category)

### Quest Structure:

Each quest folder (`20_Quests/[Type]/[Project]/`) contains:

- One `_QUEST-[Name].md` hub file with YAML frontmatter
- Related project documents and notes
- Optional subfolders for large initiatives (max 4 levels deep)
- YAML frontmatter includes: type, questType, status, area, client fields
- Quest files use dataview queries for tracking

## Daily Workflow

Daily notes use the template from `10_Library/Templates/Template_Daily_Log.md`:

1. Create daily note with YYYY-MM-DD.md format in `02_Daily/`
2. Capture tasks quickly in `00_To_Sort/Inbox-Tasks.md`
3. Link to people using `[[Name]]` format
4. Link to related documents when relevant
5. Let folder structure handle organization
6. Professional and personal logging sections included
7. Automated task queries show overdue and scheduled items
8. Archived by year/month: `02_Daily/2025/2025-04/` for older notes

### Task Management

Uses obsidian-tasks-plugin syntax exclusively. Tasks captured in Inbox, organized as needed. Calendar handles scheduling.
_Note: As of 2025-07-04, experimenting with Taskwarrior integration._

## File Naming Conventions

- **All files use underscores** instead of spaces: `File_Name.md`
- **Clean dashes** for separators: `_QUEST-SECUD.md` (not `_QUEST_-_SECUD.md`)
- Daily notes: `YYYY-MM-DD.

