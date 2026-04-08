---
title: npm Dependency Audit Scanner
description: The npm Dependency Audit Scanner skill performs comprehensive security
  analysis of Node.js project dependencies using multiple vulnerability databases
  and software composition analysis techniques. It runs npm audit –json for initial
  vulnerability detection and enriches findings with data from the OSV.dev API at
  https://api.osv.dev/v1/query. The skill resolves the complete dependency tree from
  package-lock.json and cross-references each package version against the NVD API
  v2.0 at https://services.nvd.nist.gov/rest/json/cves/2.0 for CVE details including
  CVSS v3.1 severity scores, exploit availability, and patch information. It also
  queries the GitHub Advisory Database via the GraphQL API for GitHub-specific security
  advisories. Capabilities include generating Software Bill of Materials (SBOM) in
  CycloneDX 1.5 JSON format, identifying transitive dependency vulnerabilities with
  full dependency chain paths, recommending minimal upgrade paths that fix vulnerabilities
  without breaking changes using semver analysis, detecting typosquatting packages
  by comparing against known package name patterns, and scanning for deprecated packages
  via the npm registry API. The skill produces prioritized remediation reports with
  fix commands (npm audit fix –force alternatives), CVSS-based severity ranking, and
  estimated remediation effort for each vulnerability.
verification: security_reviewed
source: https://agentskillexchange.com/skills/npm-dependency-audit-scanner/
category:
- Security &amp; Verification
framework:
- Custom Agents
---

# npm Dependency Audit Scanner

The npm Dependency Audit Scanner skill performs comprehensive security analysis of Node.js project dependencies using multiple vulnerability databases and software composition analysis techniques. It runs npm audit –json for initial vulnerability detection and enriches findings with data from the OSV.dev API at https://api.osv.dev/v1/query. The skill resolves the complete dependency tree from package-lock.json and cross-references each package version against the NVD API v2.0 at https://services.nvd.nist.gov/rest/json/cves/2.0 for CVE details including CVSS v3.1 severity scores, exploit availability, and patch information. It also queries the GitHub Advisory Database via the GraphQL API for GitHub-specific security advisories. Capabilities include generating Software Bill of Materials (SBOM) in CycloneDX 1.5 JSON format, identifying transitive dependency vulnerabilities with full dependency chain paths, recommending minimal upgrade paths that fix vulnerabilities without breaking changes using semver analysis, detecting typosquatting packages by comparing against known package name patterns, and scanning for deprecated packages via the npm registry API. The skill produces prioritized remediation reports with fix commands (npm audit fix –force alternatives), CVSS-based severity ranking, and estimated remediation effort for each vulnerability.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-dependency-audit-scanner/)
