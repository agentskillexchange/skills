---
title: "Semgrep SAST Scanner"
description: "Runs Semgrep static analysis with custom rule packs targeting OWASP Top 10 patterns. Uses semgrep CLI with –config=auto and –sarif output for GitHub Advanced Security integration and CWE-tagged finding reports."
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality & Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep SAST Scanner

Overview Runs Semgrep static analysis with custom rule packs targeting OWASP Top 10 patterns. Uses semgrep CLI with –config=auto and –sarif output for GitHub Advanced Security integration and CWE-tagged finding reports.

Key Features

- Automated detection and reporting with structured output formats for downstream integrations

- Configurable thresholds and rule sets that adapt to project-specific requirements and team conventions

- Real-time feedback loops integrated into developer workflows for immediate actionable insights

- Comprehensive logging and audit trails for compliance tracking and historical trend analysis

How It Works Semgrep SAST Scanner connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers.

Requirements

- Valid API credentials with appropriate read/write scopes for the target service

- Network access to the relevant API endpoints from the agent runtime environment

- Compatible agent framework installed and configured with the necessary SDK dependencies

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/semgrep-sast-scanner-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/semgrep-sast-scanner-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-sast-scanner-skill/)
