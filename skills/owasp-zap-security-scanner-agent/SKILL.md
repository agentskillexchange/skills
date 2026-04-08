---
title: OWASP ZAP Security Scanner Agent
description: This skill provides comprehensive web application security testing through
  the OWASP ZAP proxy API. It launches ZAP in daemon mode, configures authentication
  contexts for target applications, and orchestrates both passive and active scan
  policies. The agent manages spider crawling to discover endpoints, runs AJAX spider
  for JavaScript-heavy applications, and applies custom scan policies targeting OWASP
  Top 10 categories. Results are parsed from ZAP’s JSON alert API and transformed
  into SARIF format for integration with GitHub Advanced Security, GitLab SAST, or
  Azure DevOps. The skill supports authenticated scanning via form-based, JSON-based,
  and header-based authentication methods. It can compare scan baselines to identify
  new vulnerabilities introduced between releases. Alert filtering by risk level and
  confidence allows teams to focus on actionable findings while suppressing known
  false positives through a persistent baseline file.
verification: security_reviewed
source: https://agentskillexchange.com/skills/owasp-zap-security-scanner-agent/
category:
- Security &amp; Verification
framework:
- OpenClaw
---

# OWASP ZAP Security Scanner Agent

This skill provides comprehensive web application security testing through the OWASP ZAP proxy API. It launches ZAP in daemon mode, configures authentication contexts for target applications, and orchestrates both passive and active scan policies. The agent manages spider crawling to discover endpoints, runs AJAX spider for JavaScript-heavy applications, and applies custom scan policies targeting OWASP Top 10 categories. Results are parsed from ZAP’s JSON alert API and transformed into SARIF format for integration with GitHub Advanced Security, GitLab SAST, or Azure DevOps. The skill supports authenticated scanning via form-based, JSON-based, and header-based authentication methods. It can compare scan baselines to identify new vulnerabilities introduced between releases. Alert filtering by risk level and confidence allows teams to focus on actionable findings while suppressing known false positives through a persistent baseline file.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-security-scanner-agent/)
