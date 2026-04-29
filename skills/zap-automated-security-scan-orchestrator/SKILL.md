---
title: "ZAP Automated Security Scan Orchestrator"
description: "Orchestrates OWASP ZAP security scans via the ZAP API with automated spider, active scanner, and authentication sequence configuration. Generates compliance reports mapped to OWASP Top 10 and exports findings in SARIF and JUnit XML formats."
verification: "security_reviewed"
source: "https://github.com/zaproxy/zaproxy"
author: "OWASP ZAP"
category:
  - "Security & Verification"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 15007
---

# ZAP Automated Security Scan Orchestrator

Orchestrates OWASP ZAP security scans via the ZAP API with automated spider, active scanner, and authentication sequence configuration. Generates compliance reports mapped to OWASP Top 10 and exports findings in SARIF and JUnit XML formats.

## Prerequisites

Java or Docker

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
docker pull ghcr.io/zaproxy/zaproxy:stable
```

## Documentation

- https://www.zaproxy.org/docs/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/zap-automated-security-scan-orchestrator/)
