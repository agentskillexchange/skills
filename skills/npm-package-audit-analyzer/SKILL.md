---
name: "NPM Package Audit Analyzer"
description: "Analyzes npm package security advisories using npm audit, the npm Registry API, and the GitHub Advisory Database GraphQL API. Produces prioritized vulnerability reports with upgrade path recommendations."
category: "Library & API Reference"
framework: "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-package-audit-analyzer/"
tool_ecosystem:
  tool: graphql
  github_stars: 20332
  npm_weekly_downloads: 32010306
  github_repo: graphql/graphql-js
  license: MIT
  maintained: true
---

# NPM Package Audit Analyzer

Analyzes npm package security advisories using npm audit, the npm Registry API, and the GitHub Advisory Database GraphQL API. Produces prioritized vulnerability reports with upgrade path recommendations.

## Overview

The NPM Package Audit Analyzer skill performs deep security analysis of Node.js project dependencies beyond standard npm audit output. It queries the npm Registry API at registry.npmjs.org for package metadata and the GitHub Advisory Database via the GraphQL securityAdvisories endpoint for comprehensive vulnerability data.

The analysis begins with npm audit –json to capture the baseline vulnerability report, then enriches each advisory with detailed information from the GitHub Advisory Database including CVSS v3.1 vector strings, CWE classifications, and patch availability timelines. The skill computes actual exploitability scores by analyzing whether vulnerable code paths are reachable from the project entry points using a simplified call graph analysis.

Upgrade path computation uses the npm Registry API semver data to find the minimum version bump that resolves each vulnerability, accounting for peer dependency constraints and breaking change indicators. The skill generates a prioritized remediation plan ordering fixes by CVSS score times reachability confidence, with exact npm install commands and links to changelogs. It also tracks advisory publication dates to identify zero-day windows where the project was exposed before a fix was available.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill npm-package-audit-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill npm-package-audit-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill npm-package-audit-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill npm-package-audit-analyzer -a codex
```

### OpenClaw

```bash
clawhub install npm-package-audit-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/npm-package-audit-analyzer/
