---
name: "OWASP ZAP Scanner Agent"
description: "Integrates the OWASP ZAP API to run automated DAST scans against web applications. Parses ZAP JSON reports, triages alerts by CVSS severity, and generates remediation tickets via Jira REST API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/owasp-zap-scanner-agent/"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
---

# OWASP ZAP Scanner Agent

The OWASP ZAP Scanner Agent provides a fully automated dynamic application security testing (DAST) pipeline for AI agent workflows. It connects to the OWASP ZAP daemon via its REST API on port 8080, configuring spider and active scan policies programmatically.
The agent initiates authenticated scans using ZAP context files, supporting form-based and token-based authentication schemes. During scanning, it monitors progress through the ZAP /JSON/ascan/view/status endpoint and streams real-time alert data.
Post-scan processing parses the ZAP JSON report format, enriching each finding with CVSS 3.1 base scores from the NVD API. Alerts are deduplicated against previous scan baselines stored in SQLite. Critical and high-severity findings automatically create Jira tickets via the Jira Cloud REST API v3, including reproduction steps and suggested code fixes. The agent also generates SARIF output compatible with GitHub Advanced Security code scanning.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-scanner-agent/)
