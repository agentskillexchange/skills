---
title: "OWASP ZAP Scanner Agent"
description: "Integrates the OWASP ZAP API to run automated DAST scans against web applications. Parses ZAP JSON reports, triages alerts by CVSS severity, and generates remediation tickets via Jira REST API."
verification: "security_reviewed"
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
  license: "Apache-2.0"
---

# OWASP ZAP Scanner Agent

The OWASP ZAP Scanner Agent provides a fully automated dynamic application security testing (DAST) pipeline for AI agent workflows. It connects to the OWASP ZAP daemon via its REST API on port 8080, configuring spider and active scan policies programmatically.

The agent initiates authenticated scans using ZAP context files, supporting form-based and token-based authentication schemes. During scanning, it monitors progress through the ZAP /JSON/ascan/view/status endpoint and streams real-time alert data.

Post-scan processing parses the ZAP JSON report format, enriching each finding with CVSS 3.1 base scores from the NVD API. Alerts are deduplicated against previous scan baselines stored in SQLite. Critical and high-severity findings automatically create Jira tickets via the Jira Cloud REST API v3, including reproduction steps and suggested code fixes. The agent also generates SARIF output compatible with GitHub Advanced Security code scanning.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-scanner-agent/)
