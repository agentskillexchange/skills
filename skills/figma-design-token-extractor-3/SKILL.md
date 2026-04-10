---
name: "Figma Design Token Extractor"
description: "Extracts design tokens from Figma files using the Figma REST API and style-dictionary. Generates CSS custom properties, Tailwind configs, and Swift/Kotlin theme files from Figma components."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/figma-design-token-extractor-3/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Cursor"
---

# Figma Design Token Extractor

The Figma Design Token Extractor bridges design and development by pulling design tokens directly from Figma files via the Figma REST API. It uses style-dictionary to transform extracted tokens into platform-specific output formats.
The skill connects to Figma files and retrieves color styles, text styles, effect styles, and component properties. It maps Figma style definitions to W3C Design Token Community Group format, creating a canonical token source that feeds into multiple output targets. Supported outputs include CSS custom properties with light/dark theme variants, Tailwind CSS configuration with extended theme values, Swift asset catalogs and UIColor extensions for iOS, and Kotlin compose theme files for Android.
Token synchronization detects changes between Figma file versions and generates diffs showing added, modified, and removed tokens. The extractor handles complex token hierarchies including composite tokens for typography, shadows, and gradients. It generates Storybook documentation pages showcasing all extracted design tokens with live previews.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-design-token-extractor-3/)
