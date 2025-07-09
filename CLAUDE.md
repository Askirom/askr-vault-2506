# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian vault using the PKM-OS v1.2 (Personal Knowledge Management Operating System) - a UID-based knowledge management system based on proven OS principles. Tasks are managed externally in Todoist (migrated 2025-07-08).

## Key Instructions for Claude

### File Structure Navigation

- **Consult Vaultmap.yaml first** before searching for documents
- **Always update Vaultmap.yaml** if file locations change or when creating/deleting files
- **PKM-OS v1.2 Structure**: UID-based organization with alias system for human-readable names
- **Project Files**: Located in `var/proc/[context]/[UID]/` with UID-based naming

### File Naming Conventions

- **Content files**: `YYYYMMDDHHmm.md` format (UID-based)
- **Daily notes**: `YYYY-MM-DD.md` format in `var/log/daily/`
- **Meeting notes**: `YYYYMMDDHHmm.md` format in `var/log/meetings/`
- **Templates**: `tpl-[Type].md` in `etc/templates/`
- **System files**: Descriptive names (e.g., `personal-knowledge-os.md`)

### Obsidian Integration

- **Aliases**: All content files have `aliases: ["Human Readable Name"]` in frontmatter
- **Auto-completion**: Type `[[Project Name]]` → auto-completes to `[[202501091445]]`
- **Linking**: Use aliases for natural linking, Obsidian resolves to UIDs automatically
- **File Explorer**: Consider "Frontmatter Alias Display" plugin to show aliases

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

### PKM-OS v1.2 Directory Structure

```
/
├── etc/                    # System configuration
│   ├── templates/          # Note templates (tpl-*.md)
│   └── workflows/          # Scripts and procedures
├── var/                    # Active workspace
│   ├── [UID].md           # System spool file
│   ├── cache/maps/        # Generated MOCs
│   ├── log/daily/         # Daily logs (YYYY-MM-DD.md)
│   ├── log/meetings/      # Meeting notes (UID format)
│   └── proc/[context]/[UID]/  # Active projects
├── lib/[context]/[UID].md  # Reference library
├── archive/               # Completed processes
└── tmp/                   # Temporary files
```

### Search Priority

Use Vaultmap.yaml guidance for search priority:

- **High Priority**: `var/proc/`, `lib/`, `etc/`, `var/cache/maps/`
- **Medium Priority**: `var/log/daily/`, `var/log/meetings/`, `var/[UID].md`
- **Low Priority**: `tmp/`, `archive/`

### Person References

- Use `[[Name]]` format for person references
- Store person notes in `lib/network/[UID].md`
- Creates bidirectional connections automatically
- Use aliases for natural referencing

### Daily Notes

- Template: `etc/templates/tpl-daily-log.md`
- Location: `var/log/daily/YYYY-MM-DD.md`
- All daily notes are in single flat structure

### Project System

- **Professional**: Business client work (`var/proc/professional/[UID]/`)
- **Personal**: Personal development (`var/proc/personal/[UID]/`)
- **Network**: Community activities (`var/proc/network/[UID]/`)
- **Hive**: Relationship projects (`var/proc/hive/[UID]/`)

### Context Types

**Professional**: Business client work and professional projects
**Personal**: Personal development and individual projects  
**Network**: Community and networking projects
**Hive**: Relationship and family projects

### File Creation Rules

- **NEVER create files** unless absolutely necessary
- **ALWAYS prefer editing** existing files over creating new ones
- **NEVER proactively create documentation** files unless explicitly requested
- **Update Vaultmap.yaml** when creating/deleting files

### Metadata Requirements

All files must have proper YAML frontmatter based on type:

- **Projects**: `type: project`, `status: active`, `context: [context]`, `uid: YYYYMMDDHHmm`, `aliases: ["Name"]`, `created: YYYY-MM-DD`
- **Reference**: `type: reference`, `topic: [topic]`, `uid: YYYYMMDDHHmm`, `aliases: ["Name"]`, `created: YYYY-MM-DD`
- **Daily**: `type: daily_log`, `date: YYYY-MM-DD`, `created: YYYY-MM-DD`
- **Meeting**: `type: meeting`, `date: YYYY-MM-DD`, `uid: YYYYMMDDHHmm`, `aliases: ["Name"]`, `created: YYYY-MM-DD`
- **Templates**: `type: template`, `created: YYYY-MM-DD`
- **MOCs**: `type: moc`, `created: YYYY-MM-DD`

### Technical Environment

User primarily works in:

- **Neovim** with obsidian.nvim plugin
- **WezTerm** terminal
- **Todoist** for task management (external)

### Script Commands

- Various analysis scripts in `etc/workflows/` for time tracking and data analysis
- Workflow procedures and automation scripts

### Neovim Configuration

Update obsidian.nvim configuration for v1.2:

```lua
daily_notes = {
  folder = "var/log/daily",
  date_format = "%Y-%m-%d",
  template = "etc/templates/tpl-daily-log.md",
},

templates = {
  folder = "etc/templates/",
  date_format = "%Y-%m-%d",
  time_format = "%H:%M",
},

note_id_func = function(title)
  -- Generate UID format: YYYYMMDDHHmm
  return os.date("%Y%m%d%H%M")
end,
```

---

_For complete PKM-OS documentation, see: `etc/personal-knowledge-os.md`_
_For system maps and MOCs, see: `var/cache/maps/`_