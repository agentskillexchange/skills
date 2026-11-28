---
name: "Run an asset QA gate before Blender delivery with Blender Skills"
slug: "run-asset-qa-gate-before-blender-delivery-with-blender-skills"
description: "Check one Blender asset with profile-based diagnostics, inspect review images, and report fixes and accepted warnings before delivery."
verification: "security_reviewed"
source: "https://github.com/EL4CTEO/blender-skills/tree/ab601e27a247c18773924188eb580f81c561b249/skills/blender-asset-qa"
author: "EL4CTEO"
publisher_type: "individual"
category: "Image & Creative Automation"
framework: "Multi-Framework"
---

# Run an asset QA gate before Blender delivery with Blender Skills

Check one Blender asset with profile-based diagnostics, inspect review images, and report fixes and accepted warnings before delivery.

## Prerequisites

Blender 5.2 LTS+; blender-core and blender-asset-qa skills; agent shell and image viewer; optional Blender MCP

## Installation

Install or set up from the source-backed instructions:

Install Blender 5.2 LTS or newer. Clone https://github.com/EL4CTEO/blender-skills and check out ab601e27a247c18773924188eb580f81c561b249. On macOS/Linux, inspect install/install.sh, then run bash install/install.sh --agent agents --skills blender-core,blender-asset-qa from the checkout; use --agent claude for Claude Code or the documented install/install.ps1 equivalent on Windows. The installer replaces existing selected skill directories. Load blender-core and request blender-asset-qa for named asset objects. Keep scripts with their adjacent helper files; no MCP server is required for background execution.

- Source: https://github.com/EL4CTEO/blender-skills/tree/ab601e27a247c18773924188eb580f81c561b249/skills/blender-asset-qa

## Documentation

- https://github.com/EL4CTEO/blender-skills/tree/ab601e27a247c18773924188eb580f81c561b249/skills/blender-asset-qa/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-asset-qa-gate-before-blender-delivery-with-blender-skills/)
