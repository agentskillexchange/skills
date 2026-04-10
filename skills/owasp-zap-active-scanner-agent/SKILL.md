---
name: "OWASP ZAP Active Scanner Agent"
description: "Runs OWASP ZAP active security scans via the ZAP API daemon with custom scan policies. Generates SARIF reports compatible with GitHub Advanced Security code scanning alerts."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/owasp-zap-active-scanner-agent/"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
---

# OWASP ZAP Active Scanner Agent

The OWASP ZAP Active Scanner Agent automates web application security testing using the OWASP ZAP API in daemon mode. It configures custom scan policies that target OWASP Top 10 vulnerabilities including SQL injection, XSS, CSRF, and SSRF using ZAP's pluggable scanner architecture. The skill starts ZAP in headless daemon mode, configures the target context with authentication credentials via ZAP's Session Management API, and launches active scans with configurable thread counts and request throttling. Spider crawling uses ZAP's AJAX Spider with Selenium WebDriver integration for JavaScript-heavy applications. Scan results are parsed from ZAP's JSON report format and converted to SARIF (Static Analysis Results Interchange Format) for direct import into GitHub Advanced Security code scanning alerts. The skill supports baseline scans for CI/CD pipelines with configurable severity thresholds that gate deployments. False positive management uses ZAP's alert filter API with persistent exclusion rules stored in a YAML configuration file.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-active-scanner-agent/)
