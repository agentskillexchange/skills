---
title: OWASP ZAP Scanner Agent
description: Integrates the OWASP ZAP API to run automated DAST scans against web
  applications. Parses ZAP JSON reports, triages alerts by CVSS severity, and generates
  remediation tickets via Jira REST API.
verification: security_reviewed
source: https://github.com/zaproxy/zaproxy
category:
- Security & Verification
framework:
- OpenClaw
tool_ecosystem:
  github_repo: zaproxy/zaproxy
  github_stars: 14991
---

# OWASP ZAP Scanner Agent

Integrates the OWASP ZAP API to run automated DAST scans against web applications. Parses ZAP JSON reports, triages alerts by CVSS severity, and generates remediation tickets via Jira REST API.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/owasp-zap-scanner-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/owasp-zap-scanner-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/owasp-zap-scanner-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-scanner-agent/)
