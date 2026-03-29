---
name: "Figma Design Token Extractor"
description: "Extracts design tokens from Figma files using the Figma REST API and style-dictionary. Generates CSS custom properties, Tailwind configs, and Swift/Kotlin theme files from Figma components."
category: "Image & Creative Automation"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/figma-design-token-extractor-3/"
tool_ecosystem:
  tool: storybook
  github_stars: 89504
  npm_weekly_downloads: 13033154
  github_repo: storybookjs/storybook
  license: MIT
  maintained: true
---
# Figma Design Token Extractor

Extracts design tokens from Figma files using the Figma REST API and style-dictionary. Generates CSS custom properties, Tailwind configs, and Swift/Kotlin theme files from Figma components.

## Overview

The Figma Design Token Extractor bridges design and development by pulling design tokens directly from Figma files via the Figma REST API. It uses style-dictionary to transform extracted tokens into platform-specific output formats.

The skill connects to Figma files and retrieves color styles, text styles, effect styles, and component properties. It maps Figma style definitions to W3C Design Token Community Group format, creating a canonical token source that feeds into multiple output targets. Supported outputs include CSS custom properties with light/dark theme variants, Tailwind CSS configuration with extended theme values, Swift asset catalogs and UIColor extensions for iOS, and Kotlin compose theme files for Android.

Token synchronization detects changes between Figma file versions and generates diffs showing added, modified, and removed tokens. The extractor handles complex token hierarchies including composite tokens for typography, shadows, and gradients. It generates Storybook documentation pages showcasing all extracted design tokens with live previews.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill figma-design-token-extractor-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill figma-design-token-extractor-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill figma-design-token-extractor-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill figma-design-token-extractor-3 -a codex
```

### OpenClaw

```bash
clawhub install figma-design-token-extractor-3
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-design-token-extractor-3/)
