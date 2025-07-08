---
id: GUILD-secudor_GmbH
aliases: []
tags: []
guildName: secudor GmbH
status: active
type: moc
created: 2025-07-08
---

# The secudor GmbH Guild Charter

> [!quote]
> We are the guardians of the digital frontier, the architects of resilience. We don't just manage risk; we build trust in a world of uncertainty.

---

## Mandate

The Secudor Guild is dedicated to the protection of information and the preservation of digital sovereignty. Our agents are dispatched to entities across the realms to establish order, mitigate threats, and build robust defenses against the chaotic forces of the digital age.

## My Role: Agent Askirom

As an agent of the Guild, my purpose is to execute the contracts assigned to me with precision, wisdom, and integrity. Each client is a Quest, and each successful outcome strengthens both the client and the Guild itself.

The resources and experience gained from these Guild Quests are the fuel for my personal growth and the advancement of my Main Quests.

## Active Guild Quests

```dataview
TABLE status, client as "Client"
FROM "20_Quests"
WHERE type = "Quest" AND questType = "Guild" AND status = "active"
SORT file.mtime desc
```

## Completed Guild Quests

```dataview
TABLE status, client as "Client"
FROM "20_Quests"
WHERE type = "Quest" AND questType = "Guild" AND status = "completed"
SORT file.mtime desc
```
