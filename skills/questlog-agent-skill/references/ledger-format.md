# Ledger format

The initial file contains `# LEDGER — updated YYYY-MM-DD`, then empty `## NOW` and `## INBOX` sections. It contains no example tasks.

NOW holds one short current action. INBOX holds unstructured `- text` bullets pending human/agent triage. A workstream heading is `## slug [domain] [state]`, with lowercase alphanumeric/dot/underscore/hyphen slug. Domains: work, research, life, forge, client. States: hot, warm, paused, blocked, ember.

Workstream fields:

- `GOAL: text` — intended outcome.
- `NEXT: text` — next concrete action, not a claim of execution.
- `DUE: YYYY-MM-DD description [hard|soft]` — explicit deadline and strength.
- `WAITING: person — item — since YYYY-MM-DD — chase Nd` — waiting-on record.
- `NOTE: text` — supporting context.
- `- [ ] task` / `- [x] task` — nested task checkboxes (two-space indentation).

Unknown H2 sections are ignored by the UI; originals remain in Markdown. The content hash exposed as `head` is a revision, not a Git commit. UI preferences and local instruction drafts live beside the ledger, not in the grammar. No source data or sample records ship with the release.
