---
title: "NPM Audit Deep Scanner"
description: "Extends npm audit with deep transitive dependency analysis using the npm Registry API. Generates fix PRs via GitHub API and cross-checks advisories against the OSV.dev vulnerability database."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-audit-deep-scanner/"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
---

# NPM Audit Deep Scanner

The NPM Audit Deep Scanner skill provides comprehensive JavaScript supply chain security analysis beyond standard npm audit capabilities. It queries the npm Registry API (registry.npmjs.org) to resolve complete dependency trees, identifying phantom dependencies and version conflicts invisible to standard tooling.

The skill performs deep analysis of each package by querying the OSV.dev API (/v1/query) for vulnerability data across multiple ecosystems simultaneously. It identifies not just direct CVEs but also malicious package indicators by checking package metadata patterns against known typosquatting databases and the Socket.dev API for install script analysis.

Automated remediation generates pull requests via the GitHub REST API v3, using the Git Trees API to create atomic commits that bump vulnerable dependencies while respecting peer dependency constraints. Each PR includes a detailed impact assessment with breaking change likelihood scores computed from semver analysis and changelog parsing. Integration with the npm diff API provides human-readable code diffs between vulnerable and patched versions for security team review.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-audit-deep-scanner/)
