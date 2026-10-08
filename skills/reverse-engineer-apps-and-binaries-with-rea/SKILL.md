---
name: "Reverse-engineer apps and binaries with REA"
slug: "reverse-engineer-apps-and-binaries-with-rea"
description: "Connect coding agents to REA's MCP tools so they can inspect apps, binaries, websites, APKs, and runtime behavior with evidence-backed findings."
github_stars: 17094
verification: "security_reviewed"
source: "https://github.com/morluto/rea"
author: "morluto"
publisher_type: "open_source"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "morluto/rea"
  github_stars: 17094
  npm_package: "rea-agents"
  npm_weekly_downloads: 1291
---

# Reverse-engineer apps and binaries with REA

Connect coding agents to REA's MCP tools so they can inspect apps, binaries, websites, APKs, and runtime behavior with evidence-backed findings.

## Prerequisites

Node.js 22.19+ or newer, npm, an MCP-capable agent, and optional analysis tools such as Hopper, Ghidra, IDA, Chrome, JADX, binwalk, or Unblob depending on the target.

## Installation

Install or set up from the source-backed instructions:

Run `npx rea-agents setup`, choose the supported agents to configure, review the proposed MCP and instruction changes, approve them, and restart the agent. For CLI-only use, run `npm install --global rea-agents` and then `rea --help`.

- Source: https://github.com/morluto/rea

## Documentation

- https://morluto.github.io/rea/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reverse-engineer-apps-and-binaries-with-rea/)
