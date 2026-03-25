---
name: "OWASP ZAP API Security Auditor"
description: "Orchestrates OWASP ZAP active and passive scans against REST and GraphQL endpoints using ZAP’s Python API client. Generates DAST reports with CWE mappings and suggests WAF rule configurations."
category: "Security & Verification"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/owasp-zap-api-security-auditor/"
tool_ecosystem:
  tool: "owasp"
  github_stars: 14900
  github_repo: "zaproxy/zaproxy"
  license: "Apache-2.0"
  maintained: true
---

# OWASP ZAP API Security Auditor

Orchestrates OWASP ZAP active and passive scans against REST and GraphQL endpoints using ZAP’s Python API client. Generates DAST reports with CWE mappings and suggests WAF rule configurations.

## Overview

The OWASP ZAP API Security Auditor skill leverages the **OWASP Zed Attack Proxy (ZAP)** Python API to perform Dynamic Application Security Testing (DAST) against web applications and APIs. It supports both active scanning with configurable attack policies and passive scanning for information disclosure detection.

The skill orchestrates ZAP’s spider and AJAX spider modules to discover API endpoints, then runs targeted scans using ZAP’s scan policies. It parses OpenAPI/Swagger specifications to seed the scanner with endpoint definitions and authentication contexts. Results are enriched with CWE and OWASP Top 10 mappings.

Advanced features include authenticated scanning with session token management, GraphQL introspection-based endpoint discovery, and automated false positive suppression using context-aware heuristics. Output formats include HTML reports, JSON for CI integration, and SARIF for GitHub Advanced Security. The skill also generates suggested ModSecurity or Cloudflare WAF rules based on detected vulnerabilities.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-security-auditor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-security-auditor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-security-auditor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-security-auditor -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-api-security-auditor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/owasp-zap-api-security-auditor/
