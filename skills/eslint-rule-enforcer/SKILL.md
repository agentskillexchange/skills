---
name: "ESLint Rule Enforcer"
description: "Automates ESLint v9 flat config enforcement across monorepos using eslint-plugin-unicorn and @typescript-eslint/parser. Scans changed files via git diff, applies auto-fixable rules, and generates per-package lint reports with violation severity breakdowns."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/eslint/eslint"
tool_ecosystem:
  tool: eslint
  github_stars: 27185
  npm_weekly_downloads: 109028697
  github_repo: eslint/eslint
  license: MIT
  maintained: true
---

# ESLint Rule Enforcer

Automates ESLint v9 flat config enforcement across monorepos using eslint-plugin-unicorn and @typescript-eslint/parser. Scans changed files via git diff, applies auto-fixable rules, and generates per-package lint reports with violation severity breakdowns.

## Overview

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

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-enforcer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-enforcer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-enforcer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-enforcer -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-enforcer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/eslint-rule-enforcer/
