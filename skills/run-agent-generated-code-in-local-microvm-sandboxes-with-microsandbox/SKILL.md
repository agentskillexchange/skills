---
name: "Run agent-generated code in local microVM sandboxes with Microsandbox"
slug: "run-agent-generated-code-in-local-microvm-sandboxes-with-microsandbox"
description: "Use Microsandbox to create local microVM-backed sandboxes for isolated execution of untrusted agent-generated code and tool calls."
github_stars: 6451
verification: "security_reviewed"
source: "https://github.com/superradcompany/microsandbox"
author: "Super Rad Company"
publisher_type: "open_source_project"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "superradcompany/microsandbox"
  github_stars: 6451
---

# Run agent-generated code in local microVM sandboxes with Microsandbox

Use Microsandbox to create local microVM-backed sandboxes for isolated execution of untrusted agent-generated code and tool calls.

## Prerequisites

Microsandbox, local microVM support, agent code execution workflow

## Installation

Use the upstream install or setup path that matches your environment:
- cargo add microsandbox # 🦀 Rust
- uv add microsandbox # 🐍 Python
- npm i microsandbox # 🟦 TypeScript
- npx microsandbox run debian

Requirements and caveats from upstream:
- <img height="14" src="https://octicons-col.vercel.app/package/A770EF"> **OCI Compatible**: Runs standard container images from Docker Hub, GHCR, or any OCI registry.
- .image("python")

Basic usage or getting-started notes:
- <img height="14" src="https://octicons-col.vercel.app/database/A770EF"> **Long-Running**: Sandboxes can run in detached mode. Great for long-lived sessions.
- msb run debian

- Source: https://github.com/superradcompany/microsandbox
- Extracted from upstream docs: https://raw.githubusercontent.com/superradcompany/microsandbox/HEAD/README.md

## Documentation

- https://github.com/superradcompany/microsandbox

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agent-generated-code-in-local-microvm-sandboxes-with-microsandbox/)
