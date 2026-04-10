---
title: "OWASP ZAP API Security Auditor"
description: "Orchestrates OWASP ZAP active and passive scans against REST and GraphQL endpoints using ZAP’s Python API client. Generates DAST reports with CWE mappings and suggests WAF rule configurations."
slug: "owasp-zap-api-security-auditor"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/owasp-zap-api-security-auditor/"
listed: true
---

# OWASP ZAP API Security Auditor

Orchestrates OWASP ZAP active and passive scans against REST and GraphQL endpoints using ZAP’s Python API client. Generates DAST reports with CWE mappings and suggests WAF rule configurations.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install owasp-zap-api-security-auditor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The OWASP ZAP API Security Auditor skill leverages the OWASP Zed Attack Proxy (ZAP) Python API to perform Dynamic Application Security Testing (DAST) against web applications and APIs. It supports both active scanning with configurable attack policies and passive scanning for information disclosure detection.
The skill orchestrates ZAP’s spider and AJAX spider modules to discover API endpoints, then runs targeted scans using ZAP’s scan policies. It parses OpenAPI/Swagger specifications to seed the scanner with endpoint definitions and authentication contexts. Results are enriched with CWE and OWASP Top 10 mappings.
Advanced features include authenticated scanning with session token management, GraphQL introspection-based endpoint discovery, and automated false positive suppression using context-aware heuristics. Output formats include HTML reports, JSON for CI integration, and SARIF for GitHub Advanced Security. The skill also generates suggested ModSecurity or Cloudflare WAF rules based on detected vulnerabilities.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-api-security-auditor/)
