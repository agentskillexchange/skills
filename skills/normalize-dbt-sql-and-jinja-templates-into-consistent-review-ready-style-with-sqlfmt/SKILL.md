---
name: "Normalize dbt SQL and Jinja templates into consistent review-ready style with sqlfmt"
slug: "normalize-dbt-sql-and-jinja-templates-into-consistent-review-ready-style-with-sqlfmt"
description: "Use sqlfmt to reformat dbt-oriented SQL and Jinja-heavy query files into a stable style before code review, CI checks, or agent-generated handoff."
github_stars: 530
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

Use the upstream install or setup path that matches your environment:
- #### Recommended Installation: Use uv
- [Install uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer). From a POSIX shell, run:
- uv tool install "shandy-sqlfmt[jinjafmt]"
- **Use pip or something pip-like:**

Requirements and caveats from upstream:
- ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/shandy-sqlfmt)
- **sqlfmt integrates with your workflow.** As a CLI written in Python, it's easy to install locally on any OS and run in CI. Plays well with dbt, pre-commit, SQLFluff, VSCode, and GitHub Actions. sqlfmt powers the dbt...
- sqlfmt is a command-line tool that is built in Python and runs on MacOS, Linux, and Windows. It is distributed

Basic usage or getting-started notes:
- **sqlfmt is fast.** Forget about formatting your code, and spend your time on business logic instead. sqlfmt processes hundreds of files per second and only operates on files that have changed since the last run.
- Please visit [docs.sqlfmt.com](https://docs.sqlfmt.com) for more information on Getting Started, Integrations, the sqlfmt Style, and an API Reference. Or keep reading for an excerpt from the full docs.
- #### Try it first

- Source: https://github.com/tconbeer/sqlfmt
- Extracted from upstream docs: https://raw.githubusercontent.com/tconbeer/sqlfmt/HEAD/README.md

## Documentation

- https://sqlfmt.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-dbt-sql-and-jinja-templates-into-consistent-review-ready-style-with-sqlfmt/)
