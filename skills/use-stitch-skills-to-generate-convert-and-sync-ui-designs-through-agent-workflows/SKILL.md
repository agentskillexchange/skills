---
name: "Use Stitch Skills to generate, convert, and sync UI designs through agent workflows"
slug: "use-stitch-skills-to-generate-convert-and-sync-ui-designs-through-agent-workflows"
description: "Install Google's Stitch skill suite so Codex, Claude Code, Cursor, Gemini CLI, or OpenCode can create screens, upload design assets, extract design systems, and convert Stitch designs into app code."
github_stars: 7750
verification: "security_reviewed"
source: "https://github.com/google-labs-code/stitch-skills"
author: "Google Labs Code"
publisher_type: "organization"
category: "Image & Creative Automation"
framework: "MCP"
tool_ecosystem:
  github_repo: "google-labs-code/stitch-skills"
  github_stars: 7750
---

# Use Stitch Skills to generate, convert, and sync UI designs through agent workflows

Install Google's Stitch skill suite so Codex, Claude Code, Cursor, Gemini CLI, or OpenCode can create screens, upload design assets, extract design systems, and convert Stitch designs into app code.

## Prerequisites

An agent runtime that can load Agent Skills or plugins, plus the Stitch MCP server configured from Google's Stitch documentation

## Installation

For Codex, add the Stitch Skills marketplace, then enable the plugin you need from Codex's plugin UI:

- codex plugin marketplace add google-labs-code/stitch-skills --ref main

For Claude Code, install the project-local plugin with the documented plugins CLI:

- npx plugins add google-labs-code/stitch-skills --scope project --target claude-code

For selective skill installation, use the upstream skills CLI and include any required dependent Stitch skills:

- npx skills add google-labs-code/stitch-skills

- Source: https://github.com/google-labs-code/stitch-skills
- Extracted from upstream docs: https://raw.githubusercontent.com/google-labs-code/stitch-skills/HEAD/README.md

## Documentation

- https://stitch.withgoogle.com/docs/mcp/setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/use-stitch-skills-to-generate-convert-and-sync-ui-designs-through-agent-workflows/)
