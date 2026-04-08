---
title: Package Vulnerability Scanner
description: Package Vulnerability Scanner queries the OSV.dev API and GitHub Advisory
  Database to identify known vulnerabilities in project dependencies across npm, PyPI,
  and Go modules. It parses lockfiles directly (package-lock.json, poetry.lock, go.sum)
  to build accurate dependency trees including transitive dependencies. The scanner
  correlates findings with CVSS v3.1 scores, EPSS exploit probability data, and KEV
  catalog entries to prioritize remediation. It generates Software Bill of Materials
  reports in CycloneDX 1.5 and SPDX 2.3 formats for compliance requirements. Configurable
  policies allow suppressing known false positives via .vulnscan-ignore.yml files.
  The tool integrates with Dependabot and Renovate configurations to suggest automated
  fix PRs. Batch scanning supports monorepo workspaces with per-package result aggregation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/
category:
- Developer Tools
framework:
- Codex
---

# Package Vulnerability Scanner

Package Vulnerability Scanner queries the OSV.dev API and GitHub Advisory Database to identify known vulnerabilities in project dependencies across npm, PyPI, and Go modules. It parses lockfiles directly (package-lock.json, poetry.lock, go.sum) to build accurate dependency trees including transitive dependencies. The scanner correlates findings with CVSS v3.1 scores, EPSS exploit probability data, and KEV catalog entries to prioritize remediation. It generates Software Bill of Materials reports in CycloneDX 1.5 and SPDX 2.3 formats for compliance requirements. Configurable policies allow suppressing known false positives via .vulnscan-ignore.yml files. The tool integrates with Dependabot and Renovate configurations to suggest automated fix PRs. Batch scanning supports monorepo workspaces with per-package result aggregation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/)
