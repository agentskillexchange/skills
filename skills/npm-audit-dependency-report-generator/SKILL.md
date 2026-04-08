---
title: npm Audit Dependency Report Generator
description: This skill processes npm audit output to produce enriched vulnerability
  reports for JavaScript and TypeScript projects. It parses the JSON output from npm
  audit –json, then cross-references each vulnerability identifier with the OSV API
  at https://api.osv.dev/v1/query and the NVD REST API at https://services.nvd.nist.gov/rest/json/cves/2.0
  for CVSS base scores and vector strings. Findings are grouped by severity (Critical,
  High, Medium, Low) and include affected package versions, patched versions, and
  dependency paths. The skill generates SARIF 2.1 output compatible with GitHub Advanced
  Security code scanning and supports uploading results to GitHub via the code-scanning/sarifs
  API endpoint. It also integrates with Jira to create tickets for Critical and High
  findings using the Jira REST API v3.
verification: security_reviewed
source: https://agentskillexchange.com/skills/npm-audit-dependency-report-generator/
category:
- CI/CD Integrations
framework:
- Claude Agents
---

# npm Audit Dependency Report Generator

This skill processes npm audit output to produce enriched vulnerability reports for JavaScript and TypeScript projects. It parses the JSON output from npm audit –json, then cross-references each vulnerability identifier with the OSV API at https://api.osv.dev/v1/query and the NVD REST API at https://services.nvd.nist.gov/rest/json/cves/2.0 for CVSS base scores and vector strings. Findings are grouped by severity (Critical, High, Medium, Low) and include affected package versions, patched versions, and dependency paths. The skill generates SARIF 2.1 output compatible with GitHub Advanced Security code scanning and supports uploading results to GitHub via the code-scanning/sarifs API endpoint. It also integrates with Jira to create tickets for Critical and High findings using the Jira REST API v3.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-audit-dependency-report-generator/)
