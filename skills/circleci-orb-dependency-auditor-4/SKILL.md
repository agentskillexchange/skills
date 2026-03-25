---
name: "CircleCI Orb Dependency Auditor"
description: "Audits CircleCI orb dependencies using the CircleCI v2 API and orb registry. Detects outdated orb versions, deprecated commands, and known CVEs in orb executor images via Trivy scanning."
category: "CI/CD Integrations"
framework: "MCP-compatible"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-orb-dependency-auditor-4/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Orb Dependency Auditor

Audits CircleCI orb dependencies using the CircleCI v2 API and orb registry. Detects outdated orb versions, deprecated commands, and known CVEs in orb executor images via Trivy scanning.

## Overview

The CircleCI Orb Dependency Auditor skill performs comprehensive security and version auditing of CircleCI orb dependencies in .circleci/config.yml files. It queries the CircleCI v2 API (/api/v2/orb) and the public orb registry to compare pinned versions against latest releases.

For each orb dependency, the auditor checks release notes for breaking changes, deprecated command removals, and security patches. It parses orb source YAML to extract Docker executor image references and submits them to Trivy (aquasec/trivy) for container vulnerability scanning.

The skill generates a dependency report showing version lag, CVE counts by severity (critical/high/medium/low), and upgrade compatibility scores. It can produce automated .circleci/config.yml patches that bump orb versions with appropriate changelog links.

Namespace trust verification checks orb publisher identity against the CircleCI certified/partner program. The auditor flags community orbs lacking recent maintenance (no commits in 6+ months) and suggests certified alternatives from the circleci/ namespace.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-auditor-4
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-auditor-4 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-auditor-4 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-auditor-4 -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-dependency-auditor-4
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-orb-dependency-auditor-4/
