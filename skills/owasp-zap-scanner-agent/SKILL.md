---
name: "OWASP ZAP Scanner Agent"
description: "Integrates the OWASP ZAP API to run automated DAST scans against web applications. Parses ZAP JSON reports, triages alerts by CVSS severity, and generates remediation tickets via Jira REST API."
category: "Security & Verification"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/owasp-zap-scanner-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "owasp"  # from ase_tool_match
  github_stars: 14896  # from ase_github_stars (integer, not string)
  github_repo: "zaproxy/zaproxy"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OWASP ZAP Scanner Agent

Integrates the OWASP ZAP API to run automated DAST scans against web applications. Parses ZAP JSON reports, triages alerts by CVSS severity, and generates remediation tickets via Jira REST API.

## Overview

The OWASP ZAP Scanner Agent provides a fully automated dynamic application security testing (DAST) pipeline for AI agent workflows. It connects to the OWASP ZAP daemon via its REST API on port 8080, configuring spider and active scan policies programmatically.

The agent initiates authenticated scans using ZAP context files, supporting form-based and token-based authentication schemes. During scanning, it monitors progress through the ZAP /JSON/ascan/view/status endpoint and streams real-time alert data.

Post-scan processing parses the ZAP JSON report format, enriching each finding with CVSS 3.1 base scores from the NVD API. Alerts are deduplicated against previous scan baselines stored in SQLite. Critical and high-severity findings automatically create Jira tickets via the Jira Cloud REST API v3, including reproduction steps and suggested code fixes. The agent also generates SARIF output compatible with GitHub Advanced Security code scanning.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scanner-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scanner-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scanner-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scanner-agent -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-scanner-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/owasp-zap-scanner-agent/
