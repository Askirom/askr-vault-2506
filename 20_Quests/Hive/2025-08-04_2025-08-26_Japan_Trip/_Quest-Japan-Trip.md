---
id: _Quest-Japan-Trip
aliases: []
tags: []
area: Personal
questType: Main
status: active
type: Quest
winCondition: ""
---

# Quest: \_Quest-Japan-Trip

> [!quote]

## ✔️ Tasks

```tasks
not done
path includes 20_Quests/Personal/_Quest-Japan-Trip
```

```dataview
TABLE status, winCondition as "Objective"
FROM "20_Quests/Personal/_Quest-Japan-Trip"
WHERE type = "Milestone" AND parentQuest = this.file.link
SORT file.mtime desc
```

## Active Projects

```dataview
TABLE status, winCondition as "Win Condition"
FROM "20_Quests"
WHERE type = "Project" AND parentQuest = this.file.link AND status = "active"
SORT file.mtime desc
```

## Completed Projects

```dataview
TABLE status, winCondition as "Win Condition"
FROM "20_Quests"
WHERE type = "Project" AND parentQuest = this.file.link AND status = "completed"
SORT file.mtime desc
```

## Backlog

```dataview
TABLE status, winCondition as "Win Condition"
FROM "20_Quests"
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

## Backlog

```dataview
TABLE status, winCondition as "Win Condition"
FROM "20_Quests"
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

