---
title: OWASP ZAP Automated Scan Orchestrator
description: The OWASP ZAP Automated Scan Orchestrator leverages the ZAP Docker container
  API to perform comprehensive security assessments against web applications. It initializes
  a headless ZAP instance, configures scan policies for OWASP Top 10 categories, and
  executes both spider crawling and active attack phases. The skill parses the resulting
  JSON report to extract vulnerability findings, categorizing them by CWE ID and risk
  level (High, Medium, Low, Informational). It generates structured output including
  affected URLs, evidence strings, and remediation suggestions mapped to OWASP testing
  guidelines. Supports authentication context for scanning protected endpoints using
  session tokens or API keys. Integrates with CI/CD pipelines by returning non-zero
  exit codes when critical vulnerabilities are detected, and can output SARIF format
  for GitHub Security tab integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/owasp-zap-automated-scan-orchestrator/
category:
- Security &amp; Verification
framework:
- OpenClaw
---

# OWASP ZAP Automated Scan Orchestrator

The OWASP ZAP Automated Scan Orchestrator leverages the ZAP Docker container API to perform comprehensive security assessments against web applications. It initializes a headless ZAP instance, configures scan policies for OWASP Top 10 categories, and executes both spider crawling and active attack phases. The skill parses the resulting JSON report to extract vulnerability findings, categorizing them by CWE ID and risk level (High, Medium, Low, Informational). It generates structured output including affected URLs, evidence strings, and remediation suggestions mapped to OWASP testing guidelines. Supports authentication context for scanning protected endpoints using session tokens or API keys. Integrates with CI/CD pipelines by returning non-zero exit codes when critical vulnerabilities are detected, and can output SARIF format for GitHub Security tab integration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-automated-scan-orchestrator/)
