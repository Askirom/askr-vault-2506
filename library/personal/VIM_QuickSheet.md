---
type: reference
topic: personal
created: 2025-07-08
---

## ⚡ Vim for Fast Text Editing (Obsidian & Zed)

### ✏️ Insert / Append
- `i` → insert before cursor  
- `a` → append after cursor  
- `I` → insert at start of line  
- `A` → append at end of line  
- `o` / `O` → new line below / above  

### 🔁 Change / Delete / Yank
- `ciw` → change inner word  
- `cw` / `dw` / `yw` → change / delete / yank word  
- `x` → delete character  
- `s` → substitute character (delete + insert)  
- `cc` → change whole line  
- `dd` / `yy` / `p` / `P` → delete / copy / paste line  

### 🔀 Replace / Edit Ranges
- `C` → change to end of line  
- `ci"` / `ci'` / `ci(` / `ci{` → change inside quotes / brackets  
- `ca"` → change around quotes (includes the quotes)

### 🧱 Line Operations
- `>>` / `<<` → indent / unindent  
- `J` → join with next line  

### 🚀 Navigation
- `w` / `b` → next / previous word  
- `0` / `^` / `$` → start / first char / end of line  
- `gg` / `G` → top / bottom of file  
- `Ctrl + d` / `Ctrl + u` → half page down / up  

### 🔁 Repeat / Undo
- `.` → repeat last change  
- `u` / `Ctrl + r` → undo / redo  

### 🎯 Quick Examples
- Add bullet below: `o- <text><Esc>`  
- Replace word: `ciw<new word><Esc>`  
- Replace to end of line: `C<new text><Esc>`  
- Wrap word in quotes: `ciw"<Esc>pa"<Esc>`  
- Move line up: `ddkP`

> 🧠 Tip: Use tags for structure, and annotations for detail in tools like Timewarrior!

## 🚀 Advanced Vim-Obsidian Workflows

### 1. Rapid Task Management with `obsidian-tasks-plugin`

**Purpose:** Efficiently capture, manage, and query tasks across your vault, especially useful for daily notes and project tracking.

**Steps:**

1.  **Add a New Task:**
    *   Navigate to the line where you want to add a task (e.g., in your daily note `02 Daily/2025-07-01.md`).
    *   In **Normal mode**, press `o` to create a new line below the current one and enter Insert mode.
    *   Type your task: `- [ ] Your task description #tag/project ^block-id` (e.g., `- [ ] Review SECUD audit report #SECUD/Audit ^secud-audit-20250701`).
    *   Press `Esc` to return to Normal mode.
    *   *Pro-tip:* If adding multiple tasks, after the first, move to a new line and press `.` (dot command) to repeat the `o- [ ]` and then type the rest of the task.

2.  **Mark a Task Complete:**
    *   Navigate to the task line you want to complete.
    *   In **Normal mode**, place your cursor on the space after `[`.
    *   Press `s` (substitute character) to delete the space and enter Insert mode.
    *   Type `x` and press `Esc`. The task is now `- [x]`.

3.  **Query Tasks (in a dedicated note like `01 Nexus/000 - Master Quest Log.md`):**
    *   In **Normal mode**, navigate to where you want your task query.
    *   Press `o` to create a new line and enter Insert mode.
    *   Type the `tasks` code block:
        ```
        
        ```
    *   Press `Esc` to return to Normal mode. Obsidian's Tasks plugin will render the query.

### 2. Extracting a Selection to a New Note (Refactoring)

**Purpose:** Break down large notes into smaller, atomic notes, improving linkability, searchability, and organization.

**Steps:**

1.  **Select Text to Extract:**
    *   In **Normal mode**, move your cursor to the beginning of the text block you want to extract.
    *   Press `V` (Shift + v) to enter **Visual Line mode**.
    *   Use `j` or `k` to select all the lines you wish to extract.

2.  **Cut the Selection:**
    *   Press `d` to cut the selected lines. They are now in your Vim register.

3.  **Create a New Note Link:**
    *   Navigate to where you want to link to the new note in your current file.
    *   In **Insert mode** (press `i` or `a`), type `[[New Note Title]]` (e.g., `[[SECUD Audit Findings]]`).
    *   Press `Esc` to return to Normal mode.

4.  **Open and Populate the New Note:**
    *   Place your cursor on the newly created `[[New Note Title]]` link.
    *   Press `gd` (Obsidian's default hotkey for "Go to definition" or "Open link under cursor"). This will create and open the new note.
    *   In the new, empty note, press `p` to paste the content you cut earlier.

5.  **Save and Return:**
    *   In **Normal mode**, type `:wq` and press Enter to save and close the new note. You will be returned to your original note.

### 3. Efficient Daily Note Navigation & Templating

**Purpose:** Quickly access, create, and populate your daily notes, leveraging Obsidian's core Templates plugin for consistent structure.

**Steps:**

1.  **Go to Today's Daily Note:**
    *   Use Obsidian's built-in hotkey (default is often `Ctrl/Cmd + Shift + D`). This will open or create today's note (e.g., `02 Daily/2025-07-01.md`).

2.  **Apply a Template (using Obsidian's core Templates plugin):**
    *   *Pre-requisite:* Ensure Obsidian's core "Templates" plugin is enabled and configured to point to your `TEMPLATES/` folder.
    *   Once in your daily note, open the Obsidian Command Palette (`Ctrl/Cmd + P`).
    *   Start typing `Insert template` and select the command.
    *   A list of your templates will appear. Select `Template Daily Log` (or whatever your daily template is named). This will insert the template content into your note.

3.  **Navigate to Previous/Next Daily Note (Vim-style):**
    *   While in a daily note, you can use Obsidian's hotkeys (if configured, often `Ctrl/Cmd + Alt + Left Arrow` for previous, `Right Arrow` for next).
    *   **Vim-style alternative for specific date navigation:**
        *   In **Normal mode**, navigate to the date in the note's title (e.g., `2025-07-01`).
        *   To go to the previous day:
            *   Place your cursor on the last digit of the day (`1` in `01`).
            *   Press `Ctrl + a` (increment number under cursor) to change `01` to `02`.
            *   Then press `Ctrl + x` (decrement number under cursor) twice to change `02` to `00` and then `31` (if the month allows). This is a bit clunky for dates, but demonstrates the number manipulation.
            *   A more direct way for dates: Place your cursor on the `1` in `01`. Press `r0` to change it to `0`. Then `r3` to change it to `3`. Now you have `03`. Then `r0` to change it to `0`. Now you have `00`. Then `r3` to change it to `3`. Now you have `30`.
            *   Once the date is `2025-06-30`, place your cursor on the modified date in the title and press `gd` to open that specific daily note.
