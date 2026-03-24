---
name: "OWASP ZAP Scan Orchestrator"
description: "Orchestrates OWASP ZAP active and passive scans via the ZAP API, automating spider crawls, AJAX spidering with Selenium, and generating SARIF-format vulnerability reports."
category: "Security & Verification"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/owasp-zap-scan-orchestrator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "owasp"  # from ase_tool_match
  github_stars: 14896  # from ase_github_stars (integer, not string)
  github_repo: "zaproxy/zaproxy"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OWASP ZAP Scan Orchestrator

Orchestrates OWASP ZAP active and passive scans via the ZAP API, automating spider crawls, AJAX spidering with Selenium, and generating SARIF-format vulnerability reports.

## Overview

The OWASP ZAP Scan Orchestrator automates comprehensive web application security testing through the ZAP REST API. It configures and launches spider crawls for URL discovery, AJAX spider sessions using Selenium WebDriver for JavaScript-heavy applications, and active scan policies targeting OWASP Top 10 vulnerabilities. The agent manages ZAP contexts for authentication handling including form-based, token-based, and OAuth2 flows. It processes scan results through custom alert filters, maps findings to CWE identifiers, and generates reports in SARIF format for GitHub Security tab integration. The orchestrator supports baseline, full, and API scan types with configurable scan policies, handles session management for authenticated scanning, and integrates with CI/CD pipelines through Docker-based ZAP instances. Includes automatic false positive suppression based on historical scan data.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scan-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scan-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scan-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scan-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-scan-orchestrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/owasp-zap-scan-orchestrator/
