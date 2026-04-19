---
title: "CircleCI Orb Dependency Scanner"
description: "The CircleCI Orb Dependency Scanner skill provides automated security and freshness auditing for CircleCI pipeline configurations. It parses your config.yml to extract all orb references and queries the CircleCI Orbs Registry API to check for newer versions and deprecation notices. For each orb dependency, the skill cross-references known vulnerabilities using the Snyk REST API vulnerability database. It generates a detailed report showing which orbs have pending updates, which contain known CVEs, and the severity ratings from the National Vulnerability Database. The skill supports both public and private orbs, authenticating via CircleCI personal API tokens. It can be configured to run on schedule and produce SARIF-format output compatible with GitHub Advanced Security code scanning. Additional features include automatic pull request creation for safe orb version bumps using the CircleCI API v2 pipeline trigger endpoint. The skill maintains a local cache of orb metadata to minimize API calls during repeated scans."
source: "https://github.com/circleci/circleci-docs"
verification: "security_reviewed"
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

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-scanner-4/)
