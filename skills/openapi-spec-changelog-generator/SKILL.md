---
name: "OpenAPI Spec Changelog Generator"
description: "Compares OpenAPI 3.x specification files using the oasdiff library to detect breaking changes, deprecated endpoints, and schema modifications. Outputs structured changelogs in Markdown or JSON."
category: "Library & API Reference"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/openapi-spec-changelog-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "swagger"  # from ase_tool_match
  github_stars: 28702  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3219093  # from ase_npm_downloads
  github_repo: "swagger-api/swagger-ui"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OpenAPI Spec Changelog Generator

Compares OpenAPI 3.x specification files using the oasdiff library to detect breaking changes, deprecated endpoints, and schema modifications. Outputs structured changelogs in Markdown or JSON.

## Overview

The OpenAPI Spec Changelog Generator uses the oasdiff library (Go-based OpenAPI diff engine) to perform deep semantic comparison between two versions of OpenAPI 3.x specifications. Unlike simple text diffs, it understands OpenAPI structure to detect breaking changes (removed endpoints, required parameter additions, response schema narrowing), non-breaking additions (new optional parameters, additional response fields), and deprecations. The skill parses both YAML and JSON spec formats and resolves $ref references across multi-file specifications. It classifies changes by severity level following the OpenAPI breaking change taxonomy and generates human-readable changelogs in Markdown format suitable for developer portal publication, or structured JSON for integration with API governance pipelines. The generator supports comparing specs from URLs (pulling from Swagger Hub or API gateway exports) and can be integrated into CI to block PRs that introduce unannounced breaking changes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-changelog-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-changelog-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-changelog-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-changelog-generator -a codex
```

### OpenClaw

```bash
clawhub install openapi-spec-changelog-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/openapi-spec-changelog-generator/
