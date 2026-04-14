---
title: "npm Dependency Audit Scanner"
description: "Scans Node.js projects for vulnerable dependencies using npm audit and the OSV.dev REST API. Cross-references CVE databases via the National Vulnerability Database API v2.0 and generates SBOM documents in CycloneDX format."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-dependency-audit-scanner/"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
---

# npm Dependency Audit Scanner

The npm Dependency Audit Scanner skill performs comprehensive security analysis of Node.js project dependencies using multiple vulnerability databases and software composition analysis techniques. It runs npm audit –json for initial vulnerability detection and enriches findings with data from the OSV.dev API at https://api.osv.dev/v1/query.

The skill resolves the complete dependency tree from package-lock.json and cross-references each package version against the NVD API v2.0 at https://services.nvd.nist.gov/rest/json/cves/2.0 for CVE details including CVSS v3.1 severity scores, exploit availability, and patch information. It also queries the GitHub Advisory Database via the GraphQL API for GitHub-specific security advisories.

Capabilities include generating Software Bill of Materials (SBOM) in CycloneDX 1.5 JSON format, identifying transitive dependency vulnerabilities with full dependency chain paths, recommending minimal upgrade paths that fix vulnerabilities without breaking changes using semver analysis, detecting typosquatting packages by comparing against known package name patterns, and scanning for deprecated packages via the npm registry API. The skill produces prioritized remediation reports with fix commands (npm audit fix –force alternatives), CVSS-based severity ranking, and estimated remediation effort for each vulnerability.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-dependency-audit-scanner/)
