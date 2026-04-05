---
name: "npm Audit Dependency Report Generator"
description: "Generates comprehensive vulnerability reports from npm audit JSON output and the OSV (Open Source Vulnerabilities) API. Parses npm audit –json results, enriches each CVE with CVSS scores from the NVD REST API, and groups findings by severity. Produces SARIF output compatible with GitHub Advanced Security."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-audit-dependency-report-generator/"
---
# npm Audit Dependency Report Generator

Generates comprehensive vulnerability reports from npm audit JSON output and the OSV (Open Source Vulnerabilities) API. Parses npm audit –json results, enriches each CVE with CVSS scores from the NVD REST API, and groups findings by severity. Produces SARIF output compatible with GitHub Advanced Security.

This skill processes npm audit output to produce enriched vulnerability reports for JavaScript and TypeScript projects. It parses the JSON output from npm audit –json, then cross-references each vulnerability identifier with the OSV API at https://api.osv.dev/v1/query and the NVD REST API at https://services.nvd.nist.gov/rest/json/cves/2.0 for CVSS base scores and vector strings. Findings are grouped by severity (Critical, High, Medium, Low) and include affected package versions, patched versions, and dependency paths. The skill generates SARIF 2.1 output compatible with GitHub Advanced Security code scanning and supports uploading results to GitHub via the code-scanning/sarifs API endpoint. It also integrates with Jira to create tickets for Critical and High findings using the Jira REST API v3.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill npm-audit-dependency-report-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill npm-audit-dependency-report-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill npm-audit-dependency-report-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill npm-audit-dependency-report-generator -a codex
```

### OpenClaw

```bash
clawhub install npm-audit-dependency-report-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-audit-dependency-report-generator/)
