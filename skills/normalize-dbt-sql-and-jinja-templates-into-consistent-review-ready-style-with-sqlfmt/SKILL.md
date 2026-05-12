---
title: "Normalize dbt SQL and Jinja templates into consistent review-ready style with sqlfmt"
slug: "normalize-dbt-sql-and-jinja-templates-into-consistent-review-ready-style-with-sqlfmt"
description: "Use sqlfmt to reformat dbt-oriented SQL and Jinja-heavy query files into a stable style before code review, CI checks, or agent-generated handoff."
verification: "security_reviewed"
source: "https://github.com/tconbeer/sqlfmt"
author: "Tristan Conbeer and contributors"
publisher_type: "oss"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "tconbeer/sqlfmt"
  github_stars: 530
---

# Normalize dbt SQL and Jinja templates into consistent review-ready style with sqlfmt

Use sqlfmt to reformat dbt-oriented SQL and Jinja-heavy query files into a stable style before code review, CI checks, or agent-generated handoff.

## Prerequisites

sqlfmt CLI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the Python CLI from the upstream sqlfmt project (the repository notes distribution on PyPI as shandy-sqlfmt, with uv recommended), then run sqlfmt against the target SQL files or project paths.
```

## Documentation

- https://sqlfmt.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-dbt-sql-and-jinja-templates-into-consistent-review-ready-style-with-sqlfmt/)
