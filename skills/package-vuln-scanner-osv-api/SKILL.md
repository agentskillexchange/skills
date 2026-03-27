---
name: "Package Vulnerability Scanner"
description: "Scans npm, PyPI, and Go module dependencies for known vulnerabilities using the OSV.dev API and GitHub Advisory Database. Generates SBOM reports in CycloneDX format."
category: "Developer Tools"
framework: "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/"
---

# Package Vulnerability Scanner

Scans npm, PyPI, and Go module dependencies for known vulnerabilities using the OSV.dev API and GitHub Advisory Database. Generates SBOM reports in CycloneDX format.

## Overview

Package Vulnerability Scanner queries the OSV.dev API and GitHub Advisory Database to identify known vulnerabilities in project dependencies across npm, PyPI, and Go modules. It parses lockfiles directly (package-lock.json, poetry.lock, go.sum) to build accurate dependency trees including transitive dependencies. The scanner correlates findings with CVSS v3.1 scores, EPSS exploit probability data, and KEV catalog entries to prioritize remediation. It generates Software Bill of Materials reports in CycloneDX 1.5 and SPDX 2.3 formats for compliance requirements. Configurable policies allow suppressing known false positives via .vulnscan-ignore.yml files. The tool integrates with Dependabot and Renovate configurations to suggest automated fix PRs. Batch scanning supports monorepo workspaces with per-package result aggregation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill package-vuln-scanner-osv-api
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill package-vuln-scanner-osv-api -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill package-vuln-scanner-osv-api -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill package-vuln-scanner-osv-api -a codex
```

### OpenClaw

```bash
clawhub install package-vuln-scanner-osv-api
```

## Source

- Marketplace: https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/
