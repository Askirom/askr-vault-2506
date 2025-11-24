## PKM Logistics V1.1 — Operational Manual

**Purpose:**  
A frictionless personal operations system for consulting work.  
Minimal structure, predictable flow, zero maintenance overhead.

**Core Loop:**  
Intake → Process → Deliver → Archive

---

## 1. Folder Map (Top-Level)

Numbered prefixes enforce stable sorting.

```
00_Inbox/        ← Raw capture, unprocessed
10_Projects/     ← Active client work
20_Reference/    ← Static knowledge & standards
30_Tools/        ← Reusable checklists, templates, scripts
40_Admin/        ← Business operations (invoices, CRM, taxes)
99_Archive/      ← Closed projects & old logs
log.md           ← Single running operational log
```

### Rules for Top-Level Folders
- Do **not** create new top-level folders.  
- Keep structure shallow: 1–2 levels deep max.  
- Folders represent *function*, not topics or categories.

---

## 2. Client Folder Structure (Inside `10_Projects/CLIENT/`)

This structure enforces clean flow and liability separation.

```
01_Admin/    → Contract, SOW, NDA, stakeholder list
02_Input/    → Client-provided evidence (logs, docs, screenshots)
03_Work/     → Drafts, meeting notes, analysis, scratchpad
04_Output/   → Final deliverables (PDFs, reports)
```

### Rules
- **Never modify** files inside `02_Input`.  
- Work always happens in `03_Work`.  
- Deliverables only in `04_Output`.  
- Admin only in `01_Admin`.  
- Do not add more subfolders unless absolutely necessary.

---

## 3. Templates (Stored in `30_Tools/templates/`)

### A. Running Log (`log.md`)
Append new entries at the top. One file for months.  
Create a new file only when size becomes unmanageable.

```markdown
## 2025-11-27 (Thursday)

**Priorities:**
- [ ] Prepare final CLIFO BIA draft
- [ ] Review TOM documentation for EKIB

**Log:**
- 09:00 – Call with Anna (CLIFO). Clarified missing evidence.
- 11:30 – Updated Gap Analysis section 4.2.
- 15:00 – Reviewed contracts in 01_Admin for EKIB.
```

---

### B. Project Dashboard
Filename: `PROJECTCODE - Project Name.md`

```markdown
---
client: [[Client]]
status: Active
deadline: YYYY-MM-DD
contact: [[Name]]
---
# Project: [Project Name]

**Objective:**  
Short description.

**Milestones:**  
- [ ] Kickoff  
- [ ] Interviews  
- [ ] Draft report  
- [ ] Delivery  

**Links:**  
- [[01_Admin]]  
- [[03_Work]]  

**Notes:**  
- Key constraints, risks, reminders.
```

---

### C. Meeting Note
Filename: `YYYY-MM-DD - Client - Topic.md`

```markdown
# Meeting: [Topic]

**Date:** YYYY-MM-DD  
**Participants:** Me, [Client Contact]  

**Context / Agenda:**  
1.  
2.  

**Minutes:**  
-  
-  

**Actions:**  
- [ ] @Me:  
- [ ] @Client:
```

---

## 4. Workflows

### Daily Workflow (Start → Execution → Close)

1. Open **`log.md`**  
2. Add today’s header  
3. Empty **`00_Inbox`**  
   - Move project items → `10_Projects/<Client>/`  
   - Move stable knowledge → `20_Reference/`  
   - Move tools/templates → `30_Tools/`  
4. Work directly inside `03_Work`  
5. Update the Project Dashboard  
6. Log major events in `log.md`

Time: ~5 minutes to start, ~2 minutes to close.

---

### New Project Setup (Intake)

1. Create folder: `10_Projects/<ClientCode>`  
2. Add required subfolders:  
   `01_Admin`, `02_Input`, `03_Work`, `04_Output`  
3. Create Project Dashboard  
4. Move contract/SOW into `01_Admin`  
5. Begin working in `03_Work`

Time: 3–5 minutes.

---

### Project Closure (Archive)

1. Deliver final files → `04_Output`  
2. Ensure invoice steps handled → `40_Admin`  
3. Move entire project folder → `99_Archive/<Year>/`  
4. Update Dashboard status to “Closed”  

Time: 2–3 minutes.

---

## 5. Migration Plan (From PKM-OS V4)

**Goal:** Migrate structure, not content.

### Step 1 — Create New Skeleton (5 min)
Create the top-level folders and `log.md`.

### Step 2 — Migrate Projects (15 min)
- Move active projects from `/srv` → `10_Projects`.  
- Inside each: create `01–04` subfolders.  
- Sort files into their correct places.

### Step 3 — Migrate Knowledge (10 min)
- Move `/usr/reference` + `/usr/standards` → `20_Reference`.  
- Flatten structure — avoid deep subfolders.

### Step 4 — Migrate Tools (5 min)
- Move `/bin` → `30_Tools`.

### Step 5 — Archive Old Logs (5 min)
- Move `/var` → `99_Archive/_OldLogs`.  
- Start fresh `log.md`.

Total: ~45 minutes uninterrupted.

---

## 6. Rules of Operation (Non-Negotiable)

1. **Inbox to Zero Weekly**  
   - The system collapses if 00_Inbox grows.

2. **Evidence Integrity**  
   - Never modify files in `02_Input`.

3. **One-Way Flow**  
   `02_Input → 03_Work → 04_Output`  
   Never backward.

4. **No Metadata Debt**  
   - Use folders + filenames, not tags + systems.

5. **Shallow Hierarchy**  
   - Max depth: 2 levels.  
   - Avoid nested structures unless required by a client.

6. **Bias for Execution**  
   - Notes exist to support deliverables.  
   - If a file no longer contributes, archive or delete.

---

## 7. 30-Day Freeze (Stabilization Phase)

**For the next 30 days:**

- No new plugins  
- No folder renaming  
- No reorganizing  
- No new template structures  
- No cosmetic tweaks  
- Capture friction in `log.md` but don’t fix it yet  
- Only operate the system  

This lets the workflow stabilize before future iteration.

---

## 8. Revision History

- **v1.1** — Refined structure, clarified workflows, removed ambiguity, added operational rules.  
- **v1.0** — Initial logistics-based PKM framework.