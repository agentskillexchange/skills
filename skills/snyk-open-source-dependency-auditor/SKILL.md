---
title: "Snyk Open Source Dependency Auditor"
description: "Performs deep dependency analysis using the Snyk CLI and REST API to detect vulnerable transitive packages. Generates fix PRs with version pinning and patch recommendations."
verification: "security_reviewed"
source: "https://github.com/snyk/cli"
category:
  - "Security & Verification"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "snyk/cli"
  github_stars: 5496
---

# Snyk Open Source Dependency Auditor

The Snyk Open Source Dependency Auditor uses the Snyk CLI test command and Snyk REST API to perform comprehensive software composition analysis across project dependency trees. It resolves full transitive dependency graphs for npm (package-lock.json), Python (Pipfile.lock, requirements.txt), Go (go.sum), and Maven (pom.xml) projects. Each vulnerability is matched against the Snyk Vulnerability Database with enriched context including exploit maturity, social trending, and reachability analysis that determines if vulnerable code paths are actually invoked. The skill generates automated fix recommendations—either version upgrades to patched releases or Snyk-maintained patches for cases where upgrades would cause breaking changes. It can create GitHub pull requests with precise version bumps, updated lock files, and detailed changelogs explaining what each upgrade addresses. License compliance checking identifies AGPL, GPL, and other copyleft dependencies that may conflict with commercial software distribution.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-open-source-dependency-auditor/)
