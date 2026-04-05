---
name: "OWASP ZAP API Fuzzer"
description: "Automates REST API security testing using the OWASP ZAP Python SDK. Runs active scans, SQL injection probes, and XSS tests against OpenAPI specs with structured vulnerability reports."
category: "Security &amp; Verification"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/owasp-zap-api-fuzzer/"
---
# OWASP ZAP API Fuzzer

Automates REST API security testing using the OWASP ZAP Python SDK. Runs active scans, SQL injection probes, and XSS tests against OpenAPI specs with structured vulnerability reports.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-fuzzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-fuzzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-fuzzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-fuzzer -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-api-fuzzer
```

## Details

Automates REST API security testing using the OWASP ZAP Python SDK. Runs active scans, SQL injection probes, and XSS tests against OpenAPI specs with structured vulnerability reports.

This skill provides automated tooling for owasp zap api fuzzer workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-api-fuzzer/)
