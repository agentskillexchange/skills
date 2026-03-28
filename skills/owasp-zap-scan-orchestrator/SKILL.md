---
name: "OWASP ZAP Scan Orchestrator"
description: "Orchestrates OWASP ZAP active and passive scans via the ZAP API, automating spider crawls, AJAX spidering with Selenium, and generating SARIF-format vulnerability reports."
category: "Security & Verification"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/zaproxy/zaproxy"
tool_ecosystem:
  tool: owasp
  github_stars: 14900
  github_repo: zaproxy/zaproxy
  license: Apache-2.0
  maintained: true
---

# OWASP ZAP Scan Orchestrator

Orchestrates OWASP ZAP active and passive scans via the ZAP API, automating spider crawls, AJAX spidering with Selenium, and generating SARIF-format vulnerability reports.

## Overview

The OWASP ZAP Scan Orchestrator automates comprehensive web application security testing through the ZAP REST API. It configures and launches spider crawls for URL discovery, AJAX spider sessions using Selenium WebDriver for JavaScript-heavy applications, and active scan policies targeting OWASP Top 10 vulnerabilities. The agent manages ZAP contexts for authentication handling including form-based, token-based, and OAuth2 flows. It processes scan results through custom alert filters, maps findings to CWE identifiers, and generates reports in SARIF format for GitHub Security tab integration. The orchestrator supports baseline, full, and API scan types with configurable scan policies, handles session management for authenticated scanning, and integrates with CI/CD pipelines through Docker-based ZAP instances. Includes automatic false positive suppression based on historical scan data.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scan-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scan-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scan-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scan-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-scan-orchestrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/owasp-zap-scan-orchestrator/
