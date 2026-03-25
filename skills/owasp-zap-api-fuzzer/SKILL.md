---
name: "OWASP ZAP API Fuzzer"
description: "Automates REST API security testing using the OWASP ZAP Python SDK. Runs active scans, SQL injection probes, and XSS tests against OpenAPI specs with structured vulnerability reports."
category: "Security & Verification"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/owasp-zap-api-fuzzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "owasp"  # from ase_tool_match
  github_stars: 14900  # from ase_github_stars (integer, not string)
  github_repo: "zaproxy/zaproxy"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OWASP ZAP API Fuzzer

Automates REST API security testing using the OWASP ZAP Python SDK. Runs active scans, SQL injection probes, and XSS tests against OpenAPI specs with structured vulnerability reports.

## Overview

Automates REST API security testing using the OWASP ZAP Python SDK. Runs active scans, SQL injection probes, and XSS tests against OpenAPI specs with structured vulnerability reports.

This skill provides automated tooling for owasp zap api fuzzer workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-fuzzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-fuzzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-fuzzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-api-fuzzer -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-api-fuzzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/owasp-zap-api-fuzzer/
