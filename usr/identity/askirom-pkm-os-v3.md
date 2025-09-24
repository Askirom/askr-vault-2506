## Askirom PKM-OS — Folder & Flow Guide

### Folder Map

-   `/etc` → Templates, system rules
-   `/bin` → Repeatable checklists/playbooks
-   `/var`
    -   `/action` → One note per task
    -   `/daily` → Daily notes (by date + rolling)
    -   `/decision` → One note per decision
    -   `/meeting` → Meeting logs (append-only)
-   `/srv`
    -   `///` → Client + project work (deliverables, notes, evidence)
-   `/usr`
    -   `/identity` → Identity docs (Askirom, principles)
    -   `/reference` → General reference notes
    -   `/standards` → Standards/laws (PDFs + sidecars)
    -   `rolodex.md` → Central contacts
-   `/arc` → Archive of closed/old work
-   `/tmp` → Scratch/inbox

---

### Metadata Fields (Minimal Set)

Every note starts with just enough inline Dataview fields:

> type:: action|daily|decision|meeting|project|knowledge|standard
> status:: active|done
> client:: (if relevant)
> project:: <CLIENT-YY-###> (if relevant)

That’s it. Add extras only if they’re useful.

---

### Tasks (Actions)

-   **Stored in**: `/var/action/`
-   **Principle**: One note = one task
-   **Workflow**: Close with `status:: done` and link to output.

**Example:**
> type:: action
> status:: active
> client:: CLIFO
> project:: CLIFO-25-003
> desc:: Draft BIA interview script

---

### Projects

-   **Stored in**: `/srv/<CLIENT>/<CLIENT-YY-###>_<slug>/`
-   **Recommended files**:
    -   `_index.md` → Scope, deliverables, deadlines
    -   `backlog.md` → Planning list
    -   `deliverables/` → Shipped docs
    -   `notes/` → Working notes

**Example:**
> type:: project
> status:: active
> client:: CLIFO
> project:: CLIFO-25-003
> scope:: Notfallplan

---

### Meetings (Rolling Client Logs)

-   **Stored in**: `/var/meeting/`
-   **Principle**: One append-only file per client. New meeting notes are added to the top of the file for reverse chronological order.
-   **File Name**: `CLIENT.md` (e.g., `RCG.md`, `CLIFO.md`)

The file itself contains the log. Each new meeting entry is separated by a horizontal rule (`---`) and begins with a heading that includes the date and topic.
### Decisions

-   **Stored in**: `/var/decision/`

**Example:**
> type:: decision
> status:: done
> client:: RCG
> project:: RCG-25-001
> date:: 2025-09-02
> decision:: Switch to Fastmail
> relates:: [[2025-09-02_RCG_loeschkonzept]]

---

### Daily Notes

-   **Stored in**: `/var/daily/`

**Example:**
> type:: daily
> status:: active
> focus-3:: …
> wins:: …
> issues:: …
> next:: …

---

### Standards

-   **Stored in**: `/usr/standards/`
-   **Format**: PDFs with a sidecar `.md` file for metadata.

**Example:**
> type:: standard
> status:: active
> std:: ch-dsg
> effective:: 2023-09-01

---

### Naming Conventions

-   **Dates**: `YYYY-MM-DD`
-   **Projects**: `<CLIENT-YY-###>_<slug>`
-   **Meetings**: `YYYY-MM-DD_CLIENT_topic.md`
-   **Rule**: Keep filenames short and ASCII-safe.