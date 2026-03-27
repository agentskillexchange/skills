---
name: "Semgrep SAST Scanner"
description: "Runs Semgrep static analysis with custom rule packs targeting OWASP Top 10 patterns. Uses semgrep CLI with –config=auto and –sarif output for GitHub Advanced Security integration and CWE-tagged finding reports."
category: "Code Quality & Review"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/semgrep-sast-scanner-skill/"
tool_ecosystem:
  tool: semgrep
  github_stars: 14551
  github_repo: semgrep/semgrep
  license: LGPL-2.1
  maintained: true
---

# Semgrep SAST Scanner

Runs Semgrep static analysis with custom rule packs targeting OWASP Top 10 patterns. Uses semgrep CLI with –config=auto and –sarif output for GitHub Advanced Security integration and CWE-tagged finding reports.

## Overview

Overview

Runs Semgrep static analysis with custom rule packs targeting OWASP Top 10 patterns. Uses semgrep CLI with –config=auto and –sarif output for GitHub Advanced Security integration and CWE-tagged finding reports.

Key Features

Automated detection and reporting with structured output formats for downstream integrations

Configurable thresholds and rule sets that adapt to project-specific requirements and team conventions

Real-time feedback loops integrated into developer workflows for immediate actionable insights

Comprehensive logging and audit trails for compliance tracking and historical trend analysis

How It Works

Semgrep SAST Scanner connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers.

Requirements

Valid API credentials with appropriate read/write scopes for the target service

Network access to the relevant API endpoints from the agent runtime environment

Compatible agent framework installed and configured with the necessary SDK dependencies

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-sast-scanner-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-sast-scanner-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-sast-scanner-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-sast-scanner-skill -a codex
```

### OpenClaw

```bash
clawhub install semgrep-sast-scanner-skill
```

## Source

- Marketplace: https://agentskillexchange.com/skills/semgrep-sast-scanner-skill/
