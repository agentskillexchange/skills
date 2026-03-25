---
name: "OWASP ZAP Active Scanner Agent"
description: "Runs OWASP ZAP active security scans via the ZAP API daemon with custom scan policies. Generates SARIF reports compatible with GitHub Advanced Security code scanning alerts."
category: "Security & Verification"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/owasp-zap-active-scanner-agent/"
tool_ecosystem:
  tool: "owasp"
  github_stars: 14900
  github_repo: "zaproxy/zaproxy"
  license: "Apache-2.0"
  maintained: true
---

# OWASP ZAP Active Scanner Agent

Runs OWASP ZAP active security scans via the ZAP API daemon with custom scan policies. Generates SARIF reports compatible with GitHub Advanced Security code scanning alerts.

## Overview

The OWASP ZAP Active Scanner Agent automates web application security testing using the OWASP ZAP API in daemon mode. It configures custom scan policies that target OWASP Top 10 vulnerabilities including SQL injection, XSS, CSRF, and SSRF using ZAP’s pluggable scanner architecture. The skill starts ZAP in headless daemon mode, configures the target context with authentication credentials via ZAP’s Session Management API, and launches active scans with configurable thread counts and request throttling. Spider crawling uses ZAP’s AJAX Spider with Selenium WebDriver integration for JavaScript-heavy applications. Scan results are parsed from ZAP’s JSON report format and converted to SARIF (Static Analysis Results Interchange Format) for direct import into GitHub Advanced Security code scanning alerts. The skill supports baseline scans for CI/CD pipelines with configurable severity thresholds that gate deployments. False positive management uses ZAP’s alert filter API with persistent exclusion rules stored in a YAML configuration file.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-active-scanner-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-active-scanner-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-active-scanner-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-active-scanner-agent -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-active-scanner-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/owasp-zap-active-scanner-agent/
