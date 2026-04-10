---
title: "OWASP ZAP API Security Tester"
description: "Runs automated DAST scans against REST and GraphQL APIs using OWASP ZAP daemon API. Detects injection flaws, broken auth, and CORS misconfigurations with detailed remediation steps."
slug: "owasp-zap-api-security-tester"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/owasp-zap-api-security-tester/"
---

# OWASP ZAP API Security Tester

Runs automated DAST scans against REST and GraphQL APIs using OWASP ZAP daemon API. Detects injection flaws, broken auth, and CORS misconfigurations with detailed remediation steps.

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
clawhub install owasp-zap-api-security-tester
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The OWASP ZAP API Security Tester automates Dynamic Application Security Testing (DAST) for web APIs using the OWASP ZAP proxy daemon and its REST API. It supports both traditional REST endpoints and GraphQL schemas for comprehensive API surface coverage.
The skill connects to ZAP via its JSON API on port 8080, configuring scan policies for OWASP Top 10 categories including SQL injection, XSS, broken authentication, and security misconfiguration. GraphQL introspection queries are used to enumerate all available queries and mutations for targeted fuzzing.
Active scanning modules test for parameter tampering, IDOR vulnerabilities, JWT token weaknesses, and CORS policy misconfigurations. The agent supports both authenticated and unauthenticated scanning modes with configurable authentication scripts for OAuth2, API key, and session-based auth flows.
Scan results are exported as HTML reports with severity-ranked findings, each including specific remediation guidance and code examples. Integration with Jira and GitHub Issues enables automated ticket creation for critical findings. The skill supports baseline scan comparison to track security posture over time.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-api-security-tester/)
