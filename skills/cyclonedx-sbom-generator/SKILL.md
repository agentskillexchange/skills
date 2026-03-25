---
name: "CycloneDX SBOM Generator"
description: "Generates Software Bill of Materials in CycloneDX format using cdxgen and Syft. Scans npm, pip, and Go modules for known CVEs via OSV.dev API integration."
category: "Security & Verification"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cyclonedx-sbom-generator/"
---

# CycloneDX SBOM Generator

Generates Software Bill of Materials in CycloneDX format using cdxgen and Syft. Scans npm, pip, and Go modules for known CVEs via OSV.dev API integration.

## Overview

Generates Software Bill of Materials in CycloneDX format using cdxgen and Syft. Scans npm, pip, and Go modules for known CVEs via OSV.dev API integration.

This skill provides automated tooling for cyclonedx sbom generator workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cyclonedx-sbom-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cyclonedx-sbom-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cyclonedx-sbom-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cyclonedx-sbom-generator -a codex
```

### OpenClaw

```bash
clawhub install cyclonedx-sbom-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cyclonedx-sbom-generator/
