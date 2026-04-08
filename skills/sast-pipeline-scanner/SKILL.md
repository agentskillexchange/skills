---
title: SAST Pipeline Scanner
description: The SAST Pipeline Scanner skill integrates static application security
  testing directly into your CI/CD pipeline through agent automation. It orchestrates
  Semgrep’s pattern-matching engine with custom rule sets targeting OWASP Top 10 vulnerabilities,
  and leverages CodeQL’s semantic code analysis for deeper taint-tracking across function
  boundaries. When triggered on pull request events, the skill analyzes only the changed
  diff to minimize scan time, while maintaining a baseline of full-repository findings.
  Results are formatted in SARIF (Static Analysis Results Interchange Format) for
  compatibility with GitHub Advanced Security’s code scanning alerts dashboard. Configuration
  supports custom Semgrep rule registries, CodeQL query suites for specific languages
  (Python, JavaScript, Go, Java, C#), severity threshold gating for CI pass/fail decisions,
  and inline PR comment annotations with remediation guidance. The skill also tracks
  false positive suppressions across scans to reduce developer alert fatigue over
  time.
verification: security_reviewed
source: https://agentskillexchange.com/skills/sast-pipeline-scanner/
category:
- Security &amp; Verification
framework:
- Claude Code
---

# SAST Pipeline Scanner

The SAST Pipeline Scanner skill integrates static application security testing directly into your CI/CD pipeline through agent automation. It orchestrates Semgrep’s pattern-matching engine with custom rule sets targeting OWASP Top 10 vulnerabilities, and leverages CodeQL’s semantic code analysis for deeper taint-tracking across function boundaries. When triggered on pull request events, the skill analyzes only the changed diff to minimize scan time, while maintaining a baseline of full-repository findings. Results are formatted in SARIF (Static Analysis Results Interchange Format) for compatibility with GitHub Advanced Security’s code scanning alerts dashboard. Configuration supports custom Semgrep rule registries, CodeQL query suites for specific languages (Python, JavaScript, Go, Java, C#), severity threshold gating for CI pass/fail decisions, and inline PR comment annotations with remediation guidance. The skill also tracks false positive suppressions across scans to reduce developer alert fatigue over time.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sast-pipeline-scanner/)
