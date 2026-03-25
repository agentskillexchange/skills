---
name: "Snyk Dependency Audit Skill"
description: "Uses the Snyk CLI and REST API v1 to scan package manifests for known CVEs. Cross-references findings with the GitHub Advisory Database and produces SBOM documents in CycloneDX format."
category: "Security & Verification"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/snyk-dependency-audit-skill/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "snyk"  # from ase_tool_match
  github_stars: 5457  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 601684  # from ase_npm_downloads
  github_repo: "snyk/cli"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Snyk Dependency Audit Skill

Uses the Snyk CLI and REST API v1 to scan package manifests for known CVEs. Cross-references findings with the GitHub Advisory Database and produces SBOM documents in CycloneDX format.

## Overview

The Snyk Dependency Audit Skill automates software composition analysis by integrating the Snyk CLI (snyk test, snyk monitor) with AI agent pipelines. It parses package-lock.json, requirements.txt, go.sum, and Gemfile.lock to identify transitive dependency chains with known vulnerabilities.

Each finding is enriched with exploit maturity data from the Snyk Vulnerability Database API and cross-referenced against the GitHub Advisory Database (GHSA) via the GraphQL API. The skill calculates effective EPSS scores to prioritize remediation efforts based on real-world exploitation probability.

Output includes CycloneDX 1.5 SBOM documents and VEX (Vulnerability Exploitability eXchange) statements. The skill supports automated PR generation using the Snyk Fix API, proposing minimal version bumps that resolve vulnerabilities without breaking semver constraints. Integration with Slack Incoming Webhooks provides team notifications for newly disclosed zero-day vulnerabilities affecting monitored repositories.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill snyk-dependency-audit-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill snyk-dependency-audit-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill snyk-dependency-audit-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill snyk-dependency-audit-skill -a codex
```

### OpenClaw

```bash
clawhub install snyk-dependency-audit-skill
```

## Source

- Marketplace: https://agentskillexchange.com/skills/snyk-dependency-audit-skill/
