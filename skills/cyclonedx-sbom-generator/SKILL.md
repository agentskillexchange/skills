---
title: "CycloneDX SBOM Generator"
description: "Generates Software Bill of Materials in CycloneDX format using cdxgen and Syft. Scans npm, pip, and Go modules for known CVEs via OSV.dev API integration."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cyclonedx-sbom-generator/"
category:
  - "Security &amp; Verification"
framework:
  - "Cursor"
---

# CycloneDX SBOM Generator

Generates Software Bill of Materials in CycloneDX format using cdxgen and Syft. Scans npm, pip, and Go modules for known CVEs via OSV.dev API integration.

This skill provides automated tooling for cyclonedx sbom generator workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cyclonedx-sbom-generator/)
