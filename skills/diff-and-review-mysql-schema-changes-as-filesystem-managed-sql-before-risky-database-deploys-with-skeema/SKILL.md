---
title: "Diff and review MySQL schema changes as filesystem-managed SQL before risky database deploys with Skeema"
description: "Use Skeema when an agent needs to manage MySQL or MariaDB schema as reviewable files, compare intended changes against live databases, and stage safe deploys. A user should invoke this instead of using the database normally when the task is schema pull, diff, lint, and controlled push, not ad hoc querying or generic administration. The scope boundary is crisp and skill-shaped: filesystem-backed schema change review and deployment for MySQL-family databases, not a plain database product or migration framework listing."
source: "https://github.com/skeema/skeema"
verification: "listed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "skeema/skeema"
  github_stars: 1361
---

# Diff and review MySQL schema changes as filesystem-managed SQL before risky database deploys with Skeema

Use Skeema when an agent needs to manage MySQL or MariaDB schema as reviewable files, compare intended changes against live databases, and stage safe deploys. A user should invoke this instead of using the database normally when the task is schema pull, diff, lint, and controlled push, not ad hoc querying or generic administration. The scope boundary is crisp and skill-shaped: filesystem-backed schema change review and deployment for MySQL-family databases, not a plain database product or migration framework listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diff-and-review-mysql-schema-changes-as-filesystem-managed-sql-before-risky-database-deploys-with-skeema/)
