---
type: Quest
questType: Main
status: active
area: Personal
winCondition: ""
targetXP: 0
earnedXP: 0
---

# Quest: {{title}}

> [!quote]
> 

## XP Progress
**Target XP:** `= this.targetXP`  
**Current XP:** `= this.earnedXP`  
**Progress:** `= round((this.earnedXP / this.targetXP) * 100, 1)`%

```dataview
TABLE estimatedXP as "Est. XP", earnedXP as "Earned XP", status as "Status", winCondition as "Win Condition"
FROM "20 Quests"
WHERE type = "Milestone" AND parentQuest = this.file.link
SORT status asc, file.mtime desc
```

## Milestones

## Active Projects

```dataview
TABLE status, winCondition as "Win Condition"
FROM "20 Quests"
WHERE type = "Project" AND parentQuest = this.file.link AND status = "active"
SORT file.mtime desc
```

## Completed Projects

```dataview
TABLE status, winCondition as "Win Condition"
FROM "20 Quests"
WHERE type = "Project" AND parentQuest = this.file.link AND status = "completed"
SORT file.mtime desc
```
