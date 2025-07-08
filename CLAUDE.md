---
id: CLAUDE
aliases: []
tags: []
---

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian vault using the PKM-OS (Personal Knowledge Management Operating System) - a structured knowledge management system based on proven OS principles. Tasks are managed externally in Todoist (migrated 2025-07-08).

## Key Instructions for Claude

### File Structure Navigation

- **Consult Vaultmap.yaml first** before searching for documents
- **Always update Vaultmap.yaml** if file locations change or when creating/deleting files
- **PKM-OS Structure**: Purpose-driven organization with clear filing rules
- **Project Files**: Located in `workbench/projects/[context]/[client]/` with `_ProjectName_Project.md` main files

### File Naming Conventions

- **All files use underscores** instead of spaces: `File_Name.md`
- **Clean dashes** for separators: `_SECUD_Project.md`
- **Daily notes**: `YYYY-MM-DD.md` format in `journal/daily/`
- **Templates**: `Template_[Type].md` in `system/templates/`
- **Project files**: `_ProjectName_Project.md` pattern

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

### PKM-OS Directory Structure

- **inbox/**: New items to be processed and filed
- **journal/daily/**: Daily log entries (YYYY-MM-DD.md format)
- **workbench/projects/**: Active work organized by context/client
- **library/**: Reference materials by context (professional, personal, hive, network)
- **system/**: Templates and Maps of Content (MOCs)
- **scratchpad/**: Temporary notes for deletion

### Search Priority

Use Vaultmap.yaml guidance for search priority:

- **High Priority**: `workbench/projects/`, `library/`, `system/`
- **Medium Priority**: `journal/daily/`, `inbox/`
- **Low Priority**: `scratchpad/`

### Person References

- Use `[[Name]]` format for person references
- Store person notes in `library/network/`
- Creates bidirectional connections automatically

### Daily Notes

- Template: `system/templates/Template_Daily_Log.md`
- Location: `journal/daily/YYYY-MM-DD.md`
- All daily notes are in single flat structure

### Project System

- **Professional**: Client work (`workbench/projects/professional/[CLIENT]/`)
- **Personal**: Personal development (`workbench/projects/personal/`)
- **Network**: Community activities (`workbench/projects/network/`)
- **Hive**: Relationship projects (`workbench/projects/hive/`)

### Client Work

Active clients include: ARA, CLIFO, EHFREI, EKIBA, EMPIC, FDFRI, FITS, GOSME, INSTO, RBOMN, RCG, SECUD, SOLVE, VEDES, VGALT

### File Creation Rules

- **NEVER create files** unless absolutely necessary
- **ALWAYS prefer editing** existing files over creating new ones
- **NEVER proactively create documentation** files unless explicitly requested
- **Update Vaultmap.yaml** when creating/deleting files

### Metadata Requirements

All files must have proper YAML frontmatter based on type:

- **Projects**: `type: project`, `status: active`, `context: [context]`, `created: YYYY-MM-DD`
- **Reference**: `type: reference`, `topic: [topic]`, `created: YYYY-MM-DD`
- **Daily**: `type: daily_log`, `date: YYYY-MM-DD`, `created: YYYY-MM-DD`
- **Templates**: `type: template`, `created: YYYY-MM-DD`
- **MOCs**: `type: moc`, `created: YYYY-MM-DD`

### Technical Environment

User primarily works in:

- **Neovim** with obsidian.nvim plugin
- **WezTerm** terminal
- **Todoist** for task management (external)

---

_For complete PKM-OS documentation, see: `system/Personal-Knowledge-OS.md`_
_For system maps and MOCs, see: `system/maps/`_

