---
name: "Record system-level agent activity with AgentSight"
slug: "record-system-level-agent-activity-with-agentsight"
description: "Wrap Claude Code, Codex, Gemini CLI, OpenClaw, or another agent command with AgentSight to capture processes, files, network destinations, prompts, and reports."
github_stars: 469
verification: "security_reviewed"
source: "https://github.com/eunomia-bpf/agentsight"
author: "eunomia-bpf"
publisher_type: "organization"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "eunomia-bpf/agentsight"
  github_stars: 469
---

# Record system-level agent activity with AgentSight

Wrap Claude Code, Codex, Gemini CLI, OpenClaw, or another agent command with AgentSight to capture processes, files, network destinations, prompts, and reports.

## Prerequisites

Linux with eBPF support, sudo or equivalent probe permissions, Rust Cargo or AgentSight release binary, target agent CLI such as Claude Code, Codex, Gemini CLI, OpenCode, or OpenClaw

## Installation

Use the upstream install or setup path that matches your environment:
- cargo install agentsight
- For local use, install with cargo install agentsight or download the latest
- Docker is useful for container, CI, or isolated Linux environments, but it still needs privileged host access for eBPF. See [docs/docker.md](https://github.com/eunomia-bpf/agentsight/blob/master/docs/docker.md).
- cargo run --manifest-path agentpprof/Cargo.toml -- \

Requirements and caveats from upstream:
- | Python (aider, open-interpreter, …) | sudo ./agentsight record -c python |
- | Docker containers (OpenClaw, …) | sudo ./agentsight record -c node --binary-path docker://openclaw |
- **Q: Why doesn't AgentSight capture traffic from Claude Code, Node.js, or Gemini CLI?**

Basic usage or getting-started notes:
- Run agentsight around Claude Code, Codex, Gemini CLI,
- sudo agentsight top
- <div align="center">

- Source: https://github.com/eunomia-bpf/agentsight
- Extracted from upstream docs: https://raw.githubusercontent.com/eunomia-bpf/agentsight/HEAD/README.md

## Documentation

- https://eunomia.dev/agentsight/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/record-system-level-agent-activity-with-agentsight/)
