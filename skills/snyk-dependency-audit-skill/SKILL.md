---
name: Snyk Dependency Audit Skill
description: Uses the Snyk CLI and REST API v1 to scan package manifests for known
  CVEs. Cross-references findings with the GitHub Advisory Database and produces SBOM
  documents in CycloneDX format.
verification: security_reviewed
source: https://agentskillexchange.com/skills/snyk-dependency-audit-skill/
category:
- Security &amp; Verification
framework:
- Claude Code
---
# Snyk Dependency Audit Skill

The Snyk Dependency Audit Skill automates software composition analysis by integrating the Snyk CLI (snyk test, snyk monitor) with AI agent pipelines. It parses package-lock.json, requirements.txt, go.sum, and Gemfile.lock to identify transitive dependency chains with known vulnerabilities.
Each finding is enriched with exploit maturity data from the Snyk Vulnerability Database API and cross-referenced against the GitHub Advisory Database (GHSA) via the GraphQL API. The skill calculates effective EPSS scores to prioritize remediation efforts based on real-world exploitation probability.
Output includes CycloneDX 1.5 SBOM documents and VEX (Vulnerability Exploitability eXchange) statements. The skill supports automated PR generation using the Snyk Fix API, proposing minimal version bumps that resolve vulnerabilities without breaking semver constraints. Integration with Slack Incoming Webhooks provides team notifications for newly disclosed zero-day vulnerabilities affecting monitored repositories.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-dependency-audit-skill/)
