---
title: "Debug Firefox-only browser issues with DevTools MCP before shipping web changes"
description: "Use Firefox DevTools MCP when an agent needs to inspect pages, trace network and console activity, capture screenshots, and automate reproduction steps in Firefox instead of relying on Chrome-first tooling."
verification: security_reviewed
source: "https://github.com/mozilla/firefox-devtools-mcp"
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

This skill is for browser debugging work that specifically needs Firefox. An agent can launch or attach to Firefox, inspect pages, read console and network activity, take snapshots and screenshots, and reproduce UI issues through a DevTools-oriented MCP surface. That makes it a practical fit for web bugs that only show up in Firefox, extension debugging, standards-compliance checks, and cross-browser verification before a change ships.

The scope boundary is tight: this is not a generic browser platform card or a catch-all automation framework entry. The job is to investigate and reproduce Firefox browser behavior through an MCP-compatible debugging workflow. Invoke it when the missing piece is Firefox-aware inspection and reproduction, not when you just need a general-purpose browser SDK or a Chrome-based debugging stack.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/debug-firefox-only-browser-issues-with-devtools-mcp-before-shipping-web-changes/)
