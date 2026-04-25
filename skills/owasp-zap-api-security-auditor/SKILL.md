---
title: "OWASP ZAP API Security Auditor"
description: "Orchestrates OWASP ZAP active and passive scans against REST and GraphQL endpoints using ZAP’s Python API client. Generates DAST reports with CWE mappings and suggests WAF rule configurations."
verification: "security_reviewed"
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security & Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
---

# OWASP ZAP API Security Auditor

The OWASP ZAP API Security Auditor skill leverages the OWASP Zed Attack Proxy (ZAP) Python API to perform Dynamic Application Security Testing (DAST) against web applications and APIs. It supports both active scanning with configurable attack policies and passive scanning for information disclosure detection. The skill orchestrates ZAP’s spider and AJAX spider modules to discover API endpoints, then runs targeted scans using ZAP’s scan policies. It parses OpenAPI/Swagger specifications to seed the scanner with endpoint definitions and authentication contexts. Results are enriched with CWE and OWASP Top 10 mappings. Advanced features include authenticated scanning with session token management, GraphQL introspection-based endpoint discovery, and automated false positive suppression using context-aware heuristics. Output formats include HTML reports, JSON for CI integration, and SARIF for GitHub Advanced Security. The skill also generates suggested ModSecurity or Cloudflare WAF rules based on detected vulnerabilities.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/owasp-zap-api-security-auditor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/owasp-zap-api-security-auditor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/owasp-zap-api-security-auditor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-api-security-auditor/)
