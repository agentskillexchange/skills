---
title: "Find and export SVG icons across icon libraries for UI work"
description: "Use Better Icons when an agent needs to search icon sets, compare matches, and return the exact SVG asset needed for a UI task. It is a narrow asset-selection skill, not a generic icon platform listing."
verification: "security_reviewed"
source: "https://github.com/better-auth/better-icons"
category:
  - "Developer Tools"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-and-export-svg-icons-across-icon-libraries-for-ui-work/)
