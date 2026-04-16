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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/package-vuln-scanner-osv-api/)
