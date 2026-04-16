---
title: "Snyk License Compliance Checker"
description: "Uses the Snyk CLI and REST API to audit open-source dependencies for license compliance across npm, PyPI, Maven, and Go modules. Generates SPDX license reports and flags copyleft violations."
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

# Snyk License Compliance Checker

The Snyk License Compliance Checker skill integrates with the Snyk CLI and REST API to perform comprehensive license auditing across software projects. It analyzes dependency trees for npm, PyPI, Maven, Go modules, and NuGet packages, identifying all transitive dependency licenses.


The skill maintains configurable license allowlists and denylists, flagging copyleft licenses (GPL, AGPL, LGPL) and proprietary-incompatible licenses based on organizational policy. It cross-references licenses against the SPDX License List for standardized identification and generates compliance reports in SPDX and CycloneDX SBOM formats.


Advanced features include dual-license resolution, license exception handling (e.g., Classpath exception for GPL), and risk scoring based on license permissiveness. The skill integrates with legal review workflows, generating approval requests for newly detected license types. It supports policy-as-code via Snyk’s org-level settings and can gate pull requests when non-compliant dependencies are introduced.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-license-compliance-checker/)
