---
title: "NPM Package Audit Analyzer"
description: "The NPM Package Audit Analyzer skill performs deep security analysis of Node.js project dependencies beyond standard npm audit output. It queries the npm Registry API at registry.npmjs.org for package metadata and the GitHub Advisory Database via the GraphQL securityAdvisories endpoint for comprehensive vulnerability data. The analysis begins with npm audit &#8211;json to capture the baseline vulnerability report, then enriches each advisory with detailed information from the GitHub Advisory Database including CVSS v3.1 vector strings, CWE classifications, and patch availability timelines. The skill computes actual exploitability scores by analyzing whether vulnerable code paths are reachable from the project entry points using a simplified call graph analysis. Upgrade path computation uses the npm Registry API semver data to find the minimum version bump that resolves each vulnerability, accounting for peer dependency constraints and breaking change indicators. The skill generates a prioritized remediation plan ordering fixes by CVSS score times reachability confidence, with exact npm install commands and links to changelogs. It also tracks advisory publication dates to identify zero-day windows where the project was exposed before a fix was available."
source: "https://agentskillexchange.com/skills/npm-package-audit-analyzer/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Agents"
---

# NPM Package Audit Analyzer

The NPM Package Audit Analyzer skill performs deep security analysis of Node.js project dependencies beyond standard npm audit output. It queries the npm Registry API at registry.npmjs.org for package metadata and the GitHub Advisory Database via the GraphQL securityAdvisories endpoint for comprehensive vulnerability data. The analysis begins with npm audit &#8211;json to capture the baseline vulnerability report, then enriches each advisory with detailed information from the GitHub Advisory Database including CVSS v3.1 vector strings, CWE classifications, and patch availability timelines. The skill computes actual exploitability scores by analyzing whether vulnerable code paths are reachable from the project entry points using a simplified call graph analysis. Upgrade path computation uses the npm Registry API semver data to find the minimum version bump that resolves each vulnerability, accounting for peer dependency constraints and breaking change indicators. The skill generates a prioritized remediation plan ordering fixes by CVSS score times reachability confidence, with exact npm install commands and links to changelogs. It also tracks advisory publication dates to identify zero-day windows where the project was exposed before a fix was available.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-audit-analyzer/)
