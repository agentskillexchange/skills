---
title: "OWASP ZAP Security Scanner Agent"
description: "Automates OWASP ZAP active and passive scanning against web applications, parsing alerts into structured vulnerability reports. Integrates with the ZAP API daemon to manage contexts, spider targets, and export SARIF-formatted findings."
verification: security_reviewed
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
---

# OWASP ZAP Security Scanner Agent

This skill provides comprehensive web application security testing through the OWASP ZAP proxy API. It launches ZAP in daemon mode, configures authentication contexts for target applications, and orchestrates both passive and active scan policies. The agent manages spider crawling to discover endpoints, runs AJAX spider for JavaScript-heavy applications, and applies custom scan policies targeting OWASP Top 10 categories. Results are parsed from ZAP’s JSON alert API and transformed into SARIF format for integration with GitHub Advanced Security, GitLab SAST, or Azure DevOps. The skill supports authenticated scanning via form-based, JSON-based, and header-based authentication methods. It can compare scan baselines to identify new vulnerabilities introduced between releases. Alert filtering by risk level and confidence allows teams to focus on actionable findings while suppressing known false positives through a persistent baseline file.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-security-scanner-agent/)
