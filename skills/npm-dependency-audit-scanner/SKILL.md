---
title: "npm Dependency Audit Scanner"
description: "The npm Dependency Audit Scanner skill performs comprehensive security analysis of Node.js project dependencies using multiple vulnerability databases and software composition analysis techniques. It runs npm audit &#8211;json for initial vulnerability detection and enriches findings with data from the OSV.dev API at https://api.osv.dev/v1/query. The skill resolves the complete dependency tree from package-lock.json and cross-references each package version against the NVD API v2.0 at https://services.nvd.nist.gov/rest/json/cves/2.0 for CVE details including CVSS v3.1 severity scores, exploit availability, and patch information. It also queries the GitHub Advisory Database via the GraphQL API for GitHub-specific security advisories. Capabilities include generating Software Bill of Materials (SBOM) in CycloneDX 1.5 JSON format, identifying transitive dependency vulnerabilities with full dependency chain paths, recommending minimal upgrade paths that fix vulnerabilities without breaking changes using semver analysis, detecting typosquatting packages by comparing against known package name patterns, and scanning for deprecated packages via the npm registry API. The skill produces prioritized remediation reports with fix commands (npm audit fix &#8211;force alternatives), CVSS-based severity ranking, and estimated remediation effort for each vulnerability."
source: "https://agentskillexchange.com/skills/npm-dependency-audit-scanner/"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
---

# npm Dependency Audit Scanner

The npm Dependency Audit Scanner skill performs comprehensive security analysis of Node.js project dependencies using multiple vulnerability databases and software composition analysis techniques. It runs npm audit &#8211;json for initial vulnerability detection and enriches findings with data from the OSV.dev API at https://api.osv.dev/v1/query. The skill resolves the complete dependency tree from package-lock.json and cross-references each package version against the NVD API v2.0 at https://services.nvd.nist.gov/rest/json/cves/2.0 for CVE details including CVSS v3.1 severity scores, exploit availability, and patch information. It also queries the GitHub Advisory Database via the GraphQL API for GitHub-specific security advisories. Capabilities include generating Software Bill of Materials (SBOM) in CycloneDX 1.5 JSON format, identifying transitive dependency vulnerabilities with full dependency chain paths, recommending minimal upgrade paths that fix vulnerabilities without breaking changes using semver analysis, detecting typosquatting packages by comparing against known package name patterns, and scanning for deprecated packages via the npm registry API. The skill produces prioritized remediation reports with fix commands (npm audit fix &#8211;force alternatives), CVSS-based severity ranking, and estimated remediation effort for each vulnerability.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-dependency-audit-scanner/)
