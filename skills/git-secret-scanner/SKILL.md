---
name: Git Secret Scanner
description: Detects leaked secrets in Git repositories using pattern-based scanning with Gitleaks rule definitions and the GitHub Secret Scanning API. Identifies exposed API keys, tokens, and credentials across full commit history using git log --all -p analysis.
category: Security &amp; Verification
framework: Any Agent
verification: security_reviewed
rating: 4.3
reviews: 56
source: https://agentskillexchange.com/skill/git-secret-scanner/
---

# Git Secret Scanner

Detects leaked secrets in Git repositories using pattern-based scanning with Gitleaks rule definitions and the GitHub Secret Scanning API. Identifies exposed API keys, tokens, and credentials across full commit history using git log --all -p analysis.

## Overview

Detects leaked secrets in Git repositories using pattern-based scanning with Gitleaks rule definitions and the GitHub Secret Scanning API. Identifies exposed API keys, tokens, and credentials across full commit history using git log --all -p analysis.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill git-secret-scanner
```

### OpenClaw

```bash
clawhub install git-secret-scanner
```

### Claude Code

```bash
claude mcp add git-secret-scanner
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/git-secret-scanner/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Security &amp; Verification
- **Framework**: Any Agent
- **Rating**: 4.3/5 (56 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/git-secret-scanner/)
