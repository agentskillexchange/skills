---
title: "OWASP ZAP API Security Auditor"
description: "The OWASP ZAP API Security Auditor skill leverages the OWASP Zed Attack Proxy (ZAP) Python API to perform Dynamic Application Security Testing (DAST) against web applications and APIs. It supports both active scanning with configurable attack policies and passive scanning for information disclosure detection. The skill orchestrates ZAP&#8217;s spider and AJAX spider modules to discover API endpoints, then runs targeted scans using ZAP&#8217;s scan policies. It parses OpenAPI/Swagger specifications to seed the scanner with endpoint definitions and authentication contexts. Results are enriched with CWE and OWASP Top 10 mappings. Advanced features include authenticated scanning with session token management, GraphQL introspection-based endpoint discovery, and automated false positive suppression using context-aware heuristics. Output formats include HTML reports, JSON for CI integration, and SARIF for GitHub Advanced Security. The skill also generates suggested ModSecurity or Cloudflare WAF rules based on detected vulnerabilities."
source: "https://github.com/zaproxy/zaproxy"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
---

# OWASP ZAP API Security Auditor

The OWASP ZAP API Security Auditor skill leverages the OWASP Zed Attack Proxy (ZAP) Python API to perform Dynamic Application Security Testing (DAST) against web applications and APIs. It supports both active scanning with configurable attack policies and passive scanning for information disclosure detection. The skill orchestrates ZAP&#8217;s spider and AJAX spider modules to discover API endpoints, then runs targeted scans using ZAP&#8217;s scan policies. It parses OpenAPI/Swagger specifications to seed the scanner with endpoint definitions and authentication contexts. Results are enriched with CWE and OWASP Top 10 mappings. Advanced features include authenticated scanning with session token management, GraphQL introspection-based endpoint discovery, and automated false positive suppression using context-aware heuristics. Output formats include HTML reports, JSON for CI integration, and SARIF for GitHub Advanced Security. The skill also generates suggested ModSecurity or Cloudflare WAF rules based on detected vulnerabilities.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-api-security-auditor/)
