---
title: "Figma REST API Asset Exporter"
description: "Exports design assets from Figma files using the GET /v1/files/:key and /v1/images/:key endpoints. Supports SVG, PNG, and PDF export with scale and format parameters."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/figma-rest-api-asset-exporter/"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/figma-rest-api-asset-exporter
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/figma-rest-api-asset-exporter` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-rest-api-asset-exporter/)
