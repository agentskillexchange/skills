---
title: "Semgrep SAST Scanner"
description: "Runs Semgrep static analysis with custom rule packs targeting OWASP Top 10 patterns. Uses semgrep CLI with –config=auto and –sarif output for GitHub Advanced Security integration and CWE-tagged finding reports."
verification: "security_reviewed"
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
  license: "LGPL-2.1"
---

# Semgrep SAST Scanner

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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-sast-scanner-skill/)
