---
id: PKM-os-resources
aliases: []
tags: []
---

# PKM-OS: The Core Resource Analogy

This document outlines the foundational analogy of the entire Personal Knowledge Operating System.  
The system is designed to be a management layer for your finite biological resources by modeling them on their computer equivalents.

## The Core Mapping

| Computer Resource      | Human Equivalent            | How the PKM-OS Manages It                                          |
| ---------------------- | --------------------------- | ------------------------------------------------------------------ |
| CPU (Processing Power) | Attention / Focus           | Minimizes context switching — the biggest drain on your attention. |
| RAM (Working Memory)   | Short-Term Mental Workspace | Acts as external RAM by offloading memory into structured files.   |
| Energy (Power Supply)  | Willpower / Physical Energy | Conserves energy by reducing friction and disorganization.         |

---

## 1. CPU Load ↔️ Attentional Load

Your attention is your single processing core.  
You can only truly focus on one complex task at a time.  
Multitasking or frequent interruptions spike your "attentional load" — performance plummets like a CPU at 100% usage.

### How your OS manages your "CPU":

- **The Scheduler** (`Todoist`):  
  Acts as your process scheduler. Prevents running ten "programs" at once. Enforces single-tasking by presenting one clear priority at a time.

- **The Inbox** (`var/inb/`):  
  Functions as your interrupt handler. Captures distracting inputs without hijacking focus. Keeps your current task running undisturbed.

- **The Process Structure** (`var/proc/`):  
  Encapsulated project folders act like pre-loaded apps. Clicking a task loads the full context instantly. No wasted "CPU cycles" trying to recall what’s next.

---

## 2. RAM Usage ↔️ Working Memory

Working memory is the brain’s tiny scratchpad — volatile, limited, and easily overwhelmed.

### How your OS manages your "RAM":

- **The Process File** (`_project-note.md`):  
  External RAM for a task. Holds project details, next steps, and key facts — freeing your brain for deep work.

- **The Action Log**:  
  Stores what’s been done and what’s next. Frees mental space by holding your current state externally.

- **The Library** (`lib/`):  
  External long-term storage — your "hard drive". You don’t need to memorize the ISO 27001 standard. Just know it’s in `lib/`. Your brain stays clear for active tasks.

---

## 3. Energy ↔️ Willpower & Physical Stamina

This is your biological power supply.  
Sleep deprivation, decision fatigue, and chaos all drain it.

### How your OS conserves Energy:

- **Reduced Friction**:  
  A clear, trustworthy system saves energy otherwise wasted on meta-decisions, searching, or wondering what to do next.

- **Decision Offloading** (`log/dec/`, `log/rev/`):  
  You make a decision once, log it, and trust it. Avoids the trap of constant re-evaluation.

- **Clarity Reduces Stress**:  
  Chaos is stressful — and stress drains energy. A calm, controlled OS is inherently more energy-efficient.

