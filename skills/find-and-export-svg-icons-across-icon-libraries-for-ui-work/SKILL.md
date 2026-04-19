---
title: "Find and export SVG icons across icon libraries for UI work"
description: "Better Icons is an MCP/CLI tool for searching and retrieving icons, and the useful agent skill here is very specific: an agent searches across many icon libraries, narrows down candidates for a design or frontend task, and returns the exact icon SVG or machine-readable result needed by the implementation. Invoke this when the user asks for the right icon for a button, nav item, state badge, settings panel, auth flow, or any other UI element and you want the agent to do more than vaguely suggest “use a home icon.” The agent can search by concept, constrain by prefix or library, compare candidates, and export a concrete SVG or JSON result that can be dropped into code or design assets. That is the skill-shaped job-to-be-done. The boundary prevents this from collapsing into a product card. This entry is not “here is an icon search package” or “here is an MCP server.” It is about delegated icon selection and retrieval for real UI work. If someone only needs a package registry listing, an icon website, or a general-purpose design tool, that is not what this entry is for. Integration points are straightforward from upstream: the tool supports CLI search, direct SVG retrieval, JSON output for scripting, and MCP setup for agent environments. That makes it a good fit for frontend builds, design systems, quick refactors, and automated UI assembly where the agent must choose and fetch an actual icon asset instead of merely naming one."
source: "https://github.com/better-auth/better-icons"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "better-auth/better-icons"
  github_stars: 915
---

# Find and export SVG icons across icon libraries for UI work

Better Icons is an MCP/CLI tool for searching and retrieving icons, and the useful agent skill here is very specific: an agent searches across many icon libraries, narrows down candidates for a design or frontend task, and returns the exact icon SVG or machine-readable result needed by the implementation. Invoke this when the user asks for the right icon for a button, nav item, state badge, settings panel, auth flow, or any other UI element and you want the agent to do more than vaguely suggest “use a home icon.” The agent can search by concept, constrain by prefix or library, compare candidates, and export a concrete SVG or JSON result that can be dropped into code or design assets. That is the skill-shaped job-to-be-done. The boundary prevents this from collapsing into a product card. This entry is not “here is an icon search package” or “here is an MCP server.” It is about delegated icon selection and retrieval for real UI work. If someone only needs a package registry listing, an icon website, or a general-purpose design tool, that is not what this entry is for. Integration points are straightforward from upstream: the tool supports CLI search, direct SVG retrieval, JSON output for scripting, and MCP setup for agent environments. That makes it a good fit for frontend builds, design systems, quick refactors, and automated UI assembly where the agent must choose and fetch an actual icon asset instead of merely naming one.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-and-export-svg-icons-across-icon-libraries-for-ui-work/)
