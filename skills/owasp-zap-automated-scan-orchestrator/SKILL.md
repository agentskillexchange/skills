---
title: "OWASP ZAP Automated Scan Orchestrator"
description: "The OWASP ZAP Automated Scan Orchestrator leverages the ZAP Docker container API to perform comprehensive security assessments against web applications. It initializes a headless ZAP instance, configures scan policies for OWASP Top 10 categories, and executes both spider crawling and active attack phases. The skill parses the resulting JSON report to extract vulnerability findings, categorizing them by CWE ID and risk level (High, Medium, Low, Informational). It generates structured output including affected URLs, evidence strings, and remediation suggestions mapped to OWASP testing guidelines. Supports authentication context for scanning protected endpoints using session tokens or API keys. Integrates with CI/CD pipelines by returning non-zero exit codes when critical vulnerabilities are detected, and can output SARIF format for GitHub Security tab integration."
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

# OWASP ZAP Automated Scan Orchestrator

The OWASP ZAP Automated Scan Orchestrator leverages the ZAP Docker container API to perform comprehensive security assessments against web applications. It initializes a headless ZAP instance, configures scan policies for OWASP Top 10 categories, and executes both spider crawling and active attack phases. The skill parses the resulting JSON report to extract vulnerability findings, categorizing them by CWE ID and risk level (High, Medium, Low, Informational). It generates structured output including affected URLs, evidence strings, and remediation suggestions mapped to OWASP testing guidelines. Supports authentication context for scanning protected endpoints using session tokens or API keys. Integrates with CI/CD pipelines by returning non-zero exit codes when critical vulnerabilities are detected, and can output SARIF format for GitHub Security tab integration.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-automated-scan-orchestrator/)
