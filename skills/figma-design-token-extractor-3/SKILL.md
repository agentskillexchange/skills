---
title: "Figma Design Token Extractor"
description: "Extracts design tokens from Figma files using the Figma REST API and style-dictionary. Generates CSS custom properties, Tailwind configs, and Swift/Kotlin theme files from Figma components."
verification: security_reviewed
source: "https://developers.figma.com/docs/rest-api/"
category:
  - "Image & Creative Automation"
framework:
  - "Cursor"
---

# Figma Design Token Extractor

The Figma Design Token Extractor bridges design and development by pulling design tokens directly from Figma files via the Figma REST API. It uses style-dictionary to transform extracted tokens into platform-specific output formats.

The skill connects to Figma files and retrieves color styles, text styles, effect styles, and component properties. It maps Figma style definitions to W3C Design Token Community Group format, creating a canonical token source that feeds into multiple output targets. Supported outputs include CSS custom properties with light/dark theme variants, Tailwind CSS configuration with extended theme values, Swift asset catalogs and UIColor extensions for iOS, and Kotlin compose theme files for Android.

Token synchronization detects changes between Figma file versions and generates diffs showing added, modified, and removed tokens. The extractor handles complex token hierarchies including composite tokens for typography, shadows, and gradients. It generates Storybook documentation pages showcasing all extracted design tokens with live previews.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/figma-design-token-extractor-3
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/figma-design-token-extractor-3` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-design-token-extractor-3/)
