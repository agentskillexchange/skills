---
title: "Find and export SVG icons across icon libraries for UI work"
description: "Better Icons is an MCP/CLI tool for searching and retrieving icons, and the useful agent skill here is very specific: an agent searches across many icon libraries, narrows down candidates for a design or frontend task, and returns the exact icon SVG or machine-readable result needed by the implementation.\nInvoke this when the user asks for the right icon for a button, nav item, state badge, settings panel, auth flow, or any other UI element and you want the agent to do more than vaguely suggest “use a home icon.” The agent can search by concept, constrain by prefix or library, compare candidates, and export a concrete SVG or JSON result that can be dropped into code or design assets. That is the skill-shaped job-to-be-done.\nThe boundary prevents this from collapsing into a product card. This entry is not “here is an icon search package” or “here is an MCP server.” It is about delegated icon selection and retrieval for real UI work. If someone only needs a package registry listing, an icon website, or a general-purpose design tool, that is not what this entry is for.\nIntegration points are straightforward from upstream: the tool supports CLI search, direct SVG retrieval, JSON output for scripting, and MCP setup for agent environments. That makes it a good fit for frontend builds, design systems, quick refactors, and automated UI assembly where the agent must choose and fetch an actual icon asset instead of merely naming one."
verification: security_reviewed
source: "https://github.com/better-auth/better-icons"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "better-auth/better-icons"
  github_stars: 915
---

# Find and export SVG icons across icon libraries for UI work

Better Icons is an MCP/CLI tool for searching and retrieving icons, and the useful agent skill here is very specific: an agent searches across many icon libraries, narrows down candidates for a design or frontend task, and returns the exact icon SVG or machine-readable result needed by the implementation.
Invoke this when the user asks for the right icon for a button, nav item, state badge, settings panel, auth flow, or any other UI element and you want the agent to do more than vaguely suggest “use a home icon.” The agent can search by concept, constrain by prefix or library, compare candidates, and export a concrete SVG or JSON result that can be dropped into code or design assets. That is the skill-shaped job-to-be-done.
The boundary prevents this from collapsing into a product card. This entry is not “here is an icon search package” or “here is an MCP server.” It is about delegated icon selection and retrieval for real UI work. If someone only needs a package registry listing, an icon website, or a general-purpose design tool, that is not what this entry is for.
Integration points are straightforward from upstream: the tool supports CLI search, direct SVG retrieval, JSON output for scripting, and MCP setup for agent environments. That makes it a good fit for frontend builds, design systems, quick refactors, and automated UI assembly where the agent must choose and fetch an actual icon asset instead of merely naming one.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/find-and-export-svg-icons-across-icon-libraries-for-ui-work
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/find-and-export-svg-icons-across-icon-libraries-for-ui-work` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-and-export-svg-icons-across-icon-libraries-for-ui-work/)
