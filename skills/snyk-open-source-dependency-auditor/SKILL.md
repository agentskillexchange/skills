---
name: Snyk Open Source Dependency Auditor
description: Performs deep dependency analysis using the Snyk CLI and REST API to
  detect vulnerable transitive packages. Generates fix PRs with version pinning and
  patch recommendations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/snyk-open-source-dependency-auditor/
category:
- Security &amp; Verification
framework:
- Cursor
---
# Snyk Open Source Dependency Auditor

The Snyk Open Source Dependency Auditor uses the Snyk CLI test command and Snyk REST API to perform comprehensive software composition analysis across project dependency trees. It resolves full transitive dependency graphs for npm (package-lock.json), Python (Pipfile.lock, requirements.txt), Go (go.sum), and Maven (pom.xml) projects. Each vulnerability is matched against the Snyk Vulnerability Database with enriched context including exploit maturity, social trending, and reachability analysis that determines if vulnerable code paths are actually invoked. The skill generates automated fix recommendations—either version upgrades to patched releases or Snyk-maintained patches for cases where upgrades would cause breaking changes. It can create GitHub pull requests with precise version bumps, updated lock files, and detailed changelogs explaining what each upgrade addresses. License compliance checking identifies AGPL, GPL, and other copyleft dependencies that may conflict with commercial software distribution.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-open-source-dependency-auditor/)
