---
title: OWASP ZAP Scanner Agent
description: The OWASP ZAP Scanner Agent provides a fully automated dynamic application
  security testing (DAST) pipeline for AI agent workflows. It connects to the OWASP
  ZAP daemon via its REST API on port 8080, configuring spider and active scan policies
  programmatically. The agent initiates authenticated scans using ZAP context files,
  supporting form-based and token-based authentication schemes. During scanning, it
  monitors progress through the ZAP /JSON/ascan/view/status endpoint and streams real-time
  alert data. Post-scan processing parses the ZAP JSON report format, enriching each
  finding with CVSS 3.1 base scores from the NVD API. Alerts are deduplicated against
  previous scan baselines stored in SQLite. Critical and high-severity findings automatically
  create Jira tickets via the Jira Cloud REST API v3, including reproduction steps
  and suggested code fixes. The agent also generates SARIF output compatible with
  GitHub Advanced Security code scanning.
verification: security_reviewed
source: https://agentskillexchange.com/skills/owasp-zap-scanner-agent/
category:
- Security &amp; Verification
framework:
- OpenClaw
---

# OWASP ZAP Scanner Agent

The OWASP ZAP Scanner Agent provides a fully automated dynamic application security testing (DAST) pipeline for AI agent workflows. It connects to the OWASP ZAP daemon via its REST API on port 8080, configuring spider and active scan policies programmatically. The agent initiates authenticated scans using ZAP context files, supporting form-based and token-based authentication schemes. During scanning, it monitors progress through the ZAP /JSON/ascan/view/status endpoint and streams real-time alert data. Post-scan processing parses the ZAP JSON report format, enriching each finding with CVSS 3.1 base scores from the NVD API. Alerts are deduplicated against previous scan baselines stored in SQLite. Critical and high-severity findings automatically create Jira tickets via the Jira Cloud REST API v3, including reproduction steps and suggested code fixes. The agent also generates SARIF output compatible with GitHub Advanced Security code scanning.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-scanner-agent/)
