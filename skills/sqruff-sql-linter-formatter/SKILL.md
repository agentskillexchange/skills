---
name: "sqruff High-Performance SQL Linter and Formatter"
description: "A fast SQL linter and formatter written in Rust by Quary Labs. sqruff provides advanced configurable linting and automated formatting with significantly faster execution than Python-based alternatives, plus a browser playground for quick experimentation."
category: "Code Quality &amp; Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/quarylabs/sqruff"
tool_ecosystem:
  github_repo: "https://github.com/quarylabs/sqruff"
  github_stars: 1268
---
# sqruff High-Performance SQL Linter and Formatter

A fast SQL linter and formatter written in Rust by Quary Labs. sqruff provides advanced configurable linting and automated formatting with significantly faster execution than Python-based alternatives, plus a browser playground for quick experimentation.

sqruff is an open-source SQL linter and formatter built in Rust by Quary Labs. It reimplements SQLFluff’s rule set in a compiled language, achieving roughly 10x faster scan times on real-world SQL codebases. The tool supports multiple SQL dialects including PostgreSQL, BigQuery, Snowflake, ClickHouse, and ANSI SQL.

The linter checks SQL files against a configurable set of rules covering formatting conventions, naming standards, query structure, and anti-patterns. When violations are found, sqruff can automatically fix many of them through its formatting mode. Developers configure the tool through a .sqruff configuration file in their project root, specifying the target dialect and enabling or disabling specific rules.

sqruff is designed for integration into development workflows. It installs through Homebrew, pip, Cargo, or direct binary downloads, making it accessible regardless of the team’s primary language ecosystem. The CLI supports linting individual files, directories, or piped input, and produces structured output suitable for CI/CD pipelines.

The project maintains an interactive browser playground at playground.quary.dev where developers can test rules against their SQL without installing anything. The documentation covers installation, usage patterns, configuration options, the full rule reference, and CLI commands. Rules are organized by category with clear descriptions and examples of violations and fixes.

For data teams working with dbt, analytics pipelines, or any SQL-heavy workflow, sqruff provides consistent formatting and catches common mistakes before they reach production. Its speed makes it practical to run on every commit or as part of pre-commit hooks without adding noticeable delay to the development cycle.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sqruff-sql-linter-formatter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sqruff-sql-linter-formatter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sqruff-sql-linter-formatter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sqruff-sql-linter-formatter -a codex
```

### OpenClaw

```bash
clawhub install sqruff-sql-linter-formatter
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sqruff-sql-linter-formatter/)
