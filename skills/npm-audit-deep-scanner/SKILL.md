---
title: "NPM Audit Deep Scanner"
description: "Extends npm audit with deep transitive dependency analysis using the npm Registry API. Generates fix PRs via GitHub API and cross-checks advisories against the OSV.dev vulnerability database."
verification: "security_reviewed"
source: "https://docs.npmjs.com/cli/v10/commands/npm-audit/"
category:
  - "Security & Verification"
framework:
  - "Custom Agents"
---

# NPM Audit Deep Scanner

The NPM Audit Deep Scanner skill provides comprehensive JavaScript supply chain security analysis beyond standard npm audit capabilities. It queries the npm Registry API (registry.npmjs.org) to resolve complete dependency trees, identifying phantom dependencies and version conflicts invisible to standard tooling. The skill performs deep analysis of each package by querying the OSV.dev API (/v1/query) for vulnerability data across multiple ecosystems simultaneously. It identifies not just direct CVEs but also malicious package indicators by checking package metadata patterns against known typosquatting databases and the Socket.dev API for install script analysis. Automated remediation generates pull requests via the GitHub REST API v3, using the Git Trees API to create atomic commits that bump vulnerable dependencies while respecting peer dependency constraints. Each PR includes a detailed impact assessment with breaking change likelihood scores computed from semver analysis and changelog parsing. Integration with the npm diff API provides human-readable code diffs between vulnerable and patched versions for security team review.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/npm-audit-deep-scanner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-audit-deep-scanner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/npm-audit-deep-scanner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-audit-deep-scanner/)
