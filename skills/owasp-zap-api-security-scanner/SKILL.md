---
name: "OWASP ZAP API Security Scanner"
description: "Automates OWASP ZAP scans against REST APIs using the ZAP Python API client. Imports OpenAPI/Swagger specs for targeted scanning and generates SARIF-format reports for GitHub Security tab integration."
category: "Security & Verification"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/zaproxy/zaproxy"
tool_ecosystem:
  tool: owasp
  github_stars: 14900
  github_repo: zaproxy/zaproxy
  license: Apache-2.0
  maintained: true
---

# OWASP ZAP API Security Scanner

Automates OWASP ZAP scans against REST APIs using the ZAP Python API client. Imports OpenAPI/Swagger specs for targeted scanning and generates SARIF-format reports for GitHub Security tab integration.

## Overview

This skill automates web application and API security testing using OWASP ZAP (Zed Attack Proxy) via its Python API client. It starts ZAP in daemon mode, imports OpenAPI/Swagger specifications to discover all API endpoints, and runs targeted active and passive scans against them. The skill configures scan policies based on OWASP Top 10 categories, focusing on injection attacks, broken authentication, sensitive data exposure, and security misconfiguration. It manages ZAP contexts for authenticated scanning using session tokens or API keys, configures anti-CSRF token handling, and sets appropriate scan strength and threshold levels. Spider and AJAX Spider modules map application attack surfaces before active scanning begins. Results are exported in multiple formats including SARIF for GitHub Security tab integration, HTML for human review, and JSON for programmatic processing. The skill supports baseline scans for CI/CD pipelines with configurable fail thresholds and can compare scan results across runs to identify new vulnerabilities.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-security-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-security-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-security-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-security-scanner -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-api-security-scanner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/owasp-zap-api-security-scanner/
