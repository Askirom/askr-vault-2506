---
type: Quest
questType: Main
status: active
area: Personal
winCondition: ""
---

# Quest: {{title}}

> [!quote]
> 

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
