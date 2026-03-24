---
name: "OWASP ZAP Scanner"
description: "Integrates OWASP ZAP (Zed Attack Proxy) for automated web application security scanning. Runs active and passive scans, identifies OWASP Top 10 vulnerabilities, and generates remediation reports for CI/CD pipelines."
category: "Security & Verification"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/owasp-zap-scanner/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "owasp"  # from ase_tool_match
  github_stars: 14896  # from ase_github_stars (integer, not string)
  github_repo: "zaproxy/zaproxy"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OWASP ZAP Scanner

Integrates OWASP ZAP (Zed Attack Proxy) for automated web application security scanning. Runs active and passive scans, identifies OWASP Top 10 vulnerabilities, and generates remediation reports for CI/CD pipelines.

## Overview

Integrates OWASP ZAP (Zed Attack Proxy) for automated web application security scanning. Runs active and passive scans, identifies OWASP Top 10 vulnerabilities, and generates remediation reports for CI/CD pipelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scanner -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-scanner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/owasp-zap-scanner/
