---
title: "OWASP ZAP Scanner Agent"
description: "Integrates the OWASP ZAP API to run automated DAST scans against web applications. Parses ZAP JSON reports, triages alerts by CVSS severity, and generates remediation tickets via Jira REST API."
verification: security_reviewed
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
---

# OWASP ZAP Scanner Agent

The OWASP ZAP Scanner Agent provides a fully automated dynamic application security testing (DAST) pipeline for AI agent workflows. It connects to the OWASP ZAP daemon via its REST API on port 8080, configuring spider and active scan policies programmatically.

The agent initiates authenticated scans using ZAP context files, supporting form-based and token-based authentication schemes. During scanning, it monitors progress through the ZAP /JSON/ascan/view/status endpoint and streams real-time alert data.

Post-scan processing parses the ZAP JSON report format, enriching each finding with CVSS 3.1 base scores from the NVD API. Alerts are deduplicated against previous scan baselines stored in SQLite. Critical and high-severity findings automatically create Jira tickets via the Jira Cloud REST API v3, including reproduction steps and suggested code fixes. The agent also generates SARIF output compatible with GitHub Advanced Security code scanning.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-scanner-agent/)
