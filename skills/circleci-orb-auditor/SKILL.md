---
title: "CircleCI Orb Auditor"
description: "Audits CircleCI orb versions and configurations using the CircleCI v2 API. Flags deprecated orbs, provides pinning recommendations, and checks security advisories from the orb registry."
slug: "circleci-orb-auditor"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-orb-auditor/"
listed: true
---

# CircleCI Orb Auditor

Audits CircleCI orb versions and configurations using the CircleCI v2 API. Flags deprecated orbs, provides pinning recommendations, and checks security advisories from the orb registry.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install circleci-orb-auditor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Orb Auditor agent performs comprehensive audits of CircleCI orb usage across your organization’s projects. Using the CircleCI v2 API, it scans all .circleci/config.yml files to inventory orb dependencies and validate them against the CircleCI Orb Registry.
The auditor checks each orb reference for version pinning best practices, identifying orbs using volatile tags like @volatile or unpinned major versions that could introduce breaking changes. It queries the Orb Registry API to detect deprecated orbs and suggest official replacements, and cross-references orb versions against known security advisories published in the registry.
For each project, the agent generates a dependency report showing orb versions, update availability, and risk scores based on factors like maintenance activity, download counts, and certification status. It can automatically create pull requests to update orb versions with appropriate changelog summaries. The auditor also validates orb parameter usage against published schemas, catching misconfiguration before pipeline execution.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-auditor/)
