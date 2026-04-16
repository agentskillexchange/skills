---
title: "Figma Design Token Exporter"
description: "Extracts design tokens from Figma files using the Figma REST API v1 and transforms them into platform-specific formats via Style Dictionary. Supports CSS custom properties, Tailwind config, and iOS/Android native tokens."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/figma-design-token-exporter/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Code"
---

# Figma Design Token Exporter

The Figma Design Token Exporter connects to Figma files through the official REST API v1 to extract colors, typography, spacing, and effect styles as structured design tokens. It processes the Figma document tree to resolve component variants, nested fills, and auto-layout properties into a normalized token schema.

Transformation is handled by Amazon Style Dictionary, converting raw tokens into multiple output formats simultaneously: CSS custom properties, SCSS variables, Tailwind CSS configuration objects, Swift UIColor extensions, and Android XML resource files. The skill handles complex token relationships including composite tokens, mathematical expressions, and alias references.

It monitors Figma file versions via webhooks and can trigger automated token regeneration on design changes. The skill includes diff reporting to highlight which tokens changed between versions, preventing unexpected UI regressions. Output tokens are validated against W3C Design Token Community Group specification for interoperability.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-design-token-exporter/)
