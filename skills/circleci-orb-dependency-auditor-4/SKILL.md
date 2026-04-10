---
name: CircleCI Orb Dependency Auditor
description: Audits CircleCI orb dependencies using the CircleCI v2 API and orb registry.
  Detects outdated orb versions, deprecated commands, and known CVEs in orb executor
  images via Trivy scanning.
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-orb-dependency-auditor-4/
category:
- CI/CD Integrations
framework:
- MCP
---
# CircleCI Orb Dependency Auditor

The CircleCI Orb Dependency Auditor skill performs comprehensive security and version auditing of CircleCI orb dependencies in .circleci/config.yml files. It queries the CircleCI v2 API (/api/v2/orb) and the public orb registry to compare pinned versions against latest releases.
For each orb dependency, the auditor checks release notes for breaking changes, deprecated command removals, and security patches. It parses orb source YAML to extract Docker executor image references and submits them to Trivy (aquasec/trivy) for container vulnerability scanning.
The skill generates a dependency report showing version lag, CVE counts by severity (critical/high/medium/low), and upgrade compatibility scores. It can produce automated .circleci/config.yml patches that bump orb versions with appropriate changelog links.
Namespace trust verification checks orb publisher identity against the CircleCI certified/partner program. The auditor flags community orbs lacking recent maintenance (no commits in 6+ months) and suggests certified alternatives from the circleci/ namespace.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-auditor-4/)
