---
name: "CircleCI Orb Dependency Scanner"
description: "Scans CircleCI config.yml for outdated orb versions using the CircleCI Orbs Registry API. Reports CVEs linked to orb dependencies via Snyk vulnerability database lookups."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-orb-dependency-scanner-4/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Orb Dependency Scanner

Scans CircleCI config.yml for outdated orb versions using the CircleCI Orbs Registry API. Reports CVEs linked to orb dependencies via Snyk vulnerability database lookups.

## Overview

The CircleCI Orb Dependency Scanner skill provides automated security and freshness auditing for CircleCI pipeline configurations. It parses your config.yml to extract all orb references and queries the CircleCI Orbs Registry API to check for newer versions and deprecation notices.

For each orb dependency, the skill cross-references known vulnerabilities using the Snyk REST API vulnerability database. It generates a detailed report showing which orbs have pending updates, which contain known CVEs, and the severity ratings from the National Vulnerability Database.

The skill supports both public and private orbs, authenticating via CircleCI personal API tokens. It can be configured to run on schedule and produce SARIF-format output compatible with GitHub Advanced Security code scanning.

Additional features include automatic pull request creation for safe orb version bumps using the CircleCI API v2 pipeline trigger endpoint. The skill maintains a local cache of orb metadata to minimize API calls during repeated scans.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-scanner-4
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-scanner-4 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-scanner-4 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-scanner-4 -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-dependency-scanner-4
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-orb-dependency-scanner-4/
