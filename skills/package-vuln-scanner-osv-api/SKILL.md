---
title: "Package Vulnerability Scanner"
description: "Package Vulnerability Scanner queries the OSV.dev API and GitHub Advisory Database to identify known vulnerabilities in project dependencies across npm, PyPI, and Go modules. It parses lockfiles directly (package-lock.json, poetry.lock, go.sum) to build accurate dependency trees including transitive dependencies. The scanner correlates findings with CVSS v3.1 scores, EPSS exploit probability data, and KEV catalog entries to prioritize remediation. It generates Software Bill of Materials reports in CycloneDX 1.5 and SPDX 2.3 formats for compliance requirements. Configurable policies allow suppressing known false positives via .vulnscan-ignore.yml files. The tool integrates with Dependabot and Renovate configurations to suggest automated fix PRs. Batch scanning supports monorepo workspaces with per-package result aggregation."
source: "https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Codex"
---

# Package Vulnerability Scanner

Package Vulnerability Scanner queries the OSV.dev API and GitHub Advisory Database to identify known vulnerabilities in project dependencies across npm, PyPI, and Go modules. It parses lockfiles directly (package-lock.json, poetry.lock, go.sum) to build accurate dependency trees including transitive dependencies. The scanner correlates findings with CVSS v3.1 scores, EPSS exploit probability data, and KEV catalog entries to prioritize remediation. It generates Software Bill of Materials reports in CycloneDX 1.5 and SPDX 2.3 formats for compliance requirements. Configurable policies allow suppressing known false positives via .vulnscan-ignore.yml files. The tool integrates with Dependabot and Renovate configurations to suggest automated fix PRs. Batch scanning supports monorepo workspaces with per-package result aggregation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/)
