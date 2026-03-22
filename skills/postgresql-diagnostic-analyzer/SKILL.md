---
name: "PostgreSQL Diagnostic Analyzer"
description: "Runs diagnostic queries against PostgreSQL using pg_stat_statements, pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention, and bloat using pgstattuple and pg_repack extension analysis."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: "security_reviewed"
rating: "4.3"
reviews: "24"
creator: "Tom Wilson"
creator_handle: "@tomwilson"
creator_verified: false
source: "https://agentskillexchange.com/skill/postgresql-diagnostic-analyzer/"
---

# PostgreSQL Diagnostic Analyzer

Runs diagnostic queries against PostgreSQL using pg_stat_statements, pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention, and bloat using pgstattuple and pg_repack extension analysis.

## Installation

Install this skill in your AI coding agent:

### Any Agent (npx)
```bash
npx agentskills install postgresql-diagnostic-analyzer
```

### Claude Code
```bash
claude mcp add postgresql-diagnostic-analyzer -- npx agentskills install postgresql-diagnostic-analyzer
```

### Cursor
Add to `.cursor/agents.json`:
```json
{
  "skills": ["postgresql-diagnostic-analyzer"]
}
```

### OpenClaw
```bash
clawhub install postgresql-diagnostic-analyzer
```

### Codex
```bash
codex install skill postgresql-diagnostic-analyzer
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | 🔒 Security Reviewed |
| **Rating** | ⭐ 4.3 (24 reviews) |

## Creator

**Tom Wilson** 
Handle: `@tomwilson`
[View Profile on ASE](https://agentskillexchange.com/skill/postgresql-diagnostic-analyzer/)

---

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-diagnostic-analyzer/) • [Browse All Skills](https://agentskillexchange.com)
