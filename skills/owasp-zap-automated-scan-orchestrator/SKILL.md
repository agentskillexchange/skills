---
name: "OWASP ZAP Automated Scan Orchestrator"
description: "Runs OWASP ZAP active and passive scans against target URLs using the ZAP Docker API. Parses JSON reports to flag XSS, SQLi, and CSRF vulnerabilities with severity scoring."
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
# OWASP ZAP Automated Scan Orchestrator

Runs OWASP ZAP active and passive scans against target URLs using the ZAP Docker API. Parses JSON reports to flag XSS, SQLi, and CSRF vulnerabilities with severity scoring.

## Overview

The OWASP ZAP Automated Scan Orchestrator leverages the ZAP Docker container API to perform comprehensive security assessments against web applications. It initializes a headless ZAP instance, configures scan policies for OWASP Top 10 categories, and executes both spider crawling and active attack phases. The skill parses the resulting JSON report to extract vulnerability findings, categorizing them by CWE ID and risk level (High, Medium, Low, Informational). It generates structured output including affected URLs, evidence strings, and remediation suggestions mapped to OWASP testing guidelines. Supports authentication context for scanning protected endpoints using session tokens or API keys. Integrates with CI/CD pipelines by returning non-zero exit codes when critical vulnerabilities are detected, and can output SARIF format for GitHub Security tab integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-automated-scan-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-automated-scan-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-automated-scan-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-automated-scan-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-automated-scan-orchestrator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-automated-scan-orchestrator/)
