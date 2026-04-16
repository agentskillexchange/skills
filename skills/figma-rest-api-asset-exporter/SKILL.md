---
title: "Figma REST API Asset Exporter"
description: "Exports design assets from Figma files using the GET /v1/files/:key and /v1/images/:key endpoints. Supports SVG, PNG, and PDF export with scale and format parameters."
verification: "security_reviewed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-rest-api-asset-exporter/)
