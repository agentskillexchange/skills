---
title: "Figma Design Token Extractor"
description: "Extracts design tokens from Figma files using the Figma REST API and style-dictionary. Generates CSS custom properties, Tailwind configs, and Swift/Kotlin theme files from Figma components."
slug: "figma-design-token-extractor-3"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/figma-design-token-extractor-3/"
listed: true
---

# Figma Design Token Extractor

Extracts design tokens from Figma files using the Figma REST API and style-dictionary. Generates CSS custom properties, Tailwind configs, and Swift/Kotlin theme files from Figma components.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install figma-design-token-extractor-3
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Figma Design Token Extractor bridges design and development by pulling design tokens directly from Figma files via the Figma REST API. It uses style-dictionary to transform extracted tokens into platform-specific output formats.
The skill connects to Figma files and retrieves color styles, text styles, effect styles, and component properties. It maps Figma style definitions to W3C Design Token Community Group format, creating a canonical token source that feeds into multiple output targets. Supported outputs include CSS custom properties with light/dark theme variants, Tailwind CSS configuration with extended theme values, Swift asset catalogs and UIColor extensions for iOS, and Kotlin compose theme files for Android.
Token synchronization detects changes between Figma file versions and generates diffs showing added, modified, and removed tokens. The extractor handles complex token hierarchies including composite tokens for typography, shadows, and gradients. It generates Storybook documentation pages showcasing all extracted design tokens with live previews.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-design-token-extractor-3/)
