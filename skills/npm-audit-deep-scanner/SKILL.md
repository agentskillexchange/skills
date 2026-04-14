---
title: "NPM Audit Deep Scanner"
description: "Extends npm audit with deep transitive dependency analysis using the npm Registry API. Generates fix PRs via GitHub API and cross-checks advisories against the OSV.dev vulnerability database."
verification: security_reviewed
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-audit-deep-scanner/)
