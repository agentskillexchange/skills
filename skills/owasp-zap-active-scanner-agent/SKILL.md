---
title: "OWASP ZAP Active Scanner Agent"
description: "The OWASP ZAP Active Scanner Agent automates web application security testing using the OWASP ZAP API in daemon mode. It configures custom scan policies that target OWASP Top 10 vulnerabilities including SQL injection, XSS, CSRF, and SSRF using ZAP&#8217;s pluggable scanner architecture. The skill starts ZAP in headless daemon mode, configures the target context with authentication credentials via ZAP&#8217;s Session Management API, and launches active scans with configurable thread counts and request throttling. Spider crawling uses ZAP&#8217;s AJAX Spider with Selenium WebDriver integration for JavaScript-heavy applications. Scan results are parsed from ZAP&#8217;s JSON report format and converted to SARIF (Static Analysis Results Interchange Format) for direct import into GitHub Advanced Security code scanning alerts. The skill supports baseline scans for CI/CD pipelines with configurable severity thresholds that gate deployments. False positive management uses ZAP&#8217;s alert filter API with persistent exclusion rules stored in a YAML configuration file."
source: "https://github.com/zaproxy/zaproxy"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
---

# OWASP ZAP Active Scanner Agent

The OWASP ZAP Active Scanner Agent automates web application security testing using the OWASP ZAP API in daemon mode. It configures custom scan policies that target OWASP Top 10 vulnerabilities including SQL injection, XSS, CSRF, and SSRF using ZAP&#8217;s pluggable scanner architecture. The skill starts ZAP in headless daemon mode, configures the target context with authentication credentials via ZAP&#8217;s Session Management API, and launches active scans with configurable thread counts and request throttling. Spider crawling uses ZAP&#8217;s AJAX Spider with Selenium WebDriver integration for JavaScript-heavy applications. Scan results are parsed from ZAP&#8217;s JSON report format and converted to SARIF (Static Analysis Results Interchange Format) for direct import into GitHub Advanced Security code scanning alerts. The skill supports baseline scans for CI/CD pipelines with configurable severity thresholds that gate deployments. False positive management uses ZAP&#8217;s alert filter API with persistent exclusion rules stored in a YAML configuration file.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-active-scanner-agent/)
