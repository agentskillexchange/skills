---
title: "CircleCI Orb Dependency Auditor"
description: "The CircleCI Orb Dependency Auditor skill performs comprehensive security and version auditing of CircleCI orb dependencies in .circleci/config.yml files. It queries the CircleCI v2 API (/api/v2/orb) and the public orb registry to compare pinned versions against latest releases.\nFor each orb dependency, the auditor checks release notes for breaking changes, deprecated command removals, and security patches. It parses orb source YAML to extract Docker executor image references and submits them to Trivy (aquasec/trivy) for container vulnerability scanning.\nThe skill generates a dependency report showing version lag, CVE counts by severity (critical/high/medium/low), and upgrade compatibility scores. It can produce automated .circleci/config.yml patches that bump orb versions with appropriate changelog links.\nNamespace trust verification checks orb publisher identity against the CircleCI certified/partner program. The auditor flags community orbs lacking recent maintenance (no commits in 6+ months) and suggests certified alternatives from the circleci/ namespace."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Dependency Auditor

The CircleCI Orb Dependency Auditor skill performs comprehensive security and version auditing of CircleCI orb dependencies in .circleci/config.yml files. It queries the CircleCI v2 API (/api/v2/orb) and the public orb registry to compare pinned versions against latest releases.
For each orb dependency, the auditor checks release notes for breaking changes, deprecated command removals, and security patches. It parses orb source YAML to extract Docker executor image references and submits them to Trivy (aquasec/trivy) for container vulnerability scanning.
The skill generates a dependency report showing version lag, CVE counts by severity (critical/high/medium/low), and upgrade compatibility scores. It can produce automated .circleci/config.yml patches that bump orb versions with appropriate changelog links.
Namespace trust verification checks orb publisher identity against the CircleCI certified/partner program. The auditor flags community orbs lacking recent maintenance (no commits in 6+ months) and suggests certified alternatives from the circleci/ namespace.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-orb-dependency-auditor-4
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/circleci-orb-dependency-auditor-4` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-auditor-4/)
