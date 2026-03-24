---
name: "PostgreSQL Vacuum Deadlock Runbook"
description: "Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables, pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension and generates remediation SQL for long-running transaction conflicts."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed
rating: 4.5
reviews: 79
creator: "Ben Taylor"
creator_handle: "@bentaylor"
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/"
---
# PostgreSQL Vacuum Deadlock Runbook

Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables, pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension and generates remediation SQL for long-running transaction conflicts.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill postgresql-vacuum-deadlock-runbook
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill postgresql-vacuum-deadlock-runbook -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill postgresql-vacuum-deadlock-runbook -a cursor
```

### OpenClaw
```bash
clawhub install postgresql-vacuum-deadlock-runbook
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill postgresql-vacuum-deadlock-runbook -a codex
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
[View Profile on ASE](https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/)

---

[View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/) · [Browse All Skills](https://agentskillexchange.com/skills/)