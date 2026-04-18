---
title: "Package Vulnerability Scanner"
description: "Scans npm, PyPI, and Go module dependencies for known vulnerabilities using the OSV.dev API and GitHub Advisory Database. Generates SBOM reports in CycloneDX format."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/"
category:
  - "Developer Tools"
framework:
  - "Codex"
---

# Package Vulnerability Scanner

Package Vulnerability Scanner queries the OSV.dev API and GitHub Advisory Database to identify known vulnerabilities in project dependencies across npm, PyPI, and Go modules. It parses lockfiles directly (package-lock.json, poetry.lock, go.sum) to build accurate dependency trees including transitive dependencies. The scanner correlates findings with CVSS v3.1 scores, EPSS exploit probability data, and KEV catalog entries to prioritize remediation. It generates Software Bill of Materials reports in CycloneDX 1.5 and SPDX 2.3 formats for compliance requirements. Configurable policies allow suppressing known false positives via .vulnscan-ignore.yml files. The tool integrates with Dependabot and Renovate configurations to suggest automated fix PRs. Batch scanning supports monorepo workspaces with per-package result aggregation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/package-vuln-scanner-osv-api
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/package-vuln-scanner-osv-api` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/)
