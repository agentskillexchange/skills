# Recommended agent checkpoint

Add this instruction to a global or workspace agent prompt:

> At natural milestones and before ending work that changed a durable decision, preference, commitment, evidence claim, or project state, use `$argus` once to preserve only the delta. Route commitments through the configured commitment system, route knowledge to its canonical archive, respect each archive's `AGENTS.md` and configured layout, maintain required backlinks, and skip capture when nothing durable changed.

For substantial autonomous or GPU work, pair it with this pre-flight rule:

> Before launching substantial autonomous, multi-agent, or GPU work, use the configured budget authority. At session end, log actual usage and link the canonical artefacts preserved by `$argus`.

This is preferable to a timer. A timer cannot reliably recover a conversation after its context has disappeared, while a semantic checkpoint can distinguish durable state from transient chat.
