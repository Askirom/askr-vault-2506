# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository Overview

This is an Obsidian vault using PKM-OS v3.0 (Personal Knowledge Management Operating System) - a simplified Unix-inspired knowledge management system. Tasks are managed using Obsidian Tasks plugin with `TODO` filter.

## Key Instructions for Claude

### File Structure Navigation

- **Consult vaultmap.yaml first** before searching for documents
- **Always update vaultmap.yaml** if file locations change or when creating/deleting files
- **PKM-OS v3.0**: Uses descriptive filenames, not UIDs

### File Naming Conventions

- **Content files**: Descriptive names like `project-alpha-planning.md`
- **Daily notes**: `YYYY-MM-DD.md` format in `var/log/`
- **Templates**: `tpl-[Type].md` in `etc/templates/`

### Task Management

Tasks use Obsidian Tasks plugin with `TODO` as global filter:

- **Work tasks**: `- [ ] TODO Task description 📅 2025-07-15 ⏫`
- **Casual checklists**: `- [ ] Buy groceries` (ignored by Tasks plugin)
- **System files**: 
  - `/var/tasks.md` - Master task overview
  - `/var/spool.md` - System inbox

### PKM-OS v3.0 Directory Structure

```
/
├── etc/                    # System configuration
│   ├── templates/          # Note templates (tpl-*.md)
│   └── workflows/          # Scripts and procedures
├── var/                    # Active workspace
│   ├── tasks.md           # System task overview
│   ├── spool.md           # System inbox
│   ├── log/               # Daily & meeting logs
│   └── units/             # Active projects
├── lib/                   # Reference library
├── archive/               # Completed projects
```

### File Creation Rules

- **NEVER create files** unless absolutely necessary
- **ALWAYS prefer editing** existing files over creating new ones
- **Update vaultmap.yaml** when creating/deleting files

### Context Types

- **professional**: Business client work
- **personal**: Personal development projects
- **network**: Community activities
- **hive**: Relationship projects

### Technical Environment

- **Neovim** with obsidian.nvim plugin
- **Obsidian** with Tasks plugin
- **Git** for version control

---

_For complete PKM-OS documentation, see: `etc/personal-knowledge-os.md`_