---
title: "CircleCI Orb Dependency Auditor"
description: "Audits CircleCI orb dependencies using the CircleCI v2 API and orb registry. Detects outdated orb versions, deprecated commands, and known CVEs in orb executor images via Trivy scanning."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-auditor-4/)
