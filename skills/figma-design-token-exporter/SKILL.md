---
title: "Figma Design Token Exporter"
description: "Extracts design tokens from Figma files using the Figma REST API v1 and transforms them into platform-specific formats via Style Dictionary. Supports CSS custom properties, Tailwind config, and iOS/Android native tokens."
verification: "security_reviewed"
source: "https://developers.figma.com/docs/rest-api/"
category:
  - "Image & Creative Automation"
framework:
  - "Claude Code"
---

# Figma Design Token Exporter

The Figma Design Token Exporter connects to Figma files through the official REST API v1 to extract colors, typography, spacing, and effect styles as structured design tokens. It processes the Figma document tree to resolve component variants, nested fills, and auto-layout properties into a normalized token schema. Transformation is handled by Amazon Style Dictionary, converting raw tokens into multiple output formats simultaneously: CSS custom properties, SCSS variables, Tailwind CSS configuration objects, Swift UIColor extensions, and Android XML resource files. The skill handles complex token relationships including composite tokens, mathematical expressions, and alias references. It monitors Figma file versions via webhooks and can trigger automated token regeneration on design changes. The skill includes diff reporting to highlight which tokens changed between versions, preventing unexpected UI regressions. Output tokens are validated against W3C Design Token Community Group specification for interoperability.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/figma-design-token-exporter/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/figma-design-token-exporter
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/figma-design-token-exporter`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-design-token-exporter/)
