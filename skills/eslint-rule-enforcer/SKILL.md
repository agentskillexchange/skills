---
title: "ESLint Rule Enforcer"
description: "Overview\nAutomates ESLint v9 flat config enforcement across monorepos using eslint-plugin-unicorn and @typescript-eslint/parser. Scans changed files via git diff, applies auto-fixable rules, and generates per-package lint reports with violation severity breakdowns.\nKey Features\n\nAutomated detection and reporting with structured output formats for downstream integrations\nConfigurable thresholds and rule sets that adapt to project-specific requirements and team conventions\nReal-time feedback loops integrated into developer workflows for immediate actionable insights\nComprehensive logging and audit trails for compliance tracking and historical trend analysis\n\nHow It Works\nESLint Rule Enforcer connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers.\nRequirements\n\nValid API credentials with appropriate read/write scopes for the target service\nNetwork access to the relevant API endpoints from the agent runtime environment\nCompatible agent framework installed and configured with the necessary SDK dependencies"
verification: security_reviewed
source: "https://github.com/eslint/eslint"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  ase_npm_package: "eslint"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/eslint-rule-enforcer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/eslint-rule-enforcer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-enforcer/)
