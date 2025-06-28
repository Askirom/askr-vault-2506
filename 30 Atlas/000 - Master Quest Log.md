# Master Quest Log

## Main Quests (The Askirom Saga)

```dataview
TABLE status, winCondition as "Objective"
FROM "20 Quests"
WHERE type = "Quest" AND questType = "Main"
```

---

## Active Milestones (Revenue Tracking)

```dataview
TABLE estimatedValue as "Value", estimatedXP as "XP", status, contact, deadline
FROM "20 Quests"
WHERE type = "Milestone" AND status != "completed"
SORT estimatedValue desc
```

---

## Guild Quests (The Consultant's Ledger)

```dataview
TABLE status, client
FROM "20 Quests"
WHERE type = "Quest" AND questType = "Guild"
```
