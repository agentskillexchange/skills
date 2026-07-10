---
name: "Coordinate human-in-the-loop agent teams in auditable Matrix rooms with HiClaw"
slug: "coordinate-human-in-the-loop-agent-teams-in-auditable-matrix-rooms-with-hiclaw"
description: "Run manager-worker agent collaboration in Matrix rooms where humans can watch, intervene, and keep credentials out of worker hands."
github_stars: 4231
verification: "security_reviewed"
source: "https://github.com/agentscope-ai/HiClaw"
author: "AgentScope AI"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "agentscope-ai/HiClaw"
  github_stars: 4231
---

# Coordinate human-in-the-loop agent teams in auditable Matrix rooms with HiClaw

Run manager-worker agent collaboration in Matrix rooms where humans can watch, intervene, and keep credentials out of worker hands.

## Prerequisites

Docker; Matrix/Element client; LLM API key

## Installation

Use the upstream install or setup path that matches your environment:
- docker exec -it hiclaw-manager cat /var/log/hiclaw/manager-agent.log
- make build # Build all images
- make test # Build + run all integration tests
- make test-quick # Smoke test only

Requirements and caveats from upstream:
- **Prerequisites**: Docker Desktop (Windows/macOS) or Docker Engine (Linux).
- This removes all HiClaw containers (Manager, Workers, docker-proxy), Docker volume, network, env file, workspace directory, and install log.
- **Prerequisites**

Basic usage or getting-started notes:
- **Resources**: 2 CPU cores + 4 GB RAM minimum. For multiple Workers, 4 cores + 8 GB recommended.
- **macOS / Linux:**
- bash

- Source: https://github.com/agentscope-ai/HiClaw
- Extracted from upstream docs: https://raw.githubusercontent.com/agentscope-ai/HiClaw/HEAD/README.md

## Documentation

- https://hiclaw.io

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coordinate-human-in-the-loop-agent-teams-in-auditable-matrix-rooms-with-hiclaw/)
