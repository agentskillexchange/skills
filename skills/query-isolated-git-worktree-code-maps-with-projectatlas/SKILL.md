---
name: "Query isolated Git worktree code maps with ProjectAtlas"
slug: "query-isolated-git-worktree-code-maps-with-projectatlas"
description: "Register existing Git worktrees under explicit MCP aliases, refresh their separate code maps, and return bounded source evidence across selected checkouts."
github_stars: 456
verification: "security_reviewed"
source: "https://github.com/styler-ai/ProjectAtlas"
author: "styler-ai"
publisher_type: "individual"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "styler-ai/ProjectAtlas"
  github_stars: 456
---

# Query isolated Git worktree code maps with ProjectAtlas

Register existing Git worktrees under explicit MCP aliases, refresh their separate code maps, and return bounded source evidence across selected checkouts.

## Prerequisites

ProjectAtlas v0.5.0 native runtime; MCP-compatible coding host; existing local Git worktrees; Rust toolchain only for Cargo installation

## Installation

Install or set up from the source-backed instructions:

Install the v0.5.0 native release for your platform following docs/agent-integration.md, or build with cargo install --git https://github.com/styler-ai/ProjectAtlas --tag v0.5.0 projectatlas-cli --locked. Follow the upstream installer and host-configuration guide to configure the native MCP process for an explicitly selected control checkout; restart the coding host. Initialize the control checkout once with atlas init if its local state is absent. Read the version-matched upstream ProjectAtlas skill and worktree guide before registering existing worktrees. Cargo builds require a Rust toolchain; native release binaries do not.

- Source: https://github.com/styler-ai/ProjectAtlas

## Documentation

- https://github.com/styler-ai/ProjectAtlas/blob/v0.5.0/docs/worktree-lifecycle.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-isolated-git-worktree-code-maps-with-projectatlas/)
