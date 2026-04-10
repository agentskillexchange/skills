---
name: SQLFluff SQL Linter and Auto-Formatter
description: Lint and auto-format SQL code across 30+ dialects using SQLFluff. Enforces
  consistent style, catches syntax issues, and supports Jinja/dbt templating for ELT
  workflows.
verification: security_reviewed
source: https://github.com/sqlfluff/sqlfluff
category:
- Code Quality &amp; Review
framework:
- Claude Code
- Codex
- OpenClaw
tool_ecosystem:
  github_repo: sqlfluff/sqlfluff
  github_stars: 9635
---
# SQLFluff SQL Linter and Auto-Formatter

The SQLFluff SQL Linter and Auto-Formatter skill integrates SQLFluff, the dialect-flexible SQL linter with nearly 10,000 GitHub stars, into AI agent code review and data engineering workflows. SQLFluff catches style violations, formatting inconsistencies, and potential errors in SQL code, then auto-fixes most issues.
This skill supports over 30 SQL dialects including PostgreSQL, MySQL, BigQuery, Snowflake, Redshift, DuckDB, Databricks, ClickHouse, Trino, T-SQL, Oracle, and many more. Critically, SQLFluff also handles Jinja2 and dbt templating — it understands macros, refs, and config blocks, making it the only major SQL linter that works natively with dbt projects.
Agents use this skill by running SQLFluff's CLI commands against SQL files or directories. The sqlfluff lint command identifies violations with file, line, and column positions plus human-readable descriptions. The sqlfluff fix command auto-corrects fixable violations in place. The sqlfluff parse command produces a parse tree for deeper analysis.
Configuration is handled through .sqlfluff files that define dialect, rule selections, indentation preferences, comma placement (leading vs. trailing), keyword capitalization, and other style rules. Over 60 built-in rules cover areas like aliasing conventions, ambiguous joins, unused CTEs, inconsistent column references, and whitespace formatting.
The skill integrates with CI/CD pipelines through GitHub Actions, pre-commit hooks, and linting steps in dbt workflows. Output can be formatted as human-readable text, GitHub annotation format, JSON, or YAML for programmatic processing. Available on PyPI as sqlfluff, licensed under MIT, with Docker images available on Docker Hub.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sqlfluff-sql-linter-auto-formatter/)
