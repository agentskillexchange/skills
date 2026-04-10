---
name: "NPM Package Audit Analyzer"
description: "Analyzes npm package security advisories using npm audit, the npm Registry API, and the GitHub Advisory Database GraphQL API. Produces prioritized vulnerability reports with upgrade path recommendations."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-package-audit-analyzer/"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Agents"
---

# NPM Package Audit Analyzer

The NPM Package Audit Analyzer skill performs deep security analysis of Node.js project dependencies beyond standard npm audit output. It queries the npm Registry API at registry.npmjs.org for package metadata and the GitHub Advisory Database via the GraphQL securityAdvisories endpoint for comprehensive vulnerability data.
The analysis begins with npm audit -json to capture the baseline vulnerability report, then enriches each advisory with detailed information from the GitHub Advisory Database including CVSS v3.1 vector strings, CWE classifications, and patch availability timelines. The skill computes actual exploitability scores by analyzing whether vulnerable code paths are reachable from the project entry points using a simplified call graph analysis.
Upgrade path computation uses the npm Registry API semver data to find the minimum version bump that resolves each vulnerability, accounting for peer dependency constraints and breaking change indicators. The skill generates a prioritized remediation plan ordering fixes by CVSS score times reachability confidence, with exact npm install commands and links to changelogs. It also tracks advisory publication dates to identify zero-day windows where the project was exposed before a fix was available.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-audit-analyzer/)
