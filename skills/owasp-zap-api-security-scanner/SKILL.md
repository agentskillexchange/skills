---
title: OWASP ZAP API Security Scanner
description: This skill automates web application and API security testing using OWASP
  ZAP (Zed Attack Proxy) via its Python API client. It starts ZAP in daemon mode,
  imports OpenAPI/Swagger specifications to discover all API endpoints, and runs targeted
  active and passive scans against them. The skill configures scan policies based
  on OWASP Top 10 categories, focusing on injection attacks, broken authentication,
  sensitive data exposure, and security misconfiguration. It manages ZAP contexts
  for authenticated scanning using session tokens or API keys, configures anti-CSRF
  token handling, and sets appropriate scan strength and threshold levels. Spider
  and AJAX Spider modules map application attack surfaces before active scanning begins.
  Results are exported in multiple formats including SARIF for GitHub Security tab
  integration, HTML for human review, and JSON for programmatic processing. The skill
  supports baseline scans for CI/CD pipelines with configurable fail thresholds and
  can compare scan results across runs to identify new vulnerabilities.
verification: security_reviewed
source: https://agentskillexchange.com/skills/owasp-zap-api-security-scanner/
category:
- Security &amp; Verification
framework:
- Gemini
---

# OWASP ZAP API Security Scanner

This skill automates web application and API security testing using OWASP ZAP (Zed Attack Proxy) via its Python API client. It starts ZAP in daemon mode, imports OpenAPI/Swagger specifications to discover all API endpoints, and runs targeted active and passive scans against them. The skill configures scan policies based on OWASP Top 10 categories, focusing on injection attacks, broken authentication, sensitive data exposure, and security misconfiguration. It manages ZAP contexts for authenticated scanning using session tokens or API keys, configures anti-CSRF token handling, and sets appropriate scan strength and threshold levels. Spider and AJAX Spider modules map application attack surfaces before active scanning begins. Results are exported in multiple formats including SARIF for GitHub Security tab integration, HTML for human review, and JSON for programmatic processing. The skill supports baseline scans for CI/CD pipelines with configurable fail thresholds and can compare scan results across runs to identify new vulnerabilities.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-api-security-scanner/)
