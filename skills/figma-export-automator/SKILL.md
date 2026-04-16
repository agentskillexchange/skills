---
title: "Figma Export Automator"
description: "Exports assets from Figma files using the Figma REST API v1. Extracts component sets, design tokens (colors, typography, spacing), and renders frames as SVG/PNG. Generates CSS custom properties from styles."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/figma-export-automator/"
category:
  - "Image & Creative Automation"
framework:
  - "Claude Agents"
---

# Figma Export Automator

The Figma Export Automator skill connects Claude to Figma’s REST API v1 for extracting design assets and tokens from Figma files programmatically. It reads file structures, component hierarchies, and style definitions without requiring the Figma desktop app.


Asset export retrieves specific frames, components, or component sets as SVG, PNG, or PDF at configurable scales (1x through 4x). The skill handles Figma’s asynchronous image rendering — it requests exports, polls for completion, and downloads the rendered files. Batch export processes entire pages or component libraries in parallel.


Design token extraction parses Figma’s style definitions to generate CSS custom properties, SCSS variables, or JSON token files. It maps color styles to –color-* variables, typography styles to font-family/size/weight/line-height sets, and effect styles to box-shadow and filter values. Spacing and layout tokens are derived from auto-layout properties on components.


The skill also reads component documentation, variant properties, and description fields for generating component API documentation. It detects changes between file versions by comparing node structures, useful for design-to-code synchronization workflows. Authentication uses Figma personal access tokens. Built for design system teams and frontend developers who need automated design-to-code pipelines.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-export-automator/)
