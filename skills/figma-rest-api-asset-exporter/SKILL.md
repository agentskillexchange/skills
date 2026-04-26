---
title: "Figma REST API Asset Exporter"
description: "Exports design assets from Figma files using the GET /v1/files/:key and /v1/images/:key endpoints. Supports SVG, PNG, and PDF export with scale and format parameters."
verification: "security_reviewed"
source: "https://developers.figma.com/docs/rest-api/"
category:
  - "Image & Creative Automation"
framework:
  - "Custom Agents"
---

# Figma REST API Asset Exporter

The Figma REST API Asset Exporter automates design asset extraction from Figma files through the Figma Platform API. It queries GET /v1/files/:file_key to traverse the document tree, identifying exportable components and frames by node type and name conventions.

Core functionality includes batch image export via GET /v1/images/:file_key with ids parameter for specific node selection, format specification (svg, png, jpg, pdf), and scale multiplier (1x through 4x) for resolution variants. The exporter parses the images response to download rendered assets from the returned S3 URLs with automatic retry on rate limit (429) responses.

Advanced capabilities include component set detection through GET /v1/files/:key/components for design system asset extraction, style extraction via GET /v1/files/:key/styles for color and typography tokens, and version history traversal using GET /v1/files/:key/versions for tracking design changes. It supports Figma Variables API for extracting design tokens as JSON, handles nested frame hierarchies for organized directory output, and implements webhook listeners for file_update events to trigger automated export pipelines.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/figma-rest-api-asset-exporter/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/figma-rest-api-asset-exporter
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/figma-rest-api-asset-exporter`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-rest-api-asset-exporter/)
