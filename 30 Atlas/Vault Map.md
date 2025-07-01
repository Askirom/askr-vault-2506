# Vault Map - Dynamic Index

*Last Updated: 2025-07-01*

```yaml
vault_structure:
  name: "Askr.Vault-2506"
  total_files: 200+
  last_scan: "2025-07-01"
  
  folders:
    "00_to_sort":
      purpose: "Temporary staging, unorganized content"
      key_files:
        - "Inbox - Tasks.md"
        - "Time Tracking Analysis - June 2025.md"
      file_count: 15
      
    "01_nexus":
      purpose: "Central command, high-level coordination"
      key_files:
        - "000 - Master Quest Log.md"
        - "GEAR - Askirom Inventory v2506.md" 
        - "GUILD - secudor GmbH.md"
      file_count: 8
      
    "02_daily":
      purpose: "Daily logs, time-based tracking"
      pattern: "YYYY-MM-DD.md"
      date_range: "2025-04-23 to 2025-07-01"
      file_count: 45
      
    "10_library":
      purpose: "Reference materials, organized by category"
      subfolders:
        HIVE:
          file_count: 0
          status: "reserved"
        NETWORK:
          file_count: 8
          type: "person_references"
          pattern: "[[Name]] format"
        PERSONAL:
          file_count: 6
          type: "personal_reference"
        PROFESSIONAL:
          file_count: 4
          type: "work_reference"
        TEMPLATES:
          file_count: 6
          type: "note_templates"
          key_files:
            - "Template Daily Log.md"
            - "Template Guild Quest.md"
            - "Template Main Quest.md"
            
    "11_attachments":
      purpose: "File storage, media assets"
      organization: "by_context"
      includes: ["PDFs", "images", "contracts", "folder_structures"]
      
    "20_quests":
      purpose: "Active project management, gamified system"
      quest_types: ["guild", "main", "network", "hive"]
      subfolders:
        HIVE:
          file_count: 3
          active_projects: 2
        NETWORK:
          file_count: 6
          active_projects: 3
        PERSONAL:
          file_count: 8
          active_projects: 5
        PROFESSIONAL:
          file_count: 45
          active_clients: 15
          clients:
            - "ARA"
            - "CLIFO" 
            - "EHFREI"
            - "EKIBA"
            - "EMPIC"
            - "FDFRI"
            - "FITS"
            - "GOSME"
            - "INSTO"
            - "RBOMN"
            - "RCG"
            - "SECUD"
            - "VEDES"
            - "VGALT"
            
    "30_atlas":
      purpose: "System documentation, personal framework"
      key_files:
        - "Askirom v2506 - Shadow Bolt.md"
        - "Personal Productivity Framework v2.md"
        - "VdS 10000 Certification Overview.md"
        - "XP_Log.md"
      file_count: 12

  recent_additions:
    "2025-07-01":
      - path: "20 Quests/PROFESSIONAL/SECUD/NIS2-Sprechstunden Hub.md"
        type: "hub_note"
      - path: "20 Quests/PROFESSIONAL/SECUD/NIS2 Begrüßungs-E-Mail Template.md"
        type: "template"
      - path: "20 Quests/PROFESSIONAL/SECUD/NIS2 Vorbereitungs-Fragebogen.md"
        type: "template"
      - path: "20 Quests/PROFESSIONAL/SECUD/NIS2 Ergebnis-Dokument Template.md"
        type: "template"
      - path: "20 Quests/PROFESSIONAL/SECUD/NIS2 Berater-Checkliste.md"
        type: "checklist"
      - path: "20 Quests/PROFESSIONAL/SECUD/NIS2 Anforderungen.md"
        type: "reference"
      - path: "30 Atlas/Vault Map.md"
        type: "system_documentation"

  linking_patterns:
    wikilink_files: 91
    hub_notes:
      - "01 Nexus/000 - Master Quest Log.md"
      - "20 Quests/PROFESSIONAL/SECUD/NIS2-Sprechstunden Hub.md"
    template_usage:
      daily_log: 45
      guild_quest: 15
      milestone: 10
      
  search_shortcuts:
    find_person: "10 Library/NETWORK/"
    find_client: "20 Quests/PROFESSIONAL/[CLIENT]/"
    find_template: "10 Library/TEMPLATES/"
    find_daily: "02 Daily/YYYY-MM-DD.md"
    find_reference: "10 Library/PROFESSIONAL/"
    
  maintenance:
    inbox_location: "00 To Sort/Inbox - Tasks.md"
    master_log: "01 Nexus/000 - Master Quest Log.md"
    quest_pattern: "_QUEST - [Name].md"
    attachment_folder: "11 Attachments"
    
  system_health:
    active_quests: 20
    active_clients: 15
    daily_note_streak: "consistent_april_to_july"
    linking_density: "high"
    template_adoption: "consistent"
```

## Quick Navigation

### 🎯 **Need to find...**
- **A person**: Check `10 Library/NETWORK/`
- **A client project**: Look in `20 Quests/PROFESSIONAL/[CLIENT]/`
- **Today's work**: Current daily note `02 Daily/`
- **A template**: Browse `10 Library/TEMPLATES/`
- **System docs**: Check `30 Atlas/`

### 📋 **Common Patterns**
- Quest files: `_QUEST - [Name].md`
- Daily notes: `YYYY-MM-DD.md`  
- Templates: `Template [Type].md`
- Person notes: `[[Firstname Lastname]]`

### 🔄 **Update Instructions**
When adding/moving files, update the `recent_additions` section with:
- Date
- File path
- File type/purpose

---
*This map should be updated whenever significant vault changes occur*