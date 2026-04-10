---
title: "PostgreSQL Query Plan Explainer"
description: "Interprets PostgreSQL EXPLAIN ANALYZE output using pg_stat_statements and auto_explain module data. Identifies sequential scan bottlenecks, index recommendations via HypoPG, and buffer cache hit ratios."
slug: "postgresql-query-plan-explainer"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/postgresql-query-plan-explainer/"
listed: true
---

# PostgreSQL Query Plan Explainer

Interprets PostgreSQL EXPLAIN ANALYZE output using pg_stat_statements and auto_explain module data. Identifies sequential scan bottlenecks, index recommendations via HypoPG, and buffer cache hit ratios.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install postgresql-query-plan-explainer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-plan-explainer/)
