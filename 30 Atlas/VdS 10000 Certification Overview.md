# VdS 10000 Certification Overview

## Active VdS 10000 Engagements

```dataview
TABLE 
  client as "Client",
  status as "Status", 
  vdsStandard as "Standard",
  certificationTarget as "Cert Target"
FROM "20 Quests/PROFESSIONAL"
WHERE type = "Quest" AND vdsStandard = "VdS 10000"
SORT certificationTarget asc
```

## Milestone Progress by Phase

### Assessment Phase
```dataview
TABLE 
  parentQuest as "Client",
  winCondition as "Objective",
  status as "Status",
  estimatedValue as "Value (€)"
FROM "20 Quests/PROFESSIONAL"
WHERE type = "Milestone" AND vdsPhase = "assessment"
SORT status asc, parentQuest asc
```

### Implementation Phase
```dataview
TABLE 
  parentQuest as "Client",
  winCondition as "Objective", 
  status as "Status",
  estimatedValue as "Value (€)"
FROM "20 Quests/PROFESSIONAL"
WHERE type = "Milestone" AND vdsPhase = "implementation"
SORT status asc, parentQuest asc
```

### Certification Phase
```dataview
TABLE 
  parentQuest as "Client",
  winCondition as "Objective",
  status as "Status", 
  estimatedValue as "Value (€)"
FROM "20 Quests/PROFESSIONAL"
WHERE type = "Milestone" AND vdsPhase = "certification"
SORT status asc, parentQuest asc
```

## Financial Overview

**Total VdS 10000 Pipeline:**
```dataview
TABLE WITHOUT ID
  sum(rows.estimatedValue) as "Total Pipeline Value (€)"
FROM "20 Quests/PROFESSIONAL"
WHERE type = "Milestone" AND vdsPhase != null
```

**By Phase:**
```dataview
TABLE 
  vdsPhase as "Phase",
  sum(estimatedValue) as "Value (€)"
FROM "20 Quests/PROFESSIONAL"
WHERE type = "Milestone" AND vdsPhase != null
GROUP BY vdsPhase
SORT vdsPhase asc
```