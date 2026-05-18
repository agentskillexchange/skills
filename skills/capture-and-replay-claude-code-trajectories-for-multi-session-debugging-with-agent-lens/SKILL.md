---
name: "Capture and replay Claude Code trajectories for multi-session debugging with Agent Lens"
slug: "capture-and-replay-claude-code-trajectories-for-multi-session-debugging-with-agent-lens"
description: "Record structured Claude Code trajectories, shadow git diffs, and replay branches when agent behavior needs forensic debugging instead of ad hoc transcript review."
github_stars: 102
verification: "listed"
source: "https://github.com/dreadnode/agent-lens"
author: "Dreadnode"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "dreadnode/agent-lens"
  github_stars: 102
---

# Capture and replay Claude Code trajectories for multi-session debugging with Agent Lens

Record structured Claude Code trajectories, shadow git diffs, and replay branches when agent behavior needs forensic debugging instead of ad hoc transcript review.

## Prerequisites

Python 3.12+, uv, Agent Lens, and Claude Code access through a subscription or API key compatible with the Claude Agent SDK

## Installation

Use the upstream install or setup path that matches your environment:
- git clone <this-repo>
- uv sync
- npm install
- npm run dev

Requirements and caveats from upstream:
- Requires Python >= 3.12 and [uv](https://docs.astral.sh/uv/).
- With provider: anthropic (the default), if no ANTHROPIC_API_KEY is set, the SDK falls back to your Claude Code subscription credentials from ~/.claude/credentials.json (requires Claude Pro/Max). Usage is covered by yo...
- You are exploring a Python codebase. Use MEMORY.md to keep notes.

Basic usage or getting-started notes:
- **Note:** AgentLens currently supports Claude Code via the Claude Agent SDK. Support for additional agents and frameworks is planned — see [Roadmap](#roadmap). Some features (especially turn-level replay) are experime...
- ![Run list](docs/assets/run-list.png)
- bash

- Source: https://github.com/dreadnode/agent-lens
- Extracted from upstream docs: https://raw.githubusercontent.com/dreadnode/agent-lens/HEAD/README.md

## Documentation

- https://dreadnode.github.io/agent-lens/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-and-replay-claude-code-trajectories-for-multi-session-debugging-with-agent-lens/)
