# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian vault - a personal knowledge management system using markdown files. It follows a structured organizational framework for personal productivity, professional work, and knowledge management.

## Key Architecture

### Folder Structure
The vault uses a numerical prefix system for organization:
- `0 Inbox/` - Temporary staging for unprocessed content
- `02 Daily/` - Daily log files with date-based naming (YYYY-MM-DD.md)
- `10 Library/` - Organized reference materials by category (HIVE, NETWORK, PERSONAL, PROFESSIONAL, TEMPLATES)
- `20 Workshop/` - Active working files organized by category
- `30 Atlas/` - High-level system documentation and personal framework files

### Linking Strategy
Uses simple wikilinks for connections:
- **Person references**: `[[Name]]` format for all people mentioned
- **Direct file linking**: `[[filename]]` for related documents
- **No complex tagging**: Folder structure provides organization

### Active Plugins
- `dataview` - Database-like queries for dynamic content
- `obsidian-tasks-plugin` - Task management with scheduling
- `table-editor-obsidian` - Enhanced table editing
- `obsidian-icon-folder` - Visual folder organization
- `obsidian-git` - Git version control integration

## Common Operations

### Working with Daily Notes
Daily notes use the template from `10 Library/TEMPLATES/Template Daily Log.md` and include:
- Professional and personal logging sections
- Automated task queries showing overdue and scheduled items
- Date-based naming convention (YYYY-MM-DD.md)

### Task Management
Uses obsidian-tasks-plugin syntax with scheduling and due dates. Tasks are automatically aggregated in daily notes using dataview queries.

### Template Usage
Templates are stored in `10 Library/TEMPLATES/` and include variables like `{{DATE}}` for dynamic content generation.

### Git Integration
The vault uses obsidian-git plugin for automatic synchronization. Recent commits show regular "vault backup" operations.

## Important Files
- `30 Atlas/Askirom Obsidian Vault System Overview.md` - Comprehensive system documentation
- `30 Atlas/Askirom v2506 - Shadow Bolt.md` - Personal productivity framework and character sheet
- Templates in `10 Library/TEMPLATES/` - Standardized note structures

## File Naming Conventions
- Daily notes: `YYYY-MM-DD.md`
- Professional files often include dates: `YYYY-MM-DD Project Name.md`
- Template files prefixed with "Template"
- Atlas files contain version numbers (e.g., "v2506")

## Special Considerations
- Maintains personal and professional content separation
- Uses gamification elements (XP, quests, character stats) for productivity
- Integrates ADHD-friendly organizational principles
- Supports both German and English content