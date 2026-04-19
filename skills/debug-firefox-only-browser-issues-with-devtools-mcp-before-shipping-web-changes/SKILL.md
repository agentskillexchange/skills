---
title: "Debug Firefox-only browser issues with DevTools MCP before shipping web changes"
description: "This skill is for browser debugging work that specifically needs Firefox. An agent can launch or attach to Firefox, inspect pages, read console and network activity, take snapshots and screenshots, and reproduce UI issues through a DevTools-oriented MCP surface. That makes it a practical fit for web bugs that only show up in Firefox, extension debugging, standards-compliance checks, and cross-browser verification before a change ships. The scope boundary is tight: this is not a generic browser platform card or a catch-all automation framework entry. The job is to investigate and reproduce Firefox browser behavior through an MCP-compatible debugging workflow. Invoke it when the missing piece is Firefox-aware inspection and reproduction, not when you just need a general-purpose browser SDK or a Chrome-based debugging stack."
source: "https://github.com/mozilla/firefox-devtools-mcp"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "mozilla/firefox-devtools-mcp"
  github_stars: 107
  npm_package: "firefox-devtools-mcp"
  npm_weekly_downloads: 2962
---

# Debug Firefox-only browser issues with DevTools MCP before shipping web changes

This skill is for browser debugging work that specifically needs Firefox. An agent can launch or attach to Firefox, inspect pages, read console and network activity, take snapshots and screenshots, and reproduce UI issues through a DevTools-oriented MCP surface. That makes it a practical fit for web bugs that only show up in Firefox, extension debugging, standards-compliance checks, and cross-browser verification before a change ships. The scope boundary is tight: this is not a generic browser platform card or a catch-all automation framework entry. The job is to investigate and reproduce Firefox browser behavior through an MCP-compatible debugging workflow. Invoke it when the missing piece is Firefox-aware inspection and reproduction, not when you just need a general-purpose browser SDK or a Chrome-based debugging stack.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/debug-firefox-only-browser-issues-with-devtools-mcp-before-shipping-web-changes/)
