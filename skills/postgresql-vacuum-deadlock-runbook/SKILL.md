---
name: "PostgreSQL Vacuum Deadlock Runbook"
description: "Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables, pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension and generates remediation SQL for long-running transaction conflicts."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: "✅ Verified"
rating: "4.5"
reviews: "79"
creator: "Ben Taylor"
creator_handle: "@bentaylor"
creator_verified: "false"
source: "https://agentskillexchange.com/skill/postgresql-vacuum-deadlock-runbook/"
---

# PostgreSQL Vacuum Deadlock Runbook

Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables, pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension and generates remediation SQL for long-running transaction conflicts.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/agent-skills install postgresql-vacuum-deadlock-runbook
```

### Claude Code
```bash
claude mcp add postgresql-vacuum-deadlock-runbook
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "skills": ["postgresql-vacuum-deadlock-runbook"]
}
```

### OpenClaw
```bash
clawhub install postgresql-vacuum-deadlock-runbook
```

### Codex
```bash
codex install postgresql-vacuum-deadlock-runbook
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Claude Agents |
| **Verification** | ✅ Verified 🔒 Reviewed |
| **Rating** | ⭐⭐⭐⭐ 4.5/5 (79 reviews) |

## Creator

**Ben Taylor** 
Handle: `@bentaylor`
[View Profile on ASE](https://agentskillexchange.com/skill/postgresql-vacuum-deadlock-runbook/)

---

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-vacuum-deadlock-runbook/) · [Browse All Skills](https://agentskillexchange.com/skills/)