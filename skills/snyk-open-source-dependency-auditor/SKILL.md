---
name: "Snyk Open Source Dependency Auditor"
description: "Performs deep dependency analysis using the Snyk CLI and REST API to detect vulnerable transitive packages. Generates fix PRs with version pinning and patch recommendations."
category: "Security & Verification"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/snyk-open-source-dependency-auditor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "snyk"  # from ase_tool_match
  github_stars: 5457  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 601684  # from ase_npm_downloads
  github_repo: "snyk/cli"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Snyk Open Source Dependency Auditor

Performs deep dependency analysis using the Snyk CLI and REST API to detect vulnerable transitive packages. Generates fix PRs with version pinning and patch recommendations.

## Overview

The Snyk Open Source Dependency Auditor uses the Snyk CLI test command and Snyk REST API to perform comprehensive software composition analysis across project dependency trees. It resolves full transitive dependency graphs for npm (package-lock.json), Python (Pipfile.lock, requirements.txt), Go (go.sum), and Maven (pom.xml) projects. Each vulnerability is matched against the Snyk Vulnerability Database with enriched context including exploit maturity, social trending, and reachability analysis that determines if vulnerable code paths are actually invoked. The skill generates automated fix recommendations—either version upgrades to patched releases or Snyk-maintained patches for cases where upgrades would cause breaking changes. It can create GitHub pull requests with precise version bumps, updated lock files, and detailed changelogs explaining what each upgrade addresses. License compliance checking identifies AGPL, GPL, and other copyleft dependencies that may conflict with commercial software distribution.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill snyk-open-source-dependency-auditor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill snyk-open-source-dependency-auditor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill snyk-open-source-dependency-auditor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill snyk-open-source-dependency-auditor -a codex
```

### OpenClaw

```bash
clawhub install snyk-open-source-dependency-auditor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/snyk-open-source-dependency-auditor/
