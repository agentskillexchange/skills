---
name: "CircleCI Orb Dependency Auditor"
description: "Audits CircleCI orb dependencies using the CircleCI v2 API and orb registry. Detects outdated orb versions, deprecated commands, and known CVEs in orb executor images via Trivy scanning."
category: "CI/CD Integrations"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
tool_ecosystem:
  tool: circleci
  github_stars: 842
  github_repo: circleci/circleci-docs
  maintained: true
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-auditor-4/)
