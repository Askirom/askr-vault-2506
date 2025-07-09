# A Day in the PKM-OS: A Practical Workflow

This document is your reference guide for a typical busy day. It shows how to use your PKM-OS to seamlessly handle professional work, personal tasks, and social planning.

### **Morning (08:00) - The Daily Boot-Up**

**Goal:** To get oriented and define the day's priorities.

1. **Open your Daily Log:**
    
    - **Action:** Go to `var/log/dly/` and open today's note (e.g., `2025-07-10.md`). If it doesn't exist, create it using your `TPL-Daily-Log` template.
        
    - **OS Analogy:** The system boots up and loads the main log file for the day.
        
2. **Check the Scheduler (Todoist):**
    
    - **Action:** Open your "Today" or "Priority" view in Todoist. This is your list of scheduled processes for the day.
        
    - **OS Analogy:** The process scheduler presents the queue of tasks ready to be run.
        
3. **Plan the Day:**
    
    - **Action:** In your Daily Log note, add your first log entry.
        
    - **Log Entry:** `[2025-07-10 08:05] - PLAN: Today's focus is the ARA audit report and planning the weekend trip.`
        

### **Morning (09:00) - Deep Work: Professional Context**

**Goal:** To make progress on a key client project.

1. **Activate the Process:**
    
    - **Action:** In Todoist, find the task "Draft ARA audit report." Click the Obsidian URL in its description.
        
    - **OS Analogy:** The scheduler dispatches a process. The kernel loads the Process Control Block and its memory space.
        
2. **Execute and Log:**
    
    - **Action:** The project note `_project-ara-q3-audit.md` opens in Obsidian. You begin working. As you complete chunks of work, you add to the `Action Log` at the bottom of _that project note_.
        
    - **Log Entries:**
        
        - `[2025-07-10 09:15] - REVIEW: Read through the final evidence documents.`
            
        - `[2025-07-10 10:30] - DRAFT: Wrote sections 1 and 2 of the final report.`
            
        - `[2025-07-10 10:45] - PLAN: Outlined the remaining sections to be written tomorrow.`
            

### **Midday (12:30) - Context Switch: Social Context**

**Goal:** Handle an incoming request from a friend without losing your work context.

1. **Ingest the Interrupt:**
    
    - **Action:** A friend messages you: "Are we still on for dinner Saturday? Where should we go?" You can't decide now. You use Obsidian's quick-capture to create a new note in your `var/inb/` folder. The note is named `dinner-with-friend.md` and contains "Decide on restaurant for Saturday dinner."
        
    - **OS Analogy:** An external interrupt arrives. The kernel saves it to a buffer (`inb/`) for later processing so it doesn't disrupt the currently running process.
        

### **Afternoon (14:00) - Context Switch: Hive Context**

**Goal:** Collaborate with your girlfriend on a shared goal.

1. **Activate the Process:**
    
    - **Action:** Your girlfriend asks about the weekend trip plans. You open Todoist, find the task "Plan weekend trip," and click the link to open the project note `_project-plan-weekend-trip.md` in `var/prc/personal/`.
        
2. **Execute and Log External Actions:**
    
    - **Action:** You discuss options together. She books the train tickets. You log this action in the project note, using the `(Optional Actor)` field.
        
    - **Log Entries:**
        
        - `[2025-07-10 14:10] - REVIEW: Checked train times and hotel availability together.`
            
        - `[2025-07-10 14:25] - DECIDE: Agreed on the 10:00 train and the "Grand Hotel".`
            
        - `[2025-07-10 14:30] - COMMUNICATE (GF): Booked the train tickets online.`
            

### **End of Day (17:00) - The Daily Shutdown**

**Goal:** To process any loose ends and cleanly end the workday.

1. **Process the Inbox:**
    
    - **Action:** You look in your `var/inb/` folder and see the `dinner-with-friend.md` note. It's a simple task, not a full project. You add it directly to Todoist as a new task: "Decide on restaurant and text friend." You then delete the note from your `inb/`. Your inbox is now empty.
        
    - **OS Analogy:** The kernel processes the I/O buffer, dispatching tasks and clearing the buffer.
        
2. **Final Log Entry:**
    
    - **Action:** You open your Daily Log note (`var/log/dly/2025-07-10.md`) one last time.
        
    - **Log Entry:** `[2025-07-10 17:05] - REVIEW: Checked project statuses. Work day complete.`
        

This workflow ensures that every piece of information and every action has a clear, logical place in your system, no matter what context it comes from.