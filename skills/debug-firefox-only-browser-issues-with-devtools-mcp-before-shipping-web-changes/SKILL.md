---
title: "Debug Firefox-only browser issues with DevTools MCP before shipping web changes"
description: "Use Firefox DevTools MCP when an agent needs to inspect pages, trace network and console activity, capture screenshots, and automate reproduction steps in Firefox instead of relying on Chrome-first tooling."
verification: "security_reviewed"
source: "https://github.com/mozilla/firefox-devtools-mcp"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "mozilla/firefox-devtools-mcp"
  github_stars: 107
  ase_npm_package: "firefox-devtools-mcp"
  npm_weekly_downloads: 2962
---

# Debug Firefox-only browser issues with DevTools MCP before shipping web changes

This skill is for browser debugging work that specifically needs Firefox. An agent can launch or attach to Firefox, inspect pages, read console and network activity, take snapshots and screenshots, and reproduce UI issues through a DevTools-oriented MCP surface. That makes it a practical fit for web bugs that only show up in Firefox, extension debugging, standards-compliance checks, and cross-browser verification before a change ships.


The scope boundary is tight: this is not a generic browser platform card or a catch-all automation framework entry. The job is to investigate and reproduce Firefox browser behavior through an MCP-compatible debugging workflow. Invoke it when the missing piece is Firefox-aware inspection and reproduction, not when you just need a general-purpose browser SDK or a Chrome-based debugging stack.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/debug-firefox-only-browser-issues-with-devtools-mcp-before-shipping-web-changes/)
