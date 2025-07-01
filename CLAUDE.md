# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian vault - a personal knowledge management system using markdown files. It follows a structured organizational framework for personal productivity, professional work, and knowledge management using a gamified quest-based approach.

## Key Architecture

### Folder Structure
The vault uses a numerical prefix system for organization:
- `00 To Sort/` - Temporary holding for unorganized content (Inbox for quick capture)
- `01 Nexus/` - Central command and high-level coordination
- `02 Daily/` - Daily log files with date-based naming (YYYY-MM-DD.md), archived monthly
- `10 Library/` - Organized reference materials (Hive, Network, Personal, Professional, Templates)
- `11 Attachments/` - File attachments organized by content type (Professional, Personal, Backups, Templates)
- `20 Quests/` - Quest-based project organization (Hive, Network, Personal, Professional)
- `30 Atlas/` - High-level system documentation and personal framework files

### Linking Strategy
Uses simple wikilinks for connections:
- **Person references**: `[[Name]]` format creates bidirectional connections automatically
- **Person notes**: Store in `10 Library/Network/` 
- **Direct file linking**: `[[filename]]` for related documents
- **No complex tagging**: Folder structure provides organization

### Core Principles
- **Direct linking** over complex tagging
- **Folder organization** handles categorization  
- **Minimal thinking** required when creating notes
- **Date-based naming** for time-sensitive work (YYYY-MM-DD format)
- **Terminal-friendly naming**: Underscores instead of spaces, clean dashes

### Active Plugins
- `dataview` - Database-like queries for dynamic content
- `obsidian-tasks-plugin` - Task management with scheduling
- `table-editor-obsidian` - Enhanced table editing
- `obsidian-icon-folder` - Visual folder organization
- `obsidian-git` - Git version control integration

## Common Operations

### Quest-Based Project Management ("The Campaign of My Life")
The vault uses a gamified quest system for organizing all work and life activities:

#### Quest Types:
- **Main Quests**: Personal development and core life objectives (Askirom Evolution)
- **Guild Quests**: Professional client work organized by company (Professional folder)
- **Side Quests**: Network activities, learning, community work (Network folder)
- **Hive Quests**: Relationship with girlfriend (special sacred category)

#### Quest Structure:
- Each quest has a `_QUEST-[Name].md` file with YAML frontmatter
- Quest files use dataview queries for tracking and organization
- YAML frontmatter includes: type, questType, status, area, client fields
- No milestone system - direct project organization within quests

### Working with Daily Notes
Daily notes use the template from `10 Library/Templates/Template_Daily_Log.md` and include:
- Professional and personal logging sections
- Automated task queries showing overdue and scheduled items
- Date-based naming convention (YYYY-MM-DD.md) in `02 Daily/`
- Archived by year/month: `02 Daily/2025/2025-04/` for older notes
- Current and previous month stay in root for accessibility

### Task Management
Uses obsidian-tasks-plugin syntax exclusively for task tracking. Tasks are captured quickly in the Inbox file (`00 To Sort/Inbox-Tasks.md`) and then organized as needed. Calendar is used for reminders and scheduling rather than additional task systems.

### Template Usage
Templates are stored in `10 Library/Templates/` and include:
- `Template_Daily_Log.md` - For daily notes
- `Template_Guild_Quest.md` - For professional client projects
- `Template_Main_Quest.md` - For personal goals and projects
- Templates use variables like `{{DATE}}` and `{{title}}` for dynamic content generation

### Git Integration
The vault uses obsidian-git plugin for automatic synchronization. Regular "vault backup" operations maintain version history.

### Daily Workflow
1. Capture tasks and notes quickly in `00 To Sort/Inbox-Tasks.md`
2. Link to people using `[[Name]]` format  
3. Link to related documents when relevant
4. Let folder structure handle organization
5. Use calendar for reminders and scheduling

## Important Files
- `30 Atlas/Askirom_v2506-Shadow_Bolt.md` - Personal productivity framework and character sheet
- `01 Nexus/000-Master_Quest_Log.md` - Central quest tracking with dataview queries
- `20 Quests/Personal/_QUEST-Askirom_Evolution.md` - Personal development quest with 4-stage evolution system
- `30 Atlas/XP_Log.md` - Experience point tracking (500€ billable = 1 XP)
- Templates in `10 Library/Templates/` - Standardized note structures

