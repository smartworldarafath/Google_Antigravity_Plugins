# Antigravity Cheat Codes — The Power-User Glossary

Techniques ranked by impact. Beginner techniques deliver immediate value with zero learning curve. Intermediate techniques compound over time. Advanced techniques are for users building serious workflows.

---

## Tier 1 — Highest impact (start here)

### Be specific about output (Beginner)
Antigravity defaults to balanced, medium-length answers. Tell it exactly what you want: length, format, audience, tone.
**Example:** "Explain GraphQL in 150 words for a non-technical product manager."

### Give Antigravity a role (Beginner)
Assigning a role calibrates expertise, vocabulary, and judgment in one move.
**Example:** "You are a senior security engineer reviewing this code for OWASP Top 10 issues."

### Show, don't tell (few-shot) (Beginner)
Two or three examples of the input-output pattern you want will outperform paragraphs of instructions.
**Example:** Paste 3 sample email replies you like, then ask Antigravity to write a fourth in the same style.

### Ask Antigravity to think before answering (Beginner)
For anything non-trivial, add "think through this step by step before answering" or "show your reasoning". Quality jumps noticeably on multi-step problems.

### Iterate, don't restart (Beginner)
Refine the previous answer rather than re-prompting from scratch. "Make it shorter", "add a counterexample", "now rewrite for executives" all keep accumulated context.

---

## Tier 2 — Workflow accelerators

### Use artifacts for anything you'll reuse (Intermediate)
Code, documents, diagrams, dashboards — ask Antigravity to put them in an artifact. You get a clean, copy-paste-ready output instead of digging through chat.

### Web search for anything time-sensitive (Beginner)
Antigravity has a knowledge cutoff. For current prices, recent news, live documentation, or "what's new in X", ask Antigravity to search the web.

### File creation for documents (Intermediate)
For polished deliverables (Word docs, PDFs, slides, spreadsheets), ask Antigravity to create the file rather than paste content into chat.

### Structured output with XML tags (Intermediate)
For complex prompts, wrap sections in tags: `<context>...</context>`, `<task>...</task>`, `<constraints>...</constraints>`. Antigravity parses these reliably and they prevent instruction-drift.

### Constraints over hints (Intermediate)
"Use simple words" is a hint. "No word over 3 syllables, no sentence over 15 words" is a constraint. Constraints produce measurable changes; hints often get ignored.

---

## Tier 3 — Memory and context

### User preferences (Intermediate)
In Antigravity.ai Settings, write a paragraph about your role, tools, and how you want Antigravity to respond. Applies to every future chat.

### Projects (Intermediate)
For ongoing work, create a Project. Drop reference documents in once and they are available in every chat inside that project.

### Memory edits (Intermediate)
Ask Antigravity to "remember that I prefer X" and the memory system persists it across conversations. Ask "forget X" to remove.

### Past chat search (Intermediate)
Antigravity can search your past conversations. "What did we decide about the auth flow last week?" works.

---

## Tier 4 — Output control

### Ask for alternatives (Beginner)
"Give me three options, ranked, with tradeoffs" beats "what should I do?" every time.

### Force a format (Beginner)
"Respond as a JSON object with keys: x, y, z" or "respond as a markdown table" works when you need structured data.

### Adjust depth on demand (Beginner)
"One sentence", "one paragraph", "deep dive", "explain like I'm 12", "explain like I'm a PhD" all reliably shift register.

### Steelman the opposite (Intermediate)
Before committing to a plan, ask Antigravity to argue against it. "What's the strongest case for not doing this?"

---

## Tier 5 — Advanced

### Chain prompts deliberately (Advanced)
Break complex work into stages: research → outline → draft → critique → final. Each stage gets a focused prompt. Quality compounds.

### Self-critique loops (Advanced)
After Antigravity produces output, ask "score this 1-10 on [specific criteria], then rewrite to fix the lowest-scoring dimension." Repeat until satisfied.

### Adversarial review (Advanced)
"view_file this as a skeptical senior reviewer. What are the three weakest claims and how would you attack them?"

### Tool use with MCP (Advanced)
Connect Antigravity to external tools (Notion, Gmail, GitHub, databases) via the MCP connector menu. Coaching, code, and content workflows can now actually take action.

### Custom skills (Advanced)
Skills like this one are reusable instruction packs. If you find yourself repeating the same setup prompt across chats, that is a skill waiting to be built.

---

## Anti-patterns (the slow ways)

- Re-explaining the same context every new chat → use a Project or User Preferences
- Copy-pasting between Antigravity and another app repeatedly → ask Antigravity to do the multi-step work in one prompt
- Asking yes/no questions on judgment calls → ask for ranked options with tradeoffs
- Accepting the first draft → ask for a self-critique and one rewrite
- Vague feedback ("make it better") → name the specific dimension ("make it more concrete", "cut 30%")
