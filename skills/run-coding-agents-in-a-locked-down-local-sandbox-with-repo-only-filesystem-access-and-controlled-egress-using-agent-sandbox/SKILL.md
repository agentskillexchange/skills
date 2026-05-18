---
name: "Run coding agents in a locked-down local sandbox with repo-only filesystem access and controlled egress using agent-sandbox"
slug: "run-coding-agents-in-a-locked-down-local-sandbox-with-repo-only-filesystem-access-and-controlled-egress-using-agent-sandbox"
description: "Put Claude Code, Codex, Gemini, or other supported agent CLIs inside a persistent local sandbox instead of letting them operate directly on the host."
github_stars: 163
verification: "security_reviewed"
source: "https://github.com/mattolson/agent-sandbox"
author: "mattolson"
publisher_type: "individual"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "mattolson/agent-sandbox"
  github_stars: 163
---

# Run coding agents in a locked-down local sandbox with repo-only filesystem access and controlled egress using agent-sandbox

Put Claude Code, Codex, Gemini, or other supported agent CLIs inside a persistent local sandbox instead of letting them operate directly on the host.

## Prerequisites

Docker-compatible runtime, VM layer such as Colima, terminal or supported devcontainer IDE

## Installation

Use the upstream install or setup path that matches your environment:
- brew install colima docker docker-compose docker-buildx

Requirements and caveats from upstream:
- Target platform: [Colima](https://github.com/abiosoft/colima) + [Docker Engine](https://docs.docker.com/engine/) on Apple Silicon. Should work with any Docker-compatible runtime.
- ### 1. Install prerequisites
- You need a VM and Docker installed. This can be done in a variety of ways.

Basic usage or getting-started notes:
- Run AI coding agents in a locked-down local sandbox with:
- **CLI (preferred)** - run the agent in a terminal session using agentbox exec.
- [Colima](https://colima.run/)

- Source: https://github.com/mattolson/agent-sandbox
- Extracted from upstream docs: https://raw.githubusercontent.com/mattolson/agent-sandbox/HEAD/README.md

## Documentation

- https://github.com/mattolson/agent-sandbox#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-coding-agents-in-a-locked-down-local-sandbox-with-repo-only-filesystem-access-and-controlled-egress-using-agent-sandbox/)
