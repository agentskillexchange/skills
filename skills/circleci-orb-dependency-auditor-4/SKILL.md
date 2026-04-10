---
title: "CircleCI Orb Dependency Auditor"
description: "Audits CircleCI orb dependencies using the CircleCI v2 API and orb registry. Detects outdated orb versions, deprecated commands, and known CVEs in orb executor images via Trivy scanning."
slug: "circleci-orb-dependency-auditor-4"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-orb-dependency-auditor-4/"
---

# CircleCI Orb Dependency Auditor

Audits CircleCI orb dependencies using the CircleCI v2 API and orb registry. Detects outdated orb versions, deprecated commands, and known CVEs in orb executor images via Trivy scanning.

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
clawhub install circleci-orb-dependency-auditor-4
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Orb Dependency Auditor skill performs comprehensive security and version auditing of CircleCI orb dependencies in .circleci/config.yml files. It queries the CircleCI v2 API (/api/v2/orb) and the public orb registry to compare pinned versions against latest releases.
For each orb dependency, the auditor checks release notes for breaking changes, deprecated command removals, and security patches. It parses orb source YAML to extract Docker executor image references and submits them to Trivy (aquasec/trivy) for container vulnerability scanning.
The skill generates a dependency report showing version lag, CVE counts by severity (critical/high/medium/low), and upgrade compatibility scores. It can produce automated .circleci/config.yml patches that bump orb versions with appropriate changelog links.
Namespace trust verification checks orb publisher identity against the CircleCI certified/partner program. The auditor flags community orbs lacking recent maintenance (no commits in 6+ months) and suggests certified alternatives from the circleci/ namespace.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-auditor-4/)
