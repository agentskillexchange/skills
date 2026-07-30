---
name: "Connect RStudio to MCP Agents with ClaudeR"
slug: "connect-rstudio-to-mcp-agents-with-clauder"
description: "Use ClaudeR to expose an active RStudio session to MCP-capable coding and research agents for R execution, plots, manuscript audits, and multi-agent analysis."
github_stars: 305
verification: "security_reviewed"
source: "https://github.com/IMNMV/ClaudeR"
author: "IMNMV"
publisher_type: "open_source_project"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "IMNMV/ClaudeR"
  github_stars: 305
---

# Connect RStudio to MCP Agents with ClaudeR

Use ClaudeR to expose an active RStudio session to MCP-capable coding and research agents for R execution, plots, manuscript audits, and multi-agent analysis.

## Prerequisites

R 4.0 or later, RStudio, Python 3.8 or later, R devtools package, ClaudeR R package, clauder-mcp bridge, MCP-capable agent such as Claude Code, Codex, Gemini CLI, Cursor, or Claude Desktop

## Installation

Install or set up from the source-backed instructions:

Install R and Python prerequisites, install `devtools` in R, run `devtools::install_github("IMNMV/ClaudeR")`, load `library(ClaudeR)`, configure the target agent with `install_clauder()` or `install_cli(tools = "claude")`, then start the RStudio server/addin with `claudeAddin()`.

- Source: https://github.com/IMNMV/ClaudeR

## Documentation

- https://github.com/IMNMV/ClaudeR/blob/main/llms-install.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/connect-rstudio-to-mcp-agents-with-clauder/)
