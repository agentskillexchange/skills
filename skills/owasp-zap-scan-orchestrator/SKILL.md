---
name: OWASP ZAP Scan Orchestrator
description: Orchestrates OWASP ZAP active and passive scans via the ZAP API, automating
  spider crawls, AJAX spidering with Selenium, and generating SARIF-format vulnerability
  reports.
verification: security_reviewed
source: https://agentskillexchange.com/skills/owasp-zap-scan-orchestrator/
category:
- Security &amp; Verification
framework:
- Codex
---
# OWASP ZAP Scan Orchestrator

The OWASP ZAP Scan Orchestrator automates comprehensive web application security testing through the ZAP REST API. It configures and launches spider crawls for URL discovery, AJAX spider sessions using Selenium WebDriver for JavaScript-heavy applications, and active scan policies targeting OWASP Top 10 vulnerabilities. The agent manages ZAP contexts for authentication handling including form-based, token-based, and OAuth2 flows. It processes scan results through custom alert filters, maps findings to CWE identifiers, and generates reports in SARIF format for GitHub Security tab integration. The orchestrator supports baseline, full, and API scan types with configurable scan policies, handles session management for authenticated scanning, and integrates with CI/CD pipelines through Docker-based ZAP instances. Includes automatic false positive suppression based on historical scan data.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-scan-orchestrator/)
