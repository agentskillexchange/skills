---
title: "PostgreSQL Slow Query Analyzer"
slug: "postgresql-slow-query-analyzer"
description: "Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase."
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/postgresql-slow-query-analyzer/"
---

# PostgreSQL Slow Query Analyzer

Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-analyzer/)
