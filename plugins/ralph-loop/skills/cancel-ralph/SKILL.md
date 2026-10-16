---
name: cancel-ralph
description: "Cancel active Ralph Loop"
---

# Cancel Ralph

To cancel the Ralph loop:

1. Check if `.claude/ralph-loop.local.md` exists using run_command: `test -f .claude/ralph-loop.local.md && echo "EXISTS" || echo "NOT_FOUND"`

2. **If NOT_FOUND**: Say "No active Ralph loop found."

3. **If EXISTS**:
   - view_file `.claude/ralph-loop.local.md` to get the current iteration number from the `iteration:` field
   - Remove the file using run_command: `rm .claude/ralph-loop.local.md`
   - Report: "Cancelled Ralph loop (was at iteration N)" where N is the iteration value
