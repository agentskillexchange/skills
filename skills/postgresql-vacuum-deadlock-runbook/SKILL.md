---
name: "PostgreSQL Vacuum Deadlock Runbook"
description: "Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables, pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension and generates remediation SQL for long-running transaction conflicts."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/"
tool_ecosystem:
  tool: "postgresql"
  github_stars: 0
  npm_weekly_downloads: 21413502
  github_repo: ""
  license: ""
  maintained: false
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Claude Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | postgresql |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