## File Naming Conventions
- **All files use underscores** instead of spaces: `File_Name.md`
- **Clean dashes** for separators: `_QUEST-SECUD.md` (not `_QUEST_-_SECUD.md`)
- Daily notes: `YYYY-MM-DD.md` (in `02 Daily/`)
- Quest files: `_QUEST-[Name].md` (in `20 Quests/` subfolders, `_` prefix for sorting)
- Professional files often include dates: `YYYY-MM-DD_Project_Name.md`
- Template files: `Template_[Type].md` (in `10 Library/Templates/`)
- Atlas files contain version numbers: `Askirom_v2506-Shadow_Bolt.md`
- Person files: `Firstname_Lastname.md`

## Organizational Patterns

### Subfolder Organization
- **Client projects** can have subfolders: `SECUD/NIS2/` for specific initiatives
- **Daily notes** archived: `02 Daily/2025/2025-04/` for past months
- **Attachments** by type: `11 Attachments/Professional/`, `Personal/`, `Backups/`, `Templates/`
- Maximum 4 levels deep to maintain usability

### Quest Organization
Each quest folder (`20 Quests/[Type]/[Project]/`) contains:
- One `_QUEST-[Name].md` hub file
- Related project documents and notes
- Optional subfolders for large initiatives
- Attachment subfolders when needed

## Core Principles
- **Clarity of Purpose**: The system must make things clearer, not more complex
- **Simplicity over Complexity**: Choose the simplest tool and structure that works
- **Inquiry over Assumption**: The system is a tool for asking questions, not just storing answers
- **Effectiveness over Busyness**: The goal is results and peace of mind, not performing productivity
- **Intentional Boundaries**: Maintain clear, mindful separation between different areas of life
- **Data Portability**: Retain ownership and control over personal data
- **Terminal Compatibility**: All files should work seamlessly in terminal environments

## XP & Gamification System

### Professional XP
- **Rule**: 500€ billable work = 1 XP
- **Target**: 24 XP/month = €12,000/month
- **Tracking**: Logged in `30 Atlas/XP_Log.md`

### Personal XP
- **Completion-based**: Variable XP for milestone achievements
- **Focus**: Progress and achievement rather than time tracking

### Character Development
- 4-stage evolution system: Tutorial → Adept → Expert → Master
- Character sheet approach in Atlas files
- Energy management focus over rigid productivity

## Backend Services Philosophy

### Calendar & Scheduling
The calendar is a sacred boundary tool, used to protect energy and honor commitments:
- **External**: meetings, calls, shared events
- **Internal**: focused work sessions, deep work, recovery time
- **Boundary Rule**: If it matters, it's on the calendar. If it's on the calendar, it's respected

### Notes & Knowledge
- **System**: Obsidian with Obsidian Sync
- **Structure**: `Library` (external knowledge) vs. `Quests` (active work) vs. `Atlas` (internal wisdom)

### Tasks & Projects
- **System**: Tasks plugin for task tracking, with quick capture in Inbox file
- **Deep work**: Managed within relevant notes in Obsidian's quest system
- **Scheduling**: Calendar handles reminders and time-based organization

## Special Considerations
- Maintains personal and professional content separation
- Uses gamification elements (XP, quests, character stats) for productivity
- Integrates ADHD-friendly organizational principles
- Supports both German and English content
- Energy-aware workflows over rigid productivity systems
- Terminal-friendly file naming for cross-platform compatibility

## Search Shortcuts
- **Find person**: `10 Library/Network/`
- **Find client**: `20 Quests/Professional/[CLIENT]/`
- **Find template**: `10 Library/Templates/`
- **Find daily note**: `02 Daily/YYYY-MM-DD.md`
- **Find reference**: `10 Library/Professional/`
- **Find archived dailies**: `02 Daily/2025/YYYY-MM/`

---
*Last updated: 2025-07-01 - System reflects current quest-based gamified organization*