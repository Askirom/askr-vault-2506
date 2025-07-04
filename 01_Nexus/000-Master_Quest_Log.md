# Master Quest Log

## Main Quests (The Askirom Saga)

```dataview
TABLE status, winCondition as "Objective"
FROM "20_Quests"
WHERE type = "Quest" AND questType = "Main"
```

---

## Guild Quests (Professional Client Work)

```dataview
TABLE status, client
FROM "20_Quests"
WHERE type = "Quest" AND questType = "Guild"
```

---

## Side Quests (Network & Learning)

```dataview
TABLE status, area, client
FROM "20_Quests"
WHERE type = "Quest" AND questType = "Side"
```

---

## Hive Quests (Relationship)

```dataview
TABLE status, winCondition as "Objective"
FROM "20_Quests"
WHERE type = "Quest" AND questType = "Hive"
```
