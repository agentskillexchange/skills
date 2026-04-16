---
title: "PostgreSQL Query Optimizer Agent"
description: "Optimizes PostgreSQL queries using EXPLAIN ANALYZE output parsing with pg_stat_statements extension data. Suggests index creation via HypoPG hypothetical index simulator and validates query plans against pg_hint_plan directives."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/pg"
category:
  - "Developer Tools"
framework:
  - "OpenClaw"
tool_ecosystem:
  ase_npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Query Optimizer Agent

Optimizes PostgreSQL queries using EXPLAIN ANALYZE output parsing with pg_stat_statements extension data. Suggests index creation via HypoPG hypothetical index simulator and validates query plans against pg_hint_plan directives.

This skill provides a comprehensive automation layer for developers and teams who need reliable, repeatable workflows. It handles authentication, rate limiting, and error recovery automatically, so you can focus on the logic that matters. The agent monitors for changes in real time and applies incremental updates to minimize API calls and reduce latency. Configuration is handled through a simple YAML manifest that defines inputs, outputs, and trigger conditions. Built-in logging captures every action for audit trails and debugging. Supports both interactive and headless modes, making it suitable for CI/CD pipelines as well as local development. The skill includes pre-built templates for common use cases and can be extended with custom plugins. Error handling follows exponential backoff with jitter for transient failures and provides clear diagnostic messages for permanent errors. Compatible with major operating systems and containerized environments. Tested against production workloads with comprehensive integration test suites.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-optimizer-explain-api/)
