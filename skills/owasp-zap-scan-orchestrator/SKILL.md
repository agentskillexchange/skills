---
title: "OWASP ZAP Scan Orchestrator"
description: "Orchestrates OWASP ZAP active and passive scans via the ZAP API, automating spider crawls, AJAX spidering with Selenium, and generating SARIF-format vulnerability reports."
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

# OWASP ZAP Scan Orchestrator

The OWASP ZAP Scan Orchestrator automates comprehensive web application security testing through the ZAP REST API. It configures and launches spider crawls for URL discovery, AJAX spider sessions using Selenium WebDriver for JavaScript-heavy applications, and active scan policies targeting OWASP Top 10 vulnerabilities. The agent manages ZAP contexts for authentication handling including form-based, token-based, and OAuth2 flows. It processes scan results through custom alert filters, maps findings to CWE identifiers, and generates reports in SARIF format for GitHub Security tab integration. The orchestrator supports baseline, full, and API scan types with configurable scan policies, handles session management for authenticated scanning, and integrates with CI/CD pipelines through Docker-based ZAP instances. Includes automatic false positive suppression based on historical scan data.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/owasp-zap-scan-orchestrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/owasp-zap-scan-orchestrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-scan-orchestrator/)
