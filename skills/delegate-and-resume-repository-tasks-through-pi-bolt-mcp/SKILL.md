---
name: "Delegate and resume repository tasks through Pi-Bolt MCP"
slug: "delegate-and-resume-repository-tasks-through-pi-bolt-mcp"
description: "Delegate a scoped repository task to Pi-Bolt over MCP, inspect structured results, and resume the same Pi session for follow-up work and verification."
github_stars: 343
verification: "security_reviewed"
source: "https://github.com/opensec-git/Pi-Bolt"
author: "OpenSec (opensec-git)"
publisher_type: "community"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "opensec-git/Pi-Bolt"
  github_stars: 343
  npm_package: "pi-bolt"
  npm_weekly_downloads: 2124
---

# Delegate and resume repository tasks through Pi-Bolt MCP

Delegate a scoped repository task to Pi-Bolt over MCP, inspect structured results, and resume the same Pi session for follow-up work and verification.

## Prerequisites

Pi-Bolt executable for a supported OS/architecture; MCP stdio client; configured model provider; explicitly selected and trusted repository directory

## Installation

Install or set up from the source-backed instructions:

Download the matching asset from https://github.com/opensec-git/Pi-Bolt/releases/latest, verify against the published SHA256SUMS, and unpack it. Run Pi-Bolt interactively to configure a provider and review trust for the intended project. Configure the MCP client with the absolute executable path and args ["--mcp"]. For Claude Code, upstream documents: claude mcp add pi-bolt -- /full/path/to/pi-bolt --mcp. Call prompt with a bounded task and absolute cwd; retain sessionId for follow-ups. Avoid blanket project approval. See upstream README for platform prerequisites.

- Source: https://github.com/opensec-git/Pi-Bolt

## Documentation

- https://github.com/opensec-git/Pi-Bolt/blob/pi-bolt/docs/MCP.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/delegate-and-resume-repository-tasks-through-pi-bolt-mcp/)
