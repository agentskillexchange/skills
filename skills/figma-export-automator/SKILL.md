---
title: "Figma Export Automator"
description: "Exports assets from Figma files using the Figma REST API v1. Extracts component sets, design tokens (colors, typography, spacing), and renders frames as SVG/PNG. Generates CSS custom properties from styles."
verification: "security_reviewed"
source: "https://developers.figma.com/docs/rest-api/"
category:
  - "Image & Creative Automation"
framework:
  - "Claude Agents"
---

# Figma Export Automator

The Figma Export Automator skill connects Claude to Figma’s REST API v1 for extracting design assets and tokens from Figma files programmatically. It reads file structures, component hierarchies, and style definitions without requiring the Figma desktop app. Asset export retrieves specific frames, components, or component sets as SVG, PNG, or PDF at configurable scales (1x through 4x). The skill handles Figma’s asynchronous image rendering — it requests exports, polls for completion, and downloads the rendered files. Batch export processes entire pages or component libraries in parallel. Design token extraction parses Figma’s style definitions to generate CSS custom properties, SCSS variables, or JSON token files. It maps color styles to –color-* variables, typography styles to font-family/size/weight/line-height sets, and effect styles to box-shadow and filter values. Spacing and layout tokens are derived from auto-layout properties on components. The skill also reads component documentation, variant properties, and description fields for generating component API documentation. It detects changes between file versions by comparing node structures, useful for design-to-code synchronization workflows. Authentication uses Figma personal access tokens. Built for design system teams and frontend developers who need automated design-to-code pipelines.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/figma-export-automator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/figma-export-automator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/figma-export-automator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-export-automator/)
