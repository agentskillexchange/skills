---
title: "OWASP ZAP Scan Orchestrator"
description: "Orchestrates OWASP ZAP active and passive scans via the ZAP API, automating spider crawls, AJAX spidering with Selenium, and generating SARIF-format vulnerability reports."
slug: "owasp-zap-scan-orchestrator"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/owasp-zap-scan-orchestrator/"
---

# OWASP ZAP Scan Orchestrator

Orchestrates OWASP ZAP active and passive scans via the ZAP API, automating spider crawls, AJAX spidering with Selenium, and generating SARIF-format vulnerability reports.

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
clawhub install owasp-zap-scan-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The OWASP ZAP Scan Orchestrator automates comprehensive web application security testing through the ZAP REST API. It configures and launches spider crawls for URL discovery, AJAX spider sessions using Selenium WebDriver for JavaScript-heavy applications, and active scan policies targeting OWASP Top 10 vulnerabilities. The agent manages ZAP contexts for authentication handling including form-based, token-based, and OAuth2 flows. It processes scan results through custom alert filters, maps findings to CWE identifiers, and generates reports in SARIF format for GitHub Security tab integration. The orchestrator supports baseline, full, and API scan types with configurable scan policies, handles session management for authenticated scanning, and integrates with CI/CD pipelines through Docker-based ZAP instances. Includes automatic false positive suppression based on historical scan data.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-scan-orchestrator/)
