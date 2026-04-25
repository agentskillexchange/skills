---
title: "ESLint Rule Enforcer"
description: "Automates ESLint v9 flat config enforcement across monorepos using eslint-plugin-unicorn and @typescript-eslint/parser. Scans changed files via git diff, applies auto-fixable rules, and generates per-package lint reports with violation severity breakdowns."
verification: "security_reviewed"
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Enforcer

Overview
Automates ESLint v9 flat config enforcement across monorepos using eslint-plugin-unicorn and @typescript-eslint/parser. Scans changed files via git diff, applies auto-fixable rules, and generates per-package lint reports with violation severity breakdowns.

Key Features

Automated detection and reporting with structured output formats for downstream integrations
Configurable thresholds and rule sets that adapt to project-specific requirements and team conventions
Real-time feedback loops integrated into developer workflows for immediate actionable insights
Comprehensive logging and audit trails for compliance tracking and historical trend analysis

How It Works
ESLint Rule Enforcer connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers.

Requirements

Valid API credentials with appropriate read/write scopes for the target service
Network access to the relevant API endpoints from the agent runtime environment
Compatible agent framework installed and configured with the necessary SDK dependencies

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/eslint-rule-enforcer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/eslint-rule-enforcer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/eslint-rule-enforcer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-enforcer/)
