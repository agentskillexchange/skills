---
title: "Build embeddable Rust coding agents with Cersei"
description: "Compose coding-agent primitives in Rust, including tool execution, LLM streaming, sub-agent orchestration, memory, and MCP support, as an embeddable application workflow."
verification: "security_reviewed"
source: "https://github.com/pacifio/cersei"
author: "Adib Mohsin"
publisher_type: "individual"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "pacifio/cersei"
  github_stars: 400
---

# Build embeddable Rust coding agents with Cersei

Compose coding-agent primitives in Rust, including tool execution, LLM streaming, sub-agent orchestration, memory, and MCP support, as an embeddable application workflow.

## Prerequisites

Rust toolchain, Cargo, model provider credentials, optional MCP-compatible tools

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add the crate with `cargo add cersei`, configure a supported model provider from environment credentials, import `cersei::prelude::*`, wire coding tools and a permission policy, then run repository tasks from the Rust application.
```

## Documentation

- https://cersei.pacifio.dev/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-embeddable-rust-coding-agents-with-cersei/)
