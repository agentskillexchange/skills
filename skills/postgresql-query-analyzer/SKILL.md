---
name: "PostgreSQL Query Analyzer"
description: "Analyzes PostgreSQL slow queries using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output and pg_stat_statements views. Identifies missing indexes via pg_stat_user_tables sequential scan counters and suggests index creation with HypoPG extension."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 4.9
reviews: 82
creator: "Chris Lee"
creator_handle: "@chrislee"
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-query-analyzer/"
---
# PostgreSQL Query Analyzer

Analyzes PostgreSQL slow queries using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output and pg_stat_statements views. Identifies missing indexes via pg_stat_user_tables sequential scan counters and suggests index creation with HypoPG extension.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-analyzer -a cursor
```

### OpenClaw

```bash
clawhub install postgresql-query-analyzer
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-analyzer -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Gemini |
| Verification | Security Reviewed |
| Rating | 4.9/5 (82 reviews) |

## Creator

**Chris Lee**
- Profile: [@chrislee](https://agentskillexchange.com/browse-skills/?creator=chrislee)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-analyzer/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
