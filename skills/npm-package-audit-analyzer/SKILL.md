---
title: "NPM Package Audit Analyzer"
description: "Analyzes npm package security advisories using npm audit, the npm Registry API, and the GitHub Advisory Database GraphQL API. Produces prioritized vulnerability reports with upgrade path recommendations."
slug: "npm-package-audit-analyzer"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-package-audit-analyzer/"
---

# NPM Package Audit Analyzer

Analyzes npm package security advisories using npm audit, the npm Registry API, and the GitHub Advisory Database GraphQL API. Produces prioritized vulnerability reports with upgrade path recommendations.

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
clawhub install npm-package-audit-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The NPM Package Audit Analyzer skill performs deep security analysis of Node.js project dependencies beyond standard npm audit output. It queries the npm Registry API at registry.npmjs.org for package metadata and the GitHub Advisory Database via the GraphQL securityAdvisories endpoint for comprehensive vulnerability data.
The analysis begins with npm audit –json to capture the baseline vulnerability report, then enriches each advisory with detailed information from the GitHub Advisory Database including CVSS v3.1 vector strings, CWE classifications, and patch availability timelines. The skill computes actual exploitability scores by analyzing whether vulnerable code paths are reachable from the project entry points using a simplified call graph analysis.
Upgrade path computation uses the npm Registry API semver data to find the minimum version bump that resolves each vulnerability, accounting for peer dependency constraints and breaking change indicators. The skill generates a prioritized remediation plan ordering fixes by CVSS score times reachability confidence, with exact npm install commands and links to changelogs. It also tracks advisory publication dates to identify zero-day windows where the project was exposed before a fix was available.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-audit-analyzer/)
