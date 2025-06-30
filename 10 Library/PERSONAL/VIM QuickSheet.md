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