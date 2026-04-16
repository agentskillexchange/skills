---
title: "OWASP ZAP Scan Orchestrator"
description: "Orchestrates OWASP ZAP active and passive scans via the ZAP API, automating spider crawls, AJAX spidering with Selenium, and generating SARIF-format vulnerability reports."
verification: "security_reviewed"
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security &amp; Verification"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-scan-orchestrator/)
