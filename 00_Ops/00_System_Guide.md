You are right. I missed the `00_Ops` container in the final output. Here is the corrected, complete manual in the Markdown code block.

Markdown

````
## PKM Ops V1.3 — Operational Manual

**Core Philosophy:** Logistics for storage (`00`-`99`). Command for strategy (`HQ`).
**The Hierarchy:** Director (HQ) → Lead (Strategy) → Analyst (Log).

---

### 1. The Territory (Folder Map)

Top-level structure. **`00_Ops`** is the Command Center; everything else is storage.

- **`00_Ops`** (Command Module)
    - _Contains the files that run the system._
    - `00_HQ.md` (Director's View)
    - `YYYY-MM-log.md` (Execution Log)
    - `00_System_Guide.md` (This file)
- **`01_Inbox`**
    - Dump zone for raw signals, screenshots, PDFs. Must be processed weekly.
- **`10_Projects`** (Active Theaters)
    - Contains active client folders.
- **`20_Reference`** (The Library)
    - Standards (ISO 27001, GDPR), Technical Cheatsheets, Laws.
- **`30_Tools`** (The Workshop)
    - `01_Audit_Kits` (Checklists)
    - `02_Technical` (Scripts)
    - `03_Business` (Templates)
- **`40_Admin`** (Business Ops)
    - Invoices, Tax, Contracts, CRM.
- **`99_Archive`**
    - Closed projects and old logs.

---

### 2. Project Folder Standard

Every client folder inside `10_Projects` must follow this strict structure.

**Path:** `10_Projects / <Client_Name> /`

- **`00_Strategy.md`**: The OODA Loop and Win Conditions. (_See Template below_)
- **`01_Admin`**: Contracts, SOW, NDA, Contact info.
- **`02_Input`**: **Read-Only**. Evidence, logs, screenshots provided by client.
- **`03_Work`**: Scratchpad, drafts, meeting notes. The "Messy Kitchen."
- **`04_Output`**: Final PDFs/Reports sent to client. The "Showroom."

---

### 3. The Command Stack (Templates)

#### LEVEL 1: The Director (Portfolio View)

**File:** `00_Ops/00_HQ.md`
**Role:** Resource Allocation & Oversight.
**Frequency:** Every Morning.

```markdown
# HEADQUARTERS

**Date:** YYYY-MM-DD
**Workload:** High | Normal | Low

## 1. THEATER OVERVIEW (Status)
* **[[Client A - Audit]]:** 🟡 BLOCKED. Waiting on logs.
* **[[Client B - Pentest]]:** 🟢 ON TRACK. Drafting.
* **[[Internal Admin]]:** 🔴 URGENT. VAT filing.

## 2. DIRECTIVES (The Focus)
1. Unblock Client A (Escalate to CISO).
2. Finish VAT filing by noon.

## 3. RADAR (Incoming)
* New EU AI Act regulation drafts.
* Potential lead: Bank of Bavaria.
````

#### LEVEL 2: The Lead (Project Strategy)

File: 10_Projects/<Client>/00_Strategy.md

Role: OODA Loop & Planning.

Frequency: Before starting work on the project.

Markdown

```
# Strategy: [Client Name]

## 1. OBJECTIVES (Win Conditions)
* [ ] ISO 27001 Certificate Issued.
* [ ] Final Invoice Paid.
* **Current Phase:** Remediation.

## 2. ANALYSIS (OODA)
* **Observe:** Client has stopped sending evidence.
* **Orient:** They are likely hiding a gap in Access Control.
* **Decide:** Shift approach. Stop emailing, schedule a workshop.

## 3. NEXT ACTIONS (The Moves)
* [ ] Schedule call with CISO.
* [ ] Review `02_Input` for partial evidence.
```

#### LEVEL 3: The Analyst (Execution Log)

File: 00_Ops/YYYY-MM-log.md (e.g., 2025-11-log.md)

Role: Execution & Billing Context.

Frequency: All day.

Markdown

```
## 2025-MM-DD (Day)

**Focus:**
- [ ] Call CISO
- [ ] Send VAT

**Log:**
- 09:00: **Client A** (Clockodo: Active)
    - Call with Anna.
    - *Intel:* Confirmed IT team quit.
    - *Action:* Updated Strategy note.
- 11:30: **Admin**
    - Sent VAT files.
```

---

### 4. The Workflow (SOP)

1. **Morning Standup (The HQ):**
    
    - Open `00_Ops/00_HQ.md`.
        
    - Check project statuses.
        
    - Set the "Directives" for the day.
        
2. **Engagement (The Strategy):**
    
    - _Never_ just open a file and type.
        
    - Open `10_Projects/<Client>`.
        
    - Read `00_Strategy.md`.
        
    - **Orient:** Is the plan still valid? If not, update it.
        
    - **Act:** Move to `03_Work` to execute.
        
3. **Execution (The Log):**
    
    - Track time in Clockodo (Quantitative).
        
    - Track context in `00_Ops/YYYY-MM-log.md` (Qualitative).
        
    - Create Meeting Notes in `03_Work` named `YYYY-MM-DD - Topic`.
        
4. **Completion (The Archive):**
    
    - When a project ends, verify `04_Output` contains all deliverables.
        
    - Move folder to `99_Archive`.
        

---

### 5. Rules of Engagement

1. **No Action Without Orientation:** Do not add a task to your daily list without checking the Project's `00_Strategy` note first.
    
2. **Separate Church and State:**
    
    - **Evidence** (`02_Input`) is read-only (Liability).
        
    - **Work** (`03_Work`) is messy (Drafting).
        
    - **Output** (`04_Output`) is pristine (Deliverables).
        
3. **The "Stalled" Rule:** If a project hasn't moved in 3 days, mark it 🟡 in `00_HQ.md`. If 7 days, mark it 🔴.
    
4. **Log Reality:** If you planned to work but got distracted, log the distraction. The Log is the source of truth, not the plan