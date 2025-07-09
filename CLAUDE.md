# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian vault using the PKM-OS (Personal Knowledge Management Operating System) - a structured knowledge management system based on proven OS principles. Tasks are managed externally in Todoist (migrated 2025-07-08).

## Key Instructions for Claude

### File Structure Navigation

- **Consult Vaultmap.yaml first** before searching for documents
- **Always update Vaultmap.yaml** if file locations change or when creating/deleting files
- **PKM-OS Structure**: Purpose-driven organization with clear filing rules
- **Project Files**: Located in `var/prc/[context]/[client]/` with `_ProjectName_Project.md` main files

### File Naming Conventions

- **All files use underscores** instead of spaces: `File_Name.md`
- **Clean dashes** for separators: `_SECUD_Project.md`
- **Daily notes**: `YYYY-MM-DD.md` format in `var/log/dly/`
- **Templates**: `Template_[Type].md` in `sys/tpl/`
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

- **var/inb/**: New items to be processed and filed
- **var/log/dly/**: Daily log entries (YYYY-MM-DD.md format)
- **var/prc/**: Active work organized by context/client
- **lib/**: Reference materials by context (professional, personal, hive, network)
- **sys/**: Templates and Maps of Content (MOCs)
- **tmp/**: Temporary notes for deletion

### Search Priority

Use Vaultmap.yaml guidance for search priority:

- **High Priority**: `var/prc/`, `lib/`, `sys/`
- **Medium Priority**: `var/log/dly/`, `var/inb/`
- **Low Priority**: `tmp/`

### Person References

- Use `[[Name]]` format for person references
- Store person notes in `lib/network/`
- Creates bidirectional connections automatically

### Daily Notes

- Template: `sys/tpl/tpl-daily-log.md`
- Location: `var/log/dly/YYYY-MM-DD.md`
- All daily notes are in single flat structure

### Project System

- **Professional**: Client work (`var/prc/professional/[CLIENT]/`)
- **Personal**: Personal development (`var/prc/personal/`)
- **Network**: Community activities (`var/prc/network/`)
- **Hive**: Relationship projects (`var/prc/hive/`)

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

### Script Commands

- `rename-script-final.sh` - Renames files/directories to kebab-case format
- `kebab-rename.py` - Python script for file renaming operations
- Various analysis scripts in `sys/scripts/` for time tracking and data analysis

---

_For complete PKM-OS documentation, see: `sys/personal-knowledge-os.md`_
_For system maps and MOCs, see: `sys/maps/`_