---
title: OWASP ZAP Scan Orchestrator
description: The OWASP ZAP Scan Orchestrator automates comprehensive web application
  security testing through the ZAP REST API. It configures and launches spider crawls
  for URL discovery, AJAX spider sessions using Selenium WebDriver for JavaScript-heavy
  applications, and active scan policies targeting OWASP Top 10 vulnerabilities. The
  agent manages ZAP contexts for authentication handling including form-based, token-based,
  and OAuth2 flows. It processes scan results through custom alert filters, maps findings
  to CWE identifiers, and generates reports in SARIF format for GitHub Security tab
  integration. The orchestrator supports baseline, full, and API scan types with configurable
  scan policies, handles session management for authenticated scanning, and integrates
  with CI/CD pipelines through Docker-based ZAP instances. Includes automatic false
  positive suppression based on historical scan data.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-scan-orchestrator/)
