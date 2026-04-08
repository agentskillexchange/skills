---
title: OWASP ZAP API Security Tester
description: The OWASP ZAP API Security Tester automates Dynamic Application Security
  Testing (DAST) for web APIs using the OWASP ZAP proxy daemon and its REST API. It
  supports both traditional REST endpoints and GraphQL schemas for comprehensive API
  surface coverage. The skill connects to ZAP via its JSON API on port 8080, configuring
  scan policies for OWASP Top 10 categories including SQL injection, XSS, broken authentication,
  and security misconfiguration. GraphQL introspection queries are used to enumerate
  all available queries and mutations for targeted fuzzing. Active scanning modules
  test for parameter tampering, IDOR vulnerabilities, JWT token weaknesses, and CORS
  policy misconfigurations. The agent supports both authenticated and unauthenticated
  scanning modes with configurable authentication scripts for OAuth2, API key, and
  session-based auth flows. Scan results are exported as HTML reports with severity-ranked
  findings, each including specific remediation guidance and code examples. Integration
  with Jira and GitHub Issues enables automated ticket creation for critical findings.
  The skill supports baseline scan comparison to track security posture over time.
verification: security_reviewed
source: https://agentskillexchange.com/skills/owasp-zap-api-security-tester/
category:
- Security &amp; Verification
framework:
- Codex
---

# OWASP ZAP API Security Tester

The OWASP ZAP API Security Tester automates Dynamic Application Security Testing (DAST) for web APIs using the OWASP ZAP proxy daemon and its REST API. It supports both traditional REST endpoints and GraphQL schemas for comprehensive API surface coverage. The skill connects to ZAP via its JSON API on port 8080, configuring scan policies for OWASP Top 10 categories including SQL injection, XSS, broken authentication, and security misconfiguration. GraphQL introspection queries are used to enumerate all available queries and mutations for targeted fuzzing. Active scanning modules test for parameter tampering, IDOR vulnerabilities, JWT token weaknesses, and CORS policy misconfigurations. The agent supports both authenticated and unauthenticated scanning modes with configurable authentication scripts for OAuth2, API key, and session-based auth flows. Scan results are exported as HTML reports with severity-ranked findings, each including specific remediation guidance and code examples. Integration with Jira and GitHub Issues enables automated ticket creation for critical findings. The skill supports baseline scan comparison to track security posture over time.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-api-security-tester/)
