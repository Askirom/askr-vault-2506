# Master Quest Log

## Main Quests (The Askirom Saga)

```dataview
TABLE status, winCondition as "Objective"
FROM "20 Quests"
WHERE type = "Quest" AND questType = "Main"
```

---

## Guild Quests (The Consultant's Ledger)

```dataview
TABLE status, client
FROM "20 Quests"
WHERE type = "Quest" AND questType = "Guild"
```
