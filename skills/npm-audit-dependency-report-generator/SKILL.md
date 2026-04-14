---
title: "npm Audit Dependency Report Generator"
description: "Generates comprehensive vulnerability reports from npm audit JSON output and the OSV (Open Source Vulnerabilities) API. Parses npm audit –json results, enriches each CVE with CVSS scores from the NVD REST API, and groups findings by severity. Produces SARIF output compatible with GitHub Advanced Security."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-audit-dependency-report-generator/"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
---

# npm Audit Dependency Report Generator

This skill processes npm audit output to produce enriched vulnerability reports for JavaScript and TypeScript projects. It parses the JSON output from npm audit –json, then cross-references each vulnerability identifier with the OSV API at https://api.osv.dev/v1/query and the NVD REST API at https://services.nvd.nist.gov/rest/json/cves/2.0 for CVSS base scores and vector strings. Findings are grouped by severity (Critical, High, Medium, Low) and include affected package versions, patched versions, and dependency paths. The skill generates SARIF 2.1 output compatible with GitHub Advanced Security code scanning and supports uploading results to GitHub via the code-scanning/sarifs API endpoint. It also integrates with Jira to create tickets for Critical and High findings using the Jira REST API v3.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-audit-dependency-report-generator/)
