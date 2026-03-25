---
name: "OWASP ZAP API Security Tester"
description: "Runs automated DAST scans against REST and GraphQL APIs using OWASP ZAP daemon API. Detects injection flaws, broken auth, and CORS misconfigurations with detailed remediation steps."
category: "Security & Verification"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/owasp-zap-api-security-tester/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "owasp"  # from ase_tool_match
  github_stars: 14900  # from ase_github_stars (integer, not string)
  github_repo: "zaproxy/zaproxy"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OWASP ZAP API Security Tester

Runs automated DAST scans against REST and GraphQL APIs using OWASP ZAP daemon API. Detects injection flaws, broken auth, and CORS misconfigurations with detailed remediation steps.

## Overview

The OWASP ZAP API Security Tester automates Dynamic Application Security Testing (DAST) for web APIs using the OWASP ZAP proxy daemon and its REST API. It supports both traditional REST endpoints and GraphQL schemas for comprehensive API surface coverage.

The skill connects to ZAP via its JSON API on port 8080, configuring scan policies for OWASP Top 10 categories including SQL injection, XSS, broken authentication, and security misconfiguration. GraphQL introspection queries are used to enumerate all available queries and mutations for targeted fuzzing.

Active scanning modules test for parameter tampering, IDOR vulnerabilities, JWT token weaknesses, and CORS policy misconfigurations. The agent supports both authenticated and unauthenticated scanning modes with configurable authentication scripts for OAuth2, API key, and session-based auth flows.

Scan results are exported as HTML reports with severity-ranked findings, each including specific remediation guidance and code examples. Integration with Jira and GitHub Issues enables automated ticket creation for critical findings. The skill supports baseline scan comparison to track security posture over time.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-security-tester
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-security-tester -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-security-tester -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-security-tester -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-api-security-tester
```

## Source

- Marketplace: https://agentskillexchange.com/skills/owasp-zap-api-security-tester/
