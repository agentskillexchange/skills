---
name: "OWASP ZAP API Security Auditor"
description: "Orchestrates OWASP ZAP active and passive scans against REST and GraphQL endpoints using ZAP's Python API client. Generates DAST reports with CWE mappings and suggests WAF rule configurations."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/owasp-zap-api-security-auditor/"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
---

# OWASP ZAP API Security Auditor

The OWASP ZAP API Security Auditor skill leverages the OWASP Zed Attack Proxy (ZAP) Python API to perform Dynamic Application Security Testing (DAST) against web applications and APIs. It supports both active scanning with configurable attack policies and passive scanning for information disclosure detection.
The skill orchestrates ZAP's spider and AJAX spider modules to discover API endpoints, then runs targeted scans using ZAP's scan policies. It parses OpenAPI/Swagger specifications to seed the scanner with endpoint definitions and authentication contexts. Results are enriched with CWE and OWASP Top 10 mappings.
Advanced features include authenticated scanning with session token management, GraphQL introspection-based endpoint discovery, and automated false positive suppression using context-aware heuristics. Output formats include HTML reports, JSON for CI integration, and SARIF for GitHub Advanced Security. The skill also generates suggested ModSecurity or Cloudflare WAF rules based on detected vulnerabilities.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-api-security-auditor/)
