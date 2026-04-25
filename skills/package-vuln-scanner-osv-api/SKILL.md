---
title: "Package Vulnerability Scanner"
description: "Scans npm, PyPI, and Go module dependencies for known vulnerabilities using the OSV.dev API and GitHub Advisory Database. Generates SBOM reports in CycloneDX format."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/"
category:
  - "Developer Tools"
framework:
  - "Codex"
---

# Package Vulnerability Scanner

Package Vulnerability Scanner queries the OSV.dev API and GitHub Advisory Database to identify known vulnerabilities in project dependencies across npm, PyPI, and Go modules. It parses lockfiles directly (package-lock.json, poetry.lock, go.sum) to build accurate dependency trees including transitive dependencies. The scanner correlates findings with CVSS v3.1 scores, EPSS exploit probability data, and KEV catalog entries to prioritize remediation. It generates Software Bill of Materials reports in CycloneDX 1.5 and SPDX 2.3 formats for compliance requirements. Configurable policies allow suppressing known false positives via .vulnscan-ignore.yml files. The tool integrates with Dependabot and Renovate configurations to suggest automated fix PRs. Batch scanning supports monorepo workspaces with per-package result aggregation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/package-vuln-scanner-osv-api
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/package-vuln-scanner-osv-api`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/)
