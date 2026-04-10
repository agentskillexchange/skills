---
title: "npm Audit Dependency Report Generator"
description: "Generates comprehensive vulnerability reports from npm audit JSON output and the OSV (Open Source Vulnerabilities) API. Parses npm audit –json results, enriches each CVE with CVSS scores from the NVD REST API, and groups findings by severity. Produces SARIF output compatible with GitHub Advanced Security."
slug: "npm-audit-dependency-report-generator"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-audit-dependency-report-generator/"
---

# npm Audit Dependency Report Generator

Generates comprehensive vulnerability reports from npm audit JSON output and the OSV (Open Source Vulnerabilities) API. Parses npm audit –json results, enriches each CVE with CVSS scores from the NVD REST API, and groups findings by severity. Produces SARIF output compatible with GitHub Advanced Security.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install npm-audit-dependency-report-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill processes npm audit output to produce enriched vulnerability reports for JavaScript and TypeScript projects. It parses the JSON output from npm audit –json, then cross-references each vulnerability identifier with the OSV API at https://api.osv.dev/v1/query and the NVD REST API at https://services.nvd.nist.gov/rest/json/cves/2.0 for CVSS base scores and vector strings. Findings are grouped by severity (Critical, High, Medium, Low) and include affected package versions, patched versions, and dependency paths. The skill generates SARIF 2.1 output compatible with GitHub Advanced Security code scanning and supports uploading results to GitHub via the code-scanning/sarifs API endpoint. It also integrates with Jira to create tickets for Critical and High findings using the Jira REST API v3.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-audit-dependency-report-generator/)
