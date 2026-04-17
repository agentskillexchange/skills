---
title: "CircleCI Orb Auditor"
description: "Audits CircleCI orb versions and configurations using the CircleCI v2 API. Flags deprecated orbs, provides pinning recommendations, and checks security advisories from the orb registry."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Auditor

The CircleCI Orb Auditor agent performs comprehensive audits of CircleCI orb usage across your organization’s projects. Using the CircleCI v2 API, it scans all .circleci/config.yml files to inventory orb dependencies and validate them against the CircleCI Orb Registry.

The auditor checks each orb reference for version pinning best practices, identifying orbs using volatile tags like @volatile or unpinned major versions that could introduce breaking changes. It queries the Orb Registry API to detect deprecated orbs and suggest official replacements, and cross-references orb versions against known security advisories published in the registry.

For each project, the agent generates a dependency report showing orb versions, update availability, and risk scores based on factors like maintenance activity, download counts, and certification status. It can automatically create pull requests to update orb versions with appropriate changelog summaries. The auditor also validates orb parameter usage against published schemas, catching misconfiguration before pipeline execution.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-orb-auditor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/circleci-orb-auditor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-auditor/)
