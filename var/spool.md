---
type: SPOOL
uid: spool
aliases: ["System Inbox"]
created: 2025-07-11
---

# PKM-OS System Spool (Inbox)

_FIFO pipe for capturing all incoming items before processing_

## Processing Rules
- Append new items with timestamp
- Process daily: promote to units, reference, or archive
- Keep this file clean - it should only contain unprocessed items

## Unprocessed Items

_Add new items here with format: [YYYY-MM-DD HH:MM] - Description_

- 

---

## Recently Processed

_Move processed items here before final cleanup_

- [2025-07-11 16:45] TESTCO client inquiry → Processed as test unit (archived)
