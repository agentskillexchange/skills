---
name: "Review open pull requests against repository contribution guidelines"
slug: "review-open-pull-requests-against-repository-contribution-guidelines"
description: "This entry turns GitHub Next's Contribution Check workflow into a maintainer-facing agent routine. The agent batches open pull requests, compares them to CONTRIBUTING.md, labels likely-ready submissions, comments on gaps, and produces a report issue so humans can spend review time where it matters."
verification: "security_reviewed"
source: "https://github.com/githubnext/agentics/blob/main/docs/contribution-check.md"
author: "GitHub Next"
publisher_type: "Open Source Project"
category: "Templates & Workflows"
framework: "Multi-Framework"
---

# Review open pull requests against repository contribution guidelines

This entry turns GitHub Next's Contribution Check workflow into a maintainer-facing agent routine. The agent batches open pull requests, compares them to CONTRIBUTING.md, labels likely-ready submissions, comments on gaps, and produces a report issue so humans can spend review time where it matters.

## Prerequisites

GitHub CLI, the gh-aw extension, and a repository with CONTRIBUTING.md

## Installation

Use the upstream install or setup path that matches your environment:
- Make software maintenance enjoyable! From basic issue triage to Repo Assist - a powerful triage multi-task backlog burner, issue labeller, bug fixer and general repository assistant. Other workflows help gate your rep...

Basic usage or getting-started notes:
- [💰 Cost Tracker](docs/cost-tracker.md) - Post per-run agent spend summaries on pull requests using token-usage.jsonl from gh-aw's firewall
- [📝 Markdown Linter](docs/markdown-linter.md) - Run Markdown quality checks on all documentation files and get a prioritized issue report of violations
- **[Reporting](workflows/shared/reporting.md)** - Guidelines for reporting workflow run information with clickable run ID links

- Source: https://github.com/githubnext/agentics/blob/main/docs/contribution-check.md
- Extracted from upstream docs: https://raw.githubusercontent.com/githubnext/agentics/HEAD/README.md

## Documentation

- https://github.com/githubnext/agentics/blob/main/docs/contribution-check.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-open-pull-requests-against-repository-contribution-guidelines/)
