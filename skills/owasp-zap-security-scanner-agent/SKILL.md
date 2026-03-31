---
name: "OWASP ZAP Security Scanner Agent"
description: "Automates OWASP ZAP active and passive scanning against web applications, parsing alerts into structured vulnerability reports. Integrates with the ZAP API daemon to manage contexts, spider targets, and export SARIF-formatted findings."
category: "Security &amp; Verification"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/zaproxy/zaproxy"
tool_ecosystem:
  tool: owasp
  github_repo: zaproxy/zaproxy
  github_stars: 14928
  license: Apache-2.0
  maintained: true
---
# OWASP ZAP Security Scanner Agent

Automates OWASP ZAP active and passive scanning against web applications, parsing alerts into structured vulnerability reports. Integrates with the ZAP API daemon to manage contexts, spider targets, and export SARIF-formatted findings.

## Overview

This skill provides comprehensive web application security testing through the OWASP ZAP proxy API. It launches ZAP in daemon mode, configures authentication contexts for target applications, and orchestrates both passive and active scan policies. The agent manages spider crawling to discover endpoints, runs AJAX spider for JavaScript-heavy applications, and applies custom scan policies targeting OWASP Top 10 categories. Results are parsed from ZAP's JSON alert API and transformed into SARIF format for integration with GitHub Advanced Security, GitLab SAST, or Azure DevOps. The skill supports authenticated scanning via form-based, JSON-based, and header-based authentication methods. It can compare scan baselines to identify new vulnerabilities introduced between releases. Alert filtering by risk level and confidence allows teams to focus on actionable findings while suppressing known false positives through a persistent baseline file.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-security-scanner-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-security-scanner-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-security-scanner-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-security-scanner-agent -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-security-scanner-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-security-scanner-agent/)
