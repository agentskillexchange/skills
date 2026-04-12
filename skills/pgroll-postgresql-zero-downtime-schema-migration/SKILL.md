---
title: "pgroll PostgreSQL Zero-Downtime Schema Migration"
slug: "pgroll-postgresql-zero-downtime-schema-migration"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
source: "https://github.com/xataio/pgroll"
tool_ecosystem:
  github_repo: "xataio/pgroll"
  github_stars: 6408
---

# pgroll PostgreSQL Zero-Downtime Schema Migration

pgroll is an open-source CLI tool by Xata that performs zero-downtime, reversible schema migrations for PostgreSQL. It uses the expand-and-contract pattern to keep old and new schema versions running simultaneously with automatic backfilling and instant rollback.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pgroll-postgresql-zero-downtime-schema-migration/)
