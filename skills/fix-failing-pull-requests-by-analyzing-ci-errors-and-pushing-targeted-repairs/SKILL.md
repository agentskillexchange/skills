---
name: "Fix failing pull requests by analyzing CI errors and pushing targeted repairs"
slug: "fix-failing-pull-requests-by-analyzing-ci-errors-and-pushing-targeted-repairs"
description: "Use GitHub Next's pr-fix workflow when a pull request is blocked on failing checks and the likely repair is machine-doable. The agent inspects CI failures, traces the root cause, applies a focused fix on the PR branch, and leaves the result in reviewable Git history."
verification: "security_reviewed"
source: "https://github.com/githubnext/agentics/blob/main/docs/pr-fix.md"
author: "GitHub Next"
publisher_type: "Organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
---

# Fix failing pull requests by analyzing CI errors and pushing targeted repairs

Use GitHub Next's pr-fix workflow when a pull request is blocked on failing checks and the likely repair is machine-doable. The agent inspects CI failures, traces the root cause, applies a focused fix on the PR branch, and leaves the result in reviewable Git history.

## Prerequisites

GitHub CLI, gh-aw extension

## Installation

Use the upstream install or setup path that matches your environment:
- Make software maintenance enjoyable! From basic issue triage to Repo Assist - a powerful triage multi-task backlog burner, issue labeller, bug fixer and general repository assistant. Other workflows help gate your rep...

Basic usage or getting-started notes:
- [💰 Cost Tracker](docs/cost-tracker.md) - Post per-run agent spend summaries on pull requests using token-usage.jsonl from gh-aw's firewall
- [📝 Markdown Linter](docs/markdown-linter.md) - Run Markdown quality checks on all documentation files and get a prioritized issue report of violations
- **[Reporting](workflows/shared/reporting.md)** - Guidelines for reporting workflow run information with clickable run ID links

- Source: https://github.com/githubnext/agentics/blob/main/docs/pr-fix.md
- Extracted from upstream docs: https://raw.githubusercontent.com/githubnext/agentics/HEAD/README.md

## Documentation

- https://github.com/githubnext/agentics/blob/main/docs/pr-fix.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fix-failing-pull-requests-by-analyzing-ci-errors-and-pushing-targeted-repairs/)
