---
name: "Butler"
slug: "butler-agent-skill"
description: "Track per-project Claude usage estimates and local GPU budgets, preview admission, atomically reserve capacity, and reconcile actual usage with a local dashboard."
category: "Monitoring & Alerts"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/butler-agent-skill"
---

# Butler

Use the bundled runtime for local project-budget custody. Read [README.md](README.md) for installation and [references/accounting.md](references/accounting.md) before GPU work.

Resolve the user's explicit `BUTLER_ROOT` and project. A fresh install has no accounts, projects, reservations or usage. Do not invent a budget or scan transcripts automatically. Configure limits only from the user's authority. Registration and policy changes write state.

For a budget check, use `scripts/butler.py gate --project SLUG` or `gpu-gate`: a preview does not reserve GPU capacity. When compute launch is separately authorized, use `gpu-reserve` with a stable idempotency key before launch; reconcile actual terminal usage afterwards. No command here launches compute, bills a provider, changes provider authentication, or deletes provider disks. A disk-release entry is evidence recording, not cleanup.

The local Claude weighted-token proxy is not actual Codex quota. Optional cached Claude utilization is dated provider evidence, not a fresh quota query. Report unavailable evidence as unavailable. Gate results are advisory unless the actual execution path obeys them. Missing GPU limits are not a cap; verify policy explicitly. Never clear limits through `--unlimited` without explicit budget-owner authorization.

Use `session-log` for an authorized run summary and artifact paths. Keep ledgers and transcripts out of the public package. Open the dashboard only on loopback. Remote SSH collection and local process inspection are optional opt-ins, never implicit task steps.

## Installation and upstream provenance

The upstream skill identifier is `butler`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/butler-agent-skill --skill butler --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/butler-agent-skill#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata, a matching display heading, and this installation section added. The source snapshot is [`9b761c065043`](https://github.com/AntreasAntoniou/butler-agent-skill/tree/9b761c065043c6129f91d62a85dbdd828c514ece). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
