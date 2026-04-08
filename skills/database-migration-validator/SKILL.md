---
title: "Database Migration Validator"
slug: "database-migration-validator"
description: "Validates SQL database migrations for safety using pg_stat_statements analysis and pt-online-schema-change dry-run mode. Checks for long-running locks, missing indexes on foreign keys, and backward-incompatible column changes."
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/database-migration-validator/"
---

# Database Migration Validator

Validates SQL database migrations for safety using pg_stat_statements analysis and pt-online-schema-change dry-run mode. Checks for long-running locks, missing indexes on foreign keys, and backward-incompatible column changes.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/database-migration-validator/)
