# JCode Performance Guidelines

1. Minimize token waste: never load entire files when specific line ranges suffice.
2. When launching subagents with `invoke_subagent`, choose the most resource-efficient model (`flash` or `flash_lite` for reads/research, `pro` or `inherit` for complex refactors).
3. Always verify changes with focused test commands rather than full test suites when iterating.
