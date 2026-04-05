---
name: "CircleCI Orb Auditor"
description: "Audits CircleCI orb versions and configurations using the CircleCI v2 API. Flags deprecated orbs, provides pinning recommendations, and checks security advisories from the orb registry."
category: "CI/CD Integrations"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/circleci-orb-auditor/"
---
# CircleCI Orb Auditor

Audits CircleCI orb versions and configurations using the CircleCI v2 API. Flags deprecated orbs, provides pinning recommendations, and checks security advisories from the orb registry.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-auditor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-auditor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-auditor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-auditor -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-auditor
```

## Details

The CircleCI Orb Auditor agent performs comprehensive audits of CircleCI orb usage across your organization’s projects. Using the CircleCI v2 API, it scans all .circleci/config.yml files to inventory orb dependencies and validate them against the CircleCI Orb Registry.

The auditor checks each orb reference for version pinning best practices, identifying orbs using volatile tags like @volatile or unpinned major versions that could introduce breaking changes. It queries the Orb Registry API to detect deprecated orbs and suggest official replacements, and cross-references orb versions against known security advisories published in the registry.

For each project, the agent generates a dependency report showing orb versions, update availability, and risk scores based on factors like maintenance activity, download counts, and certification status. It can automatically create pull requests to update orb versions with appropriate changelog summaries. The auditor also validates orb parameter usage against published schemas, catching misconfiguration before pipeline execution.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-auditor/)
