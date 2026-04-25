---
title: "CircleCI Orb Dependency Scanner"
description: "Scans CircleCI config.yml for outdated orb versions using the CircleCI Orbs Registry API. Reports CVEs linked to orb dependencies via Snyk vulnerability database lookups."
verification: "security_reviewed"
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Dependency Scanner

The CircleCI Orb Dependency Scanner skill provides automated security and freshness auditing for CircleCI pipeline configurations. It parses your config.yml to extract all orb references and queries the CircleCI Orbs Registry API to check for newer versions and deprecation notices. For each orb dependency, the skill cross-references known vulnerabilities using the Snyk REST API vulnerability database. It generates a detailed report showing which orbs have pending updates, which contain known CVEs, and the severity ratings from the National Vulnerability Database. The skill supports both public and private orbs, authenticating via CircleCI personal API tokens. It can be configured to run on schedule and produce SARIF-format output compatible with GitHub Advanced Security code scanning. Additional features include automatic pull request creation for safe orb version bumps using the CircleCI API v2 pipeline trigger endpoint. The skill maintains a local cache of orb metadata to minimize API calls during repeated scans.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/circleci-orb-dependency-scanner-4/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-orb-dependency-scanner-4
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/circleci-orb-dependency-scanner-4`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-scanner-4/)
