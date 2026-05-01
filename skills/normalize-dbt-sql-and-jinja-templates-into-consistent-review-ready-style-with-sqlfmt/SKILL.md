---
title: "Normalize dbt SQL and Jinja templates into consistent review-ready style with sqlfmt"
description: "Use sqlfmt to reformat dbt-oriented SQL and Jinja-heavy query files into a stable style before code review, CI checks, or agent-generated handoff."
verification: "security_reviewed"
source: "https://github.com/tconbeer/sqlfmt"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "tconbeer/sqlfmt"
  github_stars: 530
---

# Normalize dbt SQL and Jinja templates into consistent review-ready style with sqlfmt

Use this skill when an agent needs to clean up messy dbt SQL or Jinja-templated query files before review, commit, or downstream linting. sqlfmt is a focused formatter: it rewrites supported SQL files into one consistent style, handles Jinja-aware source text, and avoids turning the task into a broader linting or warehouse-management workflow.

Invoke it when the job is specifically make these SQL files readable and consistent rather than run dbt itself, manage models, or operate a data platform. That scope boundary keeps this entry skill-shaped: the agent performs a narrow formatting pass over existing SQL assets and returns reviewable diffs.

This is especially useful after agent-generated edits, before pull requests, or when teams want style normalization without code-review debates. The upstream project explicitly positions sqlfmt as a fast SQL formatter for dbt SQL files that works with Jinja and integrates into CLI, CI, and editor workflows.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/normalize-dbt-sql-and-jinja-templates-into-consistent-review-ready-style-with-sqlfmt/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/normalize-dbt-sql-and-jinja-templates-into-consistent-review-ready-style-with-sqlfmt
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/normalize-dbt-sql-and-jinja-templates-into-consistent-review-ready-style-with-sqlfmt`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-dbt-sql-and-jinja-templates-into-consistent-review-ready-style-with-sqlfmt/)
