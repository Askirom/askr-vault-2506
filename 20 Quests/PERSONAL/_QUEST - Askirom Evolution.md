---
type: Quest
questType: Main
status: active
area: Personal
winCondition: "Master the 4-stage evolution system for personal productivity and professional excellence"
---

# QUEST - Askirom Evolution

> [!quote]
> **The Evolution Roadmap**: From Tutorial to Mastery - a systematic approach to building sustainable productivity habits while maintaining energy and achieving professional excellence.

## Evolution Stages

### Current Progress
```dataview
TABLE status, progress as "Progress", winCondition as "Objective"
FROM "20 Quests/PERSONAL/Askirom Evolution"
WHERE type = "Stage"
SORT file.name asc
```

### Stage Overview
- **[[Stage 0 - Tutorial (First 90 Days)]]** - Foundation habits and core objectives
- **[[Stage 1 - Adept (Months 4-6)]]** - Consistency and consolidation
- **[[Stage 2 - Expert (Months 7-12)]]** - Strategic application and influence
- **[[Stage 3 - Master (Year 2+)]]** - Effortless integration and generosity

## Action Log & Tasks

- [ ] TODO Complete Stage 0 baseline assessment 📅 2025-07-01
- [ ] TODO Set up daily hyperfocus ritual tracking
- [ ] TODO Implement weekly system review process
- [ ] TODO Review and update stage progression criteria

## Milestones

## Stage Milestones

```dataview
TABLE estimatedXP as "XP", status, deadline, winCondition as "Win Condition"
FROM "20 Quests"
WHERE type = "Milestone" AND parentQuest = this.file.link
SORT deadline asc
```

## Evolution Metrics

### Core Stats Tracking
- **Deep Work Blocks**: Target progression from 5/week → 12/week
- **Weight Management**: 85kg → 77kg → 68-72kg maintenance
- **ISO Study Progress**: Annex A memorization → Lead Auditor cert
- **System Mastery**: ≤30min/month on system tweaks at Stage 3

### Habit Formation
- **Daily Rituals**: Hyperfocus Lite → Pro → Creator Mode → Invisible System
- **Weekly Reviews**: System Binder → v2 → Influence Review → Heartbeat
- **Monthly Focus**: Friction removal → Writing → Show work → Mentoring

## Meeting Notes

## Key Documents
- [[30 Atlas/Askirom v2506 - Shadow Bolt]] - Current character sheet
- [[Stage 0 - Tutorial (First 90 Days)]] - Foundation stage guide
- [[Stage 1 - Adept (Months 4-6)]] - Consolidation stage guide
- [[Stage 2 - Expert (Months 7-12)]] - Strategic stage guide
- [[Stage 3 - Master (Year 2+)]] - Mastery stage guide
