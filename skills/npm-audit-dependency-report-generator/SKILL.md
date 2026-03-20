---
name: npm Audit Dependency Report Generator
description: Generates comprehensive vulnerability reports from npm audit JSON output and the OSV (Open Source Vulnerabilities) API. Parses npm audit –json results, enriches each CVE with CVSS scores from the NVD 
category: CI/CD Integrations
framework: Claude Agents
verification: security_reviewed
rating: 4.9
reviews: 28
source: https://agentskillexchange.com/skill/npm-audit-dependency-report-generator/
---

# npm Audit Dependency Report Generator

Generates comprehensive vulnerability reports from npm audit JSON output and the OSV (Open Source Vulnerabilities) API. Parses npm audit –json results, enriches each CVE with CVSS scores from the NVD REST API, and groups findings by severity. Produces SARIF output compatible with GitHub Advanced Security.

## Overview

This skill processes npm audit output to produce enriched vulnerability reports for JavaScript and TypeScript projects. It parses the JSON output from npm audit –json, then cross-references each vulnerability identifier with the OSV API at https://api.osv.dev/v1/query and the NVD REST API at https://services.nvd.nist.gov/rest/json/cves/2.0 for CVSS base scores and vector strings. Findings are grouped by severity (Critical, High, Medium, Low) and include affected package versions, patched versions, and dependency paths. The skill generates SARIF 2.1 output compatible with GitHub Advanced Security code scanning and supports uploading results to GitHub via the code-scanning/sarifs API endpoint. It also integrates with Jira to create tickets for Critical and High findings using the Jira REST API v3.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill npm-audit-dependency-report-generator
```

### OpenClaw

```bash
openclaw install npm-audit-dependency-report-generator
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | Claude Agents |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (28 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/npm-audit-dependency-report-generator/)*
