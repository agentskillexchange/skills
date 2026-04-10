---
name: "OWASP ZAP Security Scanner Agent"
description: "Automates OWASP ZAP active and passive scanning against web applications, parsing alerts into structured vulnerability reports. Integrates with the ZAP API daemon to manage contexts, spider targets, and export SARIF-formatted findings."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/owasp-zap-security-scanner-agent/"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
---

# OWASP ZAP Security Scanner Agent

This skill provides comprehensive web application security testing through the OWASP ZAP proxy API. It launches ZAP in daemon mode, configures authentication contexts for target applications, and orchestrates both passive and active scan policies. The agent manages spider crawling to discover endpoints, runs AJAX spider for JavaScript-heavy applications, and applies custom scan policies targeting OWASP Top 10 categories. Results are parsed from ZAP's JSON alert API and transformed into SARIF format for integration with GitHub Advanced Security, GitLab SAST, or Azure DevOps. The skill supports authenticated scanning via form-based, JSON-based, and header-based authentication methods. It can compare scan baselines to identify new vulnerabilities introduced between releases. Alert filtering by risk level and confidence allows teams to focus on actionable findings while suppressing known false positives through a persistent baseline file.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-security-scanner-agent/)
