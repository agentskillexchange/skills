---
name: "Swagger UI Documentation Deployer"
description: "Deploys interactive Swagger UI documentation sites from OpenAPI specs with custom branding, authentication presets, and CDN-hosted static builds. Integrates with Redoc for alternative rendering."
category: "Library & API Reference"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/swagger-ui-documentation-deployer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "swagger"  # from ase_tool_match
  github_stars: 28702  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3219093  # from ase_npm_downloads
  github_repo: "swagger-api/swagger-ui"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Swagger UI Documentation Deployer

Deploys interactive Swagger UI documentation sites from OpenAPI specs with custom branding, authentication presets, and CDN-hosted static builds. Integrates with Redoc for alternative rendering.

## Overview

This skill deploys interactive API documentation portals using Swagger UI and Redoc from OpenAPI specification files. It configures Swagger UI with custom branding including logos, color schemes, and typography matching organizational design systems. Authentication preset configuration enables Try It Out functionality with pre-populated API keys, OAuth2 client credentials, and JWT tokens for developer testing. The deployer generates static HTML builds suitable for CDN hosting on S3, CloudFront, or GitHub Pages with proper cache headers and content security policies. Multiple spec versions are supported through a version selector dropdown with automatic redirect from latest paths. The skill embeds custom CSS and JavaScript plugins for enhanced functionality including request history, response diffing, and webhook simulation. Redoc integration provides an alternative three-panel layout with nested schema visualization. Search functionality indexes endpoint descriptions, parameter names, and schema properties for quick navigation. Analytics integration tracks endpoint usage patterns to identify popular and underutilized API surfaces.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill swagger-ui-documentation-deployer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill swagger-ui-documentation-deployer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill swagger-ui-documentation-deployer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill swagger-ui-documentation-deployer -a codex
```

### OpenClaw

```bash
clawhub install swagger-ui-documentation-deployer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/swagger-ui-documentation-deployer/
