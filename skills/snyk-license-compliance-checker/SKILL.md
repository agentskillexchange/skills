---
title: "Snyk License Compliance Checker"
description: "Uses the Snyk CLI and REST API to audit open-source dependencies for license compliance across npm, PyPI, Maven, and Go modules. Generates SPDX license reports and flags copyleft violations."
verification: security_reviewed
source: "https://github.com/snyk/cli"
category:
  - "Security &amp; Verification"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-license-compliance-checker/)
