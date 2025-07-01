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

## ✔️ Tasks

```tasks
not done
path includes 20 Quests/PERSONAL/{{title}}
```

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


## Backlog

```dataview
TABLE status, winCondition as "Win Condition"
FROM "20 Quests"
WHERE type = "Project" AND parentQuest = this.file.link AND status = "backlog"
SORT file.mtime desc
```

---

## Journal

```dataview
TABLE summary as "Summary"
FROM "01 Daily"
WHERE contains(file.outlinks, this.file.link)
SORT file.mtime desc
```