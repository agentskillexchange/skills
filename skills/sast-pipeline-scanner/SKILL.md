---
title: "SAST Pipeline Scanner"
description: "The SAST Pipeline Scanner skill integrates static application security testing directly into your CI/CD pipeline through agent automation. It orchestrates Semgrep&#8217;s pattern-matching engine with custom rule sets targeting OWASP Top 10 vulnerabilities, and leverages CodeQL&#8217;s semantic code analysis for deeper taint-tracking across function boundaries. When triggered on pull request events, the skill analyzes only the changed diff to minimize scan time, while maintaining a baseline of full-repository findings. Results are formatted in SARIF (Static Analysis Results Interchange Format) for compatibility with GitHub Advanced Security&#8217;s code scanning alerts dashboard. Configuration supports custom Semgrep rule registries, CodeQL query suites for specific languages (Python, JavaScript, Go, Java, C#), severity threshold gating for CI pass/fail decisions, and inline PR comment annotations with remediation guidance. The skill also tracks false positive suppressions across scans to reduce developer alert fatigue over time."
source: "https://agentskillexchange.com/skills/sast-pipeline-scanner/"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
---

# SAST Pipeline Scanner

The SAST Pipeline Scanner skill integrates static application security testing directly into your CI/CD pipeline through agent automation. It orchestrates Semgrep&#8217;s pattern-matching engine with custom rule sets targeting OWASP Top 10 vulnerabilities, and leverages CodeQL&#8217;s semantic code analysis for deeper taint-tracking across function boundaries. When triggered on pull request events, the skill analyzes only the changed diff to minimize scan time, while maintaining a baseline of full-repository findings. Results are formatted in SARIF (Static Analysis Results Interchange Format) for compatibility with GitHub Advanced Security&#8217;s code scanning alerts dashboard. Configuration supports custom Semgrep rule registries, CodeQL query suites for specific languages (Python, JavaScript, Go, Java, C#), severity threshold gating for CI pass/fail decisions, and inline PR comment annotations with remediation guidance. The skill also tracks false positive suppressions across scans to reduce developer alert fatigue over time.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sast-pipeline-scanner/)
