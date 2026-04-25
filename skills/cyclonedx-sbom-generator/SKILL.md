---
title: "CycloneDX SBOM Generator"
description: "Generates Software Bill of Materials in CycloneDX format using cdxgen and Syft. Scans npm, pip, and Go modules for known CVEs via OSV.dev API integration."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cyclonedx-sbom-generator/"
category:
  - "Security & Verification"
framework:
  - "Cursor"
---

# CycloneDX SBOM Generator

Generates Software Bill of Materials in CycloneDX format using cdxgen and Syft. Scans npm, pip, and Go modules for known CVEs via OSV.dev API integration. This skill provides automated tooling for cyclonedx sbom generator workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cyclonedx-sbom-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cyclonedx-sbom-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cyclonedx-sbom-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cyclonedx-sbom-generator/)
