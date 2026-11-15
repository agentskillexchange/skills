---
name: "Build embeddable Rust coding agents with Cersei"
slug: "build-embeddable-rust-coding-agents-with-cersei"
description: "Compose coding-agent primitives in Rust, including tool execution, LLM streaming, sub-agent orchestration, memory, and MCP support, as an embeddable application workflow."
github_stars: 400
verification: "security_reviewed"
source: "https://github.com/pacifio/cersei"
author: "Adib Mohsin"
publisher_type: "individual"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "pacifio/cersei"
  github_stars: 400
---

# Build embeddable Rust coding agents with Cersei

Compose coding-agent primitives in Rust, including tool execution, LLM streaming, sub-agent orchestration, memory, and MCP support, as an embeddable application workflow.

## Prerequisites

Rust toolchain, Cargo, model provider credentials, optional MCP-compatible tools

## Installation

Use the upstream install or setup path that matches your environment:
- cargo install --path crates/abstract-cli
- cargo run --example stress_core_infrastructure --release # system prompt, compact, context, bash classifier
- cargo run --example stress_tools --release # all 30+ tools, registry, performance
- cargo run --example stress_orchestration --release # sub-agents, coordinator, tasks, messaging

Basic usage or getting-started notes:
- abstract # Interactive REPL
- abstract "fix the failing tests" # Single-shot
- abstract --resume # Resume last session

- Source: https://github.com/pacifio/cersei
- Extracted from upstream docs: https://raw.githubusercontent.com/pacifio/cersei/HEAD/README.md

## Documentation

- https://cersei.pacifio.dev/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-embeddable-rust-coding-agents-with-cersei/)
