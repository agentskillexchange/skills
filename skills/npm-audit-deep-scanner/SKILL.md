---
title: NPM Audit Deep Scanner
description: The NPM Audit Deep Scanner skill provides comprehensive JavaScript supply
  chain security analysis beyond standard npm audit capabilities. It queries the npm
  Registry API (registry.npmjs.org) to resolve complete dependency trees, identifying
  phantom dependencies and version conflicts invisible to standard tooling. The skill
  performs deep analysis of each package by querying the OSV.dev API (/v1/query) for
  vulnerability data across multiple ecosystems simultaneously. It identifies not
  just direct CVEs but also malicious package indicators by checking package metadata
  patterns against known typosquatting databases and the Socket.dev API for install
  script analysis. Automated remediation generates pull requests via the GitHub REST
  API v3, using the Git Trees API to create atomic commits that bump vulnerable dependencies
  while respecting peer dependency constraints. Each PR includes a detailed impact
  assessment with breaking change likelihood scores computed from semver analysis
  and changelog parsing. Integration with the npm diff API provides human-readable
  code diffs between vulnerable and patched versions for security team review.
verification: security_reviewed
source: https://agentskillexchange.com/skills/npm-audit-deep-scanner/
category:
- Security &amp; Verification
framework:
- Custom Agents
---

# NPM Audit Deep Scanner

The NPM Audit Deep Scanner skill provides comprehensive JavaScript supply chain security analysis beyond standard npm audit capabilities. It queries the npm Registry API (registry.npmjs.org) to resolve complete dependency trees, identifying phantom dependencies and version conflicts invisible to standard tooling. The skill performs deep analysis of each package by querying the OSV.dev API (/v1/query) for vulnerability data across multiple ecosystems simultaneously. It identifies not just direct CVEs but also malicious package indicators by checking package metadata patterns against known typosquatting databases and the Socket.dev API for install script analysis. Automated remediation generates pull requests via the GitHub REST API v3, using the Git Trees API to create atomic commits that bump vulnerable dependencies while respecting peer dependency constraints. Each PR includes a detailed impact assessment with breaking change likelihood scores computed from semver analysis and changelog parsing. Integration with the npm diff API provides human-readable code diffs between vulnerable and patched versions for security team review.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-audit-deep-scanner/)
