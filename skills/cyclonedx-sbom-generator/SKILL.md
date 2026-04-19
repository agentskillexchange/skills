---
title: "CycloneDX SBOM Generator"
description: "Generates Software Bill of Materials in CycloneDX format using cdxgen and Syft. Scans npm, pip, and Go modules for known CVEs via OSV.dev API integration. This skill provides automated tooling for cyclonedx sbom generator workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs."
source: "https://agentskillexchange.com/skills/cyclonedx-sbom-generator/"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Cursor"
---

# CycloneDX SBOM Generator

Generates Software Bill of Materials in CycloneDX format using cdxgen and Syft. Scans npm, pip, and Go modules for known CVEs via OSV.dev API integration. This skill provides automated tooling for cyclonedx sbom generator workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cyclonedx-sbom-generator/)
