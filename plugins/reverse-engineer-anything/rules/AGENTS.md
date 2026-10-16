# Reverse Engineer Anything (REA) Guidelines

When `reverse-engineer-anything` is active:
1. Always route target first (ASAR/JS, Android APK, Native ELF/PE/Mach-O, Firmware, WASM, EVM, Network captures).
2. Distinguish observations, inferences, and unknowns. Cite Evidence IDs.
3. Work summary-first to conserve context tokens; drill down only when specific questions remain open.
4. Close opened binary sessions with `close_binary` when analysis completes.
