---
name: Codecov Coverage Tracker
description: "Monitors test coverage trends using the Codecov API v2 /repos/{owner}/{repo}/commits\
  \ endpoint. Compares branch coverage against base, generates diff-coverage reports,\
  \ and flags untested code paths in PR comments via GitHub REST API."
category: "Code Quality &amp; Review"
framework: ChatGPT Agents
verification: security_reviewed
source: "https://agentskillexchange.com/skills/codecov-coverage-tracker-skill/"
---
# Codecov Coverage Tracker

Monitors test coverage trends using the Codecov API v2 /repos/{owner}/{repo}/commits endpoint. Compares branch coverage against base, generates diff-coverage reports, and flags untested code paths in PR comments via GitHub REST API.

Overview

Monitors test coverage trends using the Codecov API v2 /repos/{owner}/{repo}/commits endpoint. Compares branch coverage against base, generates diff-coverage reports, and flags untested code paths in PR comments via GitHub REST API.

Key Features

- Automated detection and reporting with structured output formats for downstream integrations

- Configurable thresholds and rule sets that adapt to project-specific requirements and team conventions

- Real-time feedback loops integrated into developer workflows for immediate actionable insights

- Comprehensive logging and audit trails for compliance tracking and historical trend analysis

How It Works

Codecov Coverage Tracker connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers.

Requirements

- Valid API credentials with appropriate read/write scopes for the target service

- Network access to the relevant API endpoints from the agent runtime environment

- Compatible agent framework installed and configured with the necessary SDK dependencies

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-tracker-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-tracker-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-tracker-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-tracker-skill -a codex
```

### OpenClaw

```bash
clawhub install codecov-coverage-tracker-skill
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-tracker-skill/)
