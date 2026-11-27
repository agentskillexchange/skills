---
name: "Build reviewed repository context packets with RepoPrompt CE MCP"
slug: "build-reviewed-repository-context-repoprompt-ce-mcp"
description: "Bind a repository workspace, discover relevant files, refine slices and code maps, inspect token usage, and export a reviewed context packet through MCP."
github_stars: 997
verification: "security_reviewed"
source: "https://github.com/repoprompt/repoprompt-ce"
author: "RepoPrompt"
publisher_type: "Organization"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "repoprompt/repoprompt-ce"
  github_stars: 997
---

# Build reviewed repository context packets with RepoPrompt CE MCP

Bind a repository workspace, discover relevant files, refine slices and code maps, inspect token usage, and export a reviewed context packet through MCP.

## Prerequisites

macOS 26+; RepoPrompt CE; Homebrew; MCP-compatible client; configured provider for Context Builder

## Installation

Install or set up from the source-backed instructions:

Requires macOS 26 or later and Homebrew. Run brew tap repoprompt/repoprompt-ce, then brew install --cask repoprompt-ce to install the signed public application. Open RepoPrompt CE, load the intended repository as a workspace, and configure your MCP client using the app’s MCP settings and bundled repoprompt-mcp executable. App-backed stdio is the default; keep the app running for this workflow. Inspect tools/list and the installed schemas before calling tools. Source builds additionally require full Xcode 26; they are unnecessary for the Homebrew application.

- Source: https://github.com/repoprompt/repoprompt-ce

## Documentation

- https://github.com/repoprompt/repoprompt-ce/blob/main/docs/architecture/headless-mcp-runtime.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-reviewed-repository-context-repoprompt-ce-mcp/)
