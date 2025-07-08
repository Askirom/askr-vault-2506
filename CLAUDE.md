---
id: CLAUDE
aliases: []
tags: []
---

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian vault - a personal knowledge management system using markdown files organized with a quest-based approach. Tasks are managed externally in Todoist (migrated 2025-07-08).

## Key Instructions for Claude

### File Structure Navigation

- **Consult Vaultmap.yaml first** before searching for documents
- **Always update Vaultmap.yaml** if file locations change or when creating/deleting files
- **Folder Structure**: Uses numerical prefixes (00_, 01_, 02_, etc.)
- **Quest Files**: Located in `20_Quests/[Type]/[Project]/` with `_QUEST-[Name].md` hub files

### File Naming Conventions

- **All files use underscores** instead of spaces: `File_Name.md`
- **Clean dashes** for separators: `_QUEST-SECUD.md` (not `_Quest_-_SECUD.md`)
- **Daily notes**: `YYYY-MM-DD.md` format
- **Templates**: `Template_[Type].md`

### Task Management

**IMPORTANT**: Tasks are managed externally in Todoist (migrated 2025-07-08)
- **No task syntax** in vault files (no `- [ ]` or `- [x]`)
- **No task queries** in templates or files
- **Focus**: Vault is for thinking, planning, and knowledge management only

### Active Plugins

- `dataview` - Database-like queries for dynamic content
- `table-editor-obsidian` - Enhanced table editing  
- `obsidian-icon-folder` - Visual folder organization
- `obsidian-git` - Git version control integration

### Search Priority

Use Vaultmap.yaml guidance for search priority:
- **High Priority**: `01_Nexus/`, `10_Library/`, `20_Quests/`, `30_Atlas/`
- **Medium Priority**: `02_Daily/`
- **Low Priority**: `00_To_Sort/`, `11_Attachments/`

### Person References

- Use `[[Name]]` format for person references
- Store person notes in `10_Library/Network/`
- Creates bidirectional connections automatically

### Daily Notes

- Template: `10_Library/Templates/Template_Daily_Log.md`
- Location: `02_Daily/YYYY-MM-DD.md`
- Archive: `02_Daily/YYYY/YYYY-MM/` for older notes

### Quest System

- **Main Quests**: Personal development (`20_Quests/Personal/`)
- **Guild Quests**: Professional client work (`20_Quests/Professional/`)
- **Side Quests**: Network activities (`20_Quests/Network/`)
- **Hive Quests**: Relationship projects (`20_Quests/Hive/`)

### Client Work

Active clients include: ARA, CLIFO, EHFREI, EKIBA, EMPIC, FDFRI, FITS, GOSME, INSTO, RBOMN, RCG, SECUD, VEDES, VGALT

### File Creation Rules

- **NEVER create files** unless absolutely necessary
- **ALWAYS prefer editing** existing files over creating new ones
- **NEVER proactively create documentation** files unless explicitly requested
- **Update Vaultmap.yaml** when creating/deleting files

### Technical Environment

User primarily works in:
- **Neovim** with obsidian.nvim plugin
- **WezTerm** terminal
- **Todoist** for task management (external)

---

*For complete system documentation, see: `30_Atlas/Askirom_System_2025-07-08.md`*