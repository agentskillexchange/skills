---
title: "Package Vulnerability Scanner"
description: "Scans npm, PyPI, and Go module dependencies for known vulnerabilities using the OSV.dev API and GitHub Advisory Database. Generates SBOM reports in CycloneDX format."
slug: "package-vuln-scanner-osv-api"
category:
  - "Developer Tools"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/"
---

# Package Vulnerability Scanner

Scans npm, PyPI, and Go module dependencies for known vulnerabilities using the OSV.dev API and GitHub Advisory Database. Generates SBOM reports in CycloneDX format.

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
clawhub install package-vuln-scanner-osv-api
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Package Vulnerability Scanner queries the OSV.dev API and GitHub Advisory Database to identify known vulnerabilities in project dependencies across npm, PyPI, and Go modules. It parses lockfiles directly (package-lock.json, poetry.lock, go.sum) to build accurate dependency trees including transitive dependencies. The scanner correlates findings with CVSS v3.1 scores, EPSS exploit probability data, and KEV catalog entries to prioritize remediation. It generates Software Bill of Materials reports in CycloneDX 1.5 and SPDX 2.3 formats for compliance requirements. Configurable policies allow suppressing known false positives via .vulnscan-ignore.yml files. The tool integrates with Dependabot and Renovate configurations to suggest automated fix PRs. Batch scanning supports monorepo workspaces with per-package result aggregation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/)
