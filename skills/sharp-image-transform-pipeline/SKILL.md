---
name: "Sharp Image Transform Pipeline"
description: "Builds composable image processing pipelines using the Sharp library with libvips bindings for Node.js. Chains resize, crop, overlay, and format conversion operations with streaming I/O, EXIF metadata preservation, and ICC color profile management."
category: "Image & Creative Automation"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sharp-image-transform-pipeline/"
tool_ecosystem:
  tool: "sharp"
  github_stars: 32074
  npm_weekly_downloads: 54450041
  github_repo: "lovell/sharp"
  license: "Apache-2.0"
  maintained: true
---

# Sharp Image Transform Pipeline

Builds composable image processing pipelines using the Sharp library with libvips bindings for Node.js. Chains resize, crop, overlay, and format conversion operations with streaming I/O, EXIF metadata preservation, and ICC color profile management.

## Overview

Builds composable image processing pipelines using the Sharp library with libvips bindings for Node.js. Chains resize, crop, overlay, and format conversion operations with streaming I/O, EXIF metadata preservation, and ICC color profile management.

This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sharp-image-transform-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sharp-image-transform-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sharp-image-transform-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sharp-image-transform-pipeline -a codex
```

### OpenClaw

```bash
clawhub install sharp-image-transform-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sharp-image-transform-pipeline/
