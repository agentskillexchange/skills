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

Use the upstream install or setup path that matches your environment:
- npx plugins add google-labs-code/stitch-skills --scope project --target claude-code
- npx plugins add google-labs-code/stitch-skills --scope workspace --target cursor
- OpenCode does **not** use npx plugins / npx skills or the Codex/Claude marketplace layout.
- npx skills add google-labs-code/stitch-skills

Requirements and caveats from upstream:
- **Naming:** OpenCode requires skill name frontmatter to be lowercase kebab-case and match the directory name. Skills that use stitch::… names (or other non-kebab forms) need the name field and folder renamed before Op...
- Stitch Design Skills often have inter-dependencies. If you choose to install skills selectively, ensure you include all required dependencies.

Basic usage or getting-started notes:
- The fastest way to set up the full Stitch plugin suite globally.
- Add the Stitch Skills marketplace, then install the plugins you need.
- <details open>

- Source: https://github.com/google-labs-code/stitch-skills
- Extracted from upstream docs: https://raw.githubusercontent.com/google-labs-code/stitch-skills/HEAD/README.md

## Documentation

- https://stitch.withgoogle.com/docs/mcp/setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/use-stitch-skills-to-generate-convert-and-sync-ui-designs-through-agent-workflows/)
