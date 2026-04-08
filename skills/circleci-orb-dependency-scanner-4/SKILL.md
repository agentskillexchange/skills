---
title: CircleCI Orb Dependency Scanner
description: The CircleCI Orb Dependency Scanner skill provides automated security
  and freshness auditing for CircleCI pipeline configurations. It parses your config.yml
  to extract all orb references and queries the CircleCI Orbs Registry API to check
  for newer versions and deprecation notices. For each orb dependency, the skill cross-references
  known vulnerabilities using the Snyk REST API vulnerability database. It generates
  a detailed report showing which orbs have pending updates, which contain known CVEs,
  and the severity ratings from the National Vulnerability Database. The skill supports
  both public and private orbs, authenticating via CircleCI personal API tokens. It
  can be configured to run on schedule and produce SARIF-format output compatible
  with GitHub Advanced Security code scanning. Additional features include automatic
  pull request creation for safe orb version bumps using the CircleCI API v2 pipeline
  trigger endpoint. The skill maintains a local cache of orb metadata to minimize
  API calls during repeated scans.
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-orb-dependency-scanner-4/
category:
- CI/CD Integrations
framework:
- Claude Code
---

# CircleCI Orb Dependency Scanner

The CircleCI Orb Dependency Scanner skill provides automated security and freshness auditing for CircleCI pipeline configurations. It parses your config.yml to extract all orb references and queries the CircleCI Orbs Registry API to check for newer versions and deprecation notices. For each orb dependency, the skill cross-references known vulnerabilities using the Snyk REST API vulnerability database. It generates a detailed report showing which orbs have pending updates, which contain known CVEs, and the severity ratings from the National Vulnerability Database. The skill supports both public and private orbs, authenticating via CircleCI personal API tokens. It can be configured to run on schedule and produce SARIF-format output compatible with GitHub Advanced Security code scanning. Additional features include automatic pull request creation for safe orb version bumps using the CircleCI API v2 pipeline trigger endpoint. The skill maintains a local cache of orb metadata to minimize API calls during repeated scans.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-scanner-4/)
