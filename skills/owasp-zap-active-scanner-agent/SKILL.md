---
title: "OWASP ZAP Active Scanner Agent"
description: "Runs OWASP ZAP active security scans via the ZAP API daemon with custom scan policies. Generates SARIF reports compatible with GitHub Advanced Security code scanning alerts."
verification: security_reviewed
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
---

# OWASP ZAP Active Scanner Agent

The OWASP ZAP Active Scanner Agent automates web application security testing using the OWASP ZAP API in daemon mode. It configures custom scan policies that target OWASP Top 10 vulnerabilities including SQL injection, XSS, CSRF, and SSRF using ZAP’s pluggable scanner architecture. The skill starts ZAP in headless daemon mode, configures the target context with authentication credentials via ZAP’s Session Management API, and launches active scans with configurable thread counts and request throttling. Spider crawling uses ZAP’s AJAX Spider with Selenium WebDriver integration for JavaScript-heavy applications. Scan results are parsed from ZAP’s JSON report format and converted to SARIF (Static Analysis Results Interchange Format) for direct import into GitHub Advanced Security code scanning alerts. The skill supports baseline scans for CI/CD pipelines with configurable severity thresholds that gate deployments. False positive management uses ZAP’s alert filter API with persistent exclusion rules stored in a YAML configuration file.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-active-scanner-agent/)
