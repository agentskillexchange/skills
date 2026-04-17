---
title: "OWASP ZAP Active Scanner Agent"
description: "Runs OWASP ZAP active security scans via the ZAP API daemon with custom scan policies. Generates SARIF reports compatible with GitHub Advanced Security code scanning alerts."
verification: security_reviewed
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security & Verification"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
  license: "Apache-2.0"
---

# OWASP ZAP Active Scanner Agent

The OWASP ZAP Active Scanner Agent automates web application security testing using the OWASP ZAP API in daemon mode. It configures custom scan policies that target OWASP Top 10 vulnerabilities including SQL injection, XSS, CSRF, and SSRF using ZAP’s pluggable scanner architecture. The skill starts ZAP in headless daemon mode, configures the target context with authentication credentials via ZAP’s Session Management API, and launches active scans with configurable thread counts and request throttling. Spider crawling uses ZAP’s AJAX Spider with Selenium WebDriver integration for JavaScript-heavy applications. Scan results are parsed from ZAP’s JSON report format and converted to SARIF (Static Analysis Results Interchange Format) for direct import into GitHub Advanced Security code scanning alerts. The skill supports baseline scans for CI/CD pipelines with configurable severity thresholds that gate deployments. False positive management uses ZAP’s alert filter API with persistent exclusion rules stored in a YAML configuration file.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/owasp-zap-active-scanner-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/owasp-zap-active-scanner-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-active-scanner-agent/)
