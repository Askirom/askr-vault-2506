# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian vault - a personal knowledge management system using markdown files. It follows a structured organizational framework for personal productivity, professional work, and knowledge management.

## Key Architecture

### Folder Structure
The vault uses a numerical prefix system for organization:
- `01 Daily/` - Daily log files with date-based naming (YYYY-MM-DD.md)
- `10 Library/` - Organized reference materials by category (HIVE, NETWORK, PERSONAL, PROFESSIONAL, TEMPLATES)
- `11 Attachments/` - File attachments and media assets
- `20 Quests/` - Quest-based project organization (HIVE, NETWORK, PERSONAL, PROFESSIONAL)
- `30 Atlas/` - High-level system documentation and personal framework files
- `00 To Sort/` - Temporary holding for unorganized content

### Linking Strategy
Uses simple wikilinks for connections:
- **Person references**: `[[Name]]` format creates bidirectional connections automatically
- **Person notes**: Store in `10 Library/NETWORK/` 
- **Direct file linking**: `[[filename]]` for related documents
- **No complex tagging**: Folder structure provides organization

### Core Principles
- **Direct linking** over complex tagging
- **Folder organization** handles categorization  
- **Minimal thinking** required when creating notes
- **Date-based naming** for time-sensitive work (YYYY-MM-DD format)

### Active Plugins
- `dataview` - Database-like queries for dynamic content
- `obsidian-tasks-plugin` - Task management with scheduling
- `quickadd` - Fast task capture and content routing with smart automation
- `table-editor-obsidian` - Enhanced table editing
- `obsidian-icon-folder` - Visual folder organization
- `obsidian-git` - Git version control integration

## Common Operations

### Quest-Based Project Management
The vault uses a gamified quest system for organizing work:
- **Guild Quests**: Professional client work organized by company (PROFESSIONAL folder)
- **Main Quests**: Personal goals and long-term projects
- Each quest has a `QUEST - [Name].md` file with dataview queries for tracking milestones
- Quest files use YAML frontmatter with type, questType, status, area, and client fields

### Working with Daily Notes
Daily notes use the template from `10 Library/TEMPLATES/Template Daily Log.md` and include:
- Professional and personal logging sections
- Automated task queries showing overdue and scheduled items
- Date-based naming convention (YYYY-MM-DD.md)

### Task Management
Uses obsidian-tasks-plugin syntax with scheduling and due dates. Tasks are automatically aggregated in daily notes using dataview queries.

#### QuickAdd Task Capture System
The vault uses QuickAdd plugin for lightning-fast task capture with intelligent routing:
- **⚡ Quick Task** - Smart routing based on client/keyword detection
- **🏢 Client Task** - Structured capture for professional work
- **📅 Today's Tasks** - Direct capture to current daily note
- **🏠 Personal Task** - Routes to personal quest system
- **📥 Quick Sort** - Temporary inbox for uncertain categorization

Configuration files:
- `quickadd-scripts/quick-task.js` - Smart routing logic with client detection
- `10 Library/TEMPLATES/QuickAdd Client Task.md` - Template for complex client tasks

### Template Usage
Templates are stored in `10 Library/TEMPLATES/` and include:
- `Template Daily Log.md` - For daily notes
- `Template Guild Quest.md` - For professional client projects
- `Template Main Quest.md` - For personal goals and projects
- Templates use variables like `{{DATE}}` and `{{title}}` for dynamic content generation

### Git Integration
The vault uses obsidian-git plugin for automatic synchronization. Recent commits show regular "vault backup" operations.

### Daily Workflow
1. Capture content in `00 To Sort/` or directly in appropriate folder
2. Link to people using `[[Name]]` format  
3. Link to related documents when relevant
4. Let folder structure handle organization

## Important Files
- `30 Atlas/Askirom v2506 - Shadow Bolt.md` - Personal productivity framework and character sheet
- `30 Atlas/000 - Master Quest Log.md` - Central quest tracking with dataview queries
- `20 Quests/PERSONAL/QUEST - Askirom Evolution.md` - Personal development quest with 4-stage evolution system
- Templates in `10 Library/TEMPLATES/` - Standardized note structures
- `quickadd-scripts/quick-task.js` - Smart task routing automation

## File Naming Conventions
- Daily notes: `YYYY-MM-DD.md` (in `01 Daily/`)
- Quest files: `QUEST - [Name].md` (in `20 Quests/` subfolders)
- Professional files often include dates: `YYYY-MM-DD Project Name.md`
- Template files prefixed with "Template" (in `10 Library/TEMPLATES/`)
- Atlas files contain version numbers (e.g., "v2506")
- Attachments organized by context in `11 Attachments/`

## Core Principles
- **Clarity of Purpose**: The system must make things clearer, not more complex
- **Simplicity over Complexity**: Choose the simplest tool and structure that works
- **Inquiry over Assumption**: The system is a tool for asking questions, not just storing answers
- **Effectiveness over Busyness**: The goal is results and peace of mind, not performing productivity
- **Intentional Boundaries**: Maintain clear, mindful separation between different areas of life
- **Data Portability**: Retain ownership and control over personal data

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
- **System**: QuickAdd plugin for lightning-fast capture with intelligent routing
- **Deep work**: Managed within relevant notes in Obsidian's quest system
- **Capture patterns**: 5 essential patterns covering 90% of task creation needs

## Special Considerations
- Maintains personal and professional content separation
- Uses gamification elements (XP, quests, character stats) for productivity
- Integrates ADHD-friendly organizational principles
- Supports both German and English content
- Energy-aware workflows over rigid productivity systems