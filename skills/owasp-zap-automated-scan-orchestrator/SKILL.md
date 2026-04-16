---
title: "OWASP ZAP Automated Scan Orchestrator"
description: "Runs OWASP ZAP active and passive scans against target URLs using the ZAP Docker API. Parses JSON reports to flag XSS, SQLi, and CSRF vulnerabilities with severity scoring."
verification: "security_reviewed"
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
  license: "Apache-2.0"
---

# OWASP ZAP Automated Scan Orchestrator

The OWASP ZAP Automated Scan Orchestrator leverages the ZAP Docker container API to perform comprehensive security assessments against web applications. It initializes a headless ZAP instance, configures scan policies for OWASP Top 10 categories, and executes both spider crawling and active attack phases. The skill parses the resulting JSON report to extract vulnerability findings, categorizing them by CWE ID and risk level (High, Medium, Low, Informational). It generates structured output including affected URLs, evidence strings, and remediation suggestions mapped to OWASP testing guidelines. Supports authentication context for scanning protected endpoints using session tokens or API keys. Integrates with CI/CD pipelines by returning non-zero exit codes when critical vulnerabilities are detected, and can output SARIF format for GitHub Security tab integration.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-automated-scan-orchestrator/)
