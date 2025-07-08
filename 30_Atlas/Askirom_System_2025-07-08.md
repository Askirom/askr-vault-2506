---
id: Askirom_System_2025-07-08
aliases: [System Documentation, Workflow Documentation]
tags: [system, workflow, documentation]
---

# Askirom System Documentation v2025-07-08

*Complete system documentation following task management migration to Todoist*

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
- `table-editor-obsidian` - Enhanced table editing
- `obsidian-icon-folder` - Visual folder organization
- `obsidian-git` - Git version control integration

### Technical Environment

**Primary Tools:**

- **Neovim**: Main environment for writing, thinking, and automation scripts
- **obsidian.nvim**: Seamless vault access without leaving terminal
- **WezTerm**: Terminal-first workflow for focused sessions
- **Todoist**: External task management (tasks migrated from vault 2025-07-08)

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
2. Link to people using `[[Name]]` format
3. Link to related documents when relevant
4. Let folder structure handle organization
5. Professional and personal logging sections included
6. Archived by year/month: `02_Daily/2025/2025-04/` for older notes

### Task Management

**External Task Management:** Tasks migrated to Todoist (2025-07-08). Vault now focuses on thinking, planning, and knowledge management.

- **Execution**: Todoist for task tracking and scheduling
- **Planning**: Vault for strategic thinking and quest coordination
- **Clean Separation**: No task syntax in vault files

**Migration Details:**
- 71 tasks extracted from 34+ files
- All incomplete tasks organized in `migrate-to-todoist.md`
- Task-related queries and syntax removed from all files
- Templates updated to focus on reflection and planning

## File Naming Conventions

- **All files use underscores** instead of spaces: `File_Name.md`
- **Clean dashes** for separators: `_QUEST-SECUD.md` (not `_Quest_-_SECUD.md`)
- Daily notes: `YYYY-MM-DD.md`

## Active Clients (as of 2025-07-08)

- **ARA** - Data processing assessments
- **CLIFO** - IT security consulting  
- **EHFREI** - Risk analysis projects
- **EKIBA** - ISMS documentation
- **EMPIC** - VdS certification support
- **FDFRI** - Data protection compliance
- **FITS** - Document management systems
- **GOSME** - Various security projects
- **INSTO** - Information security
- **RBOMN** - Compliance consulting
- **RCG** - Deputy appointments and consulting
- **SECUD** - NIS2 implementation and auditing
- **VEDES** - Security assessments
- **VGALT** - Compliance projects

## Revenue Tracking System

### XP System
- **Professional**: 500€ billable = 1 XP
- **Target**: 24 XP/month = €12,000
- **Tracking**: `30_Atlas/XP_Log.md`

### Character Sheet
- **Location**: `30_Atlas/Askirom_v2506-Shadow_Bolt.md`
- **Purpose**: Personal development tracking and gamification

## File Patterns

- **Quest files**: `_Quest-[Name].md`
- **Daily notes**: `YYYY-MM-DD.md`
- **Templates**: `Template_[Type].md`
- **Professional docs**: `YYYY-MM-DD_[Project].md`
- **Person files**: `Firstname_Lastname.md`

## System Evolution Notes

### 2025-07-08 Task Migration
- Migrated all task management to external Todoist system
- Cleaned vault of task syntax and queries
- Focused vault on strategic thinking and knowledge management
- Maintained quest-based organization for high-level coordination

### Future Considerations
- Continue terminal-first workflow with neovim/wezterm
- Maintain clean separation between thinking (vault) and execution (todoist)
- Preserve quest gamification for motivation and organization
- Regular system reviews and documentation updates

## Integration Points

### With Todoist
- **Strategic Planning**: Vault for long-term thinking and quest coordination
- **Daily Execution**: Todoist for task tracking and scheduling
- **Revenue Tracking**: XP system remains in vault for motivation

### With Development Environment
- **Primary Editor**: Neovim with obsidian.nvim plugin
- **Terminal**: WezTerm for focused sessions
- **Version Control**: Git integration for backup and versioning
- **Automation**: Custom scripts for workflow optimization

## Maintenance Schedule

- **Daily**: Daily notes creation and logging
- **Weekly**: Quest status reviews and updates
- **Monthly**: XP tracking and system performance review
- **Quarterly**: Major system documentation updates
- **Yearly**: Complete system architecture review

---

*This documentation represents the current state of the Askirom personal productivity system as of 2025-07-08, following the major task management migration to external tools.*