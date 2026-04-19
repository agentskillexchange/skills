---
title: "OWASP ZAP Security Scanner Agent"
description: "This skill provides comprehensive web application security testing through the OWASP ZAP proxy API. It launches ZAP in daemon mode, configures authentication contexts for target applications, and orchestrates both passive and active scan policies. The agent manages spider crawling to discover endpoints, runs AJAX spider for JavaScript-heavy applications, and applies custom scan policies targeting OWASP Top 10 categories. Results are parsed from ZAP&#8217;s JSON alert API and transformed into SARIF format for integration with GitHub Advanced Security, GitLab SAST, or Azure DevOps. The skill supports authenticated scanning via form-based, JSON-based, and header-based authentication methods. It can compare scan baselines to identify new vulnerabilities introduced between releases. Alert filtering by risk level and confidence allows teams to focus on actionable findings while suppressing known false positives through a persistent baseline file."
source: "https://github.com/zaproxy/zaproxy"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
---

# OWASP ZAP Security Scanner Agent

This skill provides comprehensive web application security testing through the OWASP ZAP proxy API. It launches ZAP in daemon mode, configures authentication contexts for target applications, and orchestrates both passive and active scan policies. The agent manages spider crawling to discover endpoints, runs AJAX spider for JavaScript-heavy applications, and applies custom scan policies targeting OWASP Top 10 categories. Results are parsed from ZAP&#8217;s JSON alert API and transformed into SARIF format for integration with GitHub Advanced Security, GitLab SAST, or Azure DevOps. The skill supports authenticated scanning via form-based, JSON-based, and header-based authentication methods. It can compare scan baselines to identify new vulnerabilities introduced between releases. Alert filtering by risk level and confidence allows teams to focus on actionable findings while suppressing known false positives through a persistent baseline file.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-security-scanner-agent/)
