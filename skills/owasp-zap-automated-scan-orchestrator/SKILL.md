---
title: "OWASP ZAP Automated Scan Orchestrator"
description: "Runs OWASP ZAP active and passive scans against target URLs using the ZAP Docker API. Parses JSON reports to flag XSS, SQLi, and CSRF vulnerabilities with severity scoring."
verification: security_reviewed
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
---

# OWASP ZAP Automated Scan Orchestrator

Runs OWASP ZAP active and passive scans against target URLs using the ZAP Docker API. Parses JSON reports to flag XSS, SQLi, and CSRF vulnerabilities with severity scoring.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/owasp-zap-automated-scan-orchestrator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/owasp-zap-automated-scan-orchestrator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/owasp-zap-automated-scan-orchestrator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-automated-scan-orchestrator/)
