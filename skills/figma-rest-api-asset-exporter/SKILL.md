---
name: "Figma REST API Asset Exporter"
description: "Exports design assets from Figma files using the GET /v1/files/:key and /v1/images/:key endpoints. Supports SVG, PNG, and PDF export with scale and format parameters."
category: "Image & Creative Automation"
framework: "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/figma-rest-api-asset-exporter/"
---

# Figma REST API Asset Exporter

Exports design assets from Figma files using the GET /v1/files/:key and /v1/images/:key endpoints. Supports SVG, PNG, and PDF export with scale and format parameters.

## Overview

The Figma REST API Asset Exporter automates design asset extraction from Figma files through the Figma Platform API. It queries GET /v1/files/:file_key to traverse the document tree, identifying exportable components and frames by node type and name conventions.

Core functionality includes batch image export via GET /v1/images/:file_key with ids parameter for specific node selection, format specification (svg, png, jpg, pdf), and scale multiplier (1x through 4x) for resolution variants. The exporter parses the images response to download rendered assets from the returned S3 URLs with automatic retry on rate limit (429) responses.

Advanced capabilities include component set detection through GET /v1/files/:key/components for design system asset extraction, style extraction via GET /v1/files/:key/styles for color and typography tokens, and version history traversal using GET /v1/files/:key/versions for tracking design changes. It supports Figma Variables API for extracting design tokens as JSON, handles nested frame hierarchies for organized directory output, and implements webhook listeners for file_update events to trigger automated export pipelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill figma-rest-api-asset-exporter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill figma-rest-api-asset-exporter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill figma-rest-api-asset-exporter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill figma-rest-api-asset-exporter -a codex
```

### OpenClaw

```bash
clawhub install figma-rest-api-asset-exporter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/figma-rest-api-asset-exporter/
