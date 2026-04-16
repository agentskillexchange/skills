---
title: "Figma Design Token Extractor"
description: "Extracts design tokens from Figma files using the Figma REST API and style-dictionary. Generates CSS custom properties, Tailwind configs, and Swift/Kotlin theme files from Figma components."
verification: "security_reviewed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-design-token-extractor-3/)
