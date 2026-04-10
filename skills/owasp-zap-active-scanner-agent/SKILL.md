---
title: "OWASP ZAP Active Scanner Agent"
description: "Runs OWASP ZAP active security scans via the ZAP API daemon with custom scan policies. Generates SARIF reports compatible with GitHub Advanced Security code scanning alerts."
slug: "owasp-zap-active-scanner-agent"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/owasp-zap-active-scanner-agent/"
listed: true
---

# OWASP ZAP Active Scanner Agent

Runs OWASP ZAP active security scans via the ZAP API daemon with custom scan policies. Generates SARIF reports compatible with GitHub Advanced Security code scanning alerts.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install owasp-zap-active-scanner-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The OWASP ZAP Active Scanner Agent automates web application security testing using the OWASP ZAP API in daemon mode. It configures custom scan policies that target OWASP Top 10 vulnerabilities including SQL injection, XSS, CSRF, and SSRF using ZAP’s pluggable scanner architecture. The skill starts ZAP in headless daemon mode, configures the target context with authentication credentials via ZAP’s Session Management API, and launches active scans with configurable thread counts and request throttling. Spider crawling uses ZAP’s AJAX Spider with Selenium WebDriver integration for JavaScript-heavy applications. Scan results are parsed from ZAP’s JSON report format and converted to SARIF (Static Analysis Results Interchange Format) for direct import into GitHub Advanced Security code scanning alerts. The skill supports baseline scans for CI/CD pipelines with configurable severity thresholds that gate deployments. False positive management uses ZAP’s alert filter API with persistent exclusion rules stored in a YAML configuration file.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-active-scanner-agent/)
