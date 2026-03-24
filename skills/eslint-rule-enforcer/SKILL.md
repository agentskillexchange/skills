---
name: "ESLint Rule Enforcer"
description: "Automates ESLint v9 flat config enforcement across monorepos using eslint-plugin-unicorn and @typescript-eslint/parser. Scans changed files via git diff, applies auto-fixable rules, and generates per-package lint reports with violation severity breakdowns."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/eslint-rule-enforcer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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
