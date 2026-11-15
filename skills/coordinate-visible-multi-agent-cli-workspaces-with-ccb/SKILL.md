---
name: "Coordinate visible multi-agent CLI workspaces with CCB"
slug: "coordinate-visible-multi-agent-cli-workspaces-with-ccb"
description: "Use CCB to run Codex, Claude, Gemini, Cursor, OpenCode, and other CLI agents in a visible project workspace with configured panes, shared memory, role packs, and human takeover."
github_stars: 3237
verification: "security_reviewed"
source: "https://github.com/SeemSeam/claude_codex_bridge"
author: "SeemSeam contributors"
publisher_type: "open_source"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "SeemSeam/claude_codex_bridge"
  github_stars: 3237
  npm_package: "@seemseam/ccb"
  npm_weekly_downloads: 9851
---

# Coordinate visible multi-agent CLI workspaces with CCB

Use CCB to run Codex, Claude, Gemini, Cursor, OpenCode, and other CLI agents in a visible project workspace with configured panes, shared memory, role packs, and human takeover.

## Prerequisites

CCB CLI, one or more supported local CLI agents such as Codex, Claude, Gemini, Cursor, OpenCode, or Copilot, optional mobile controller

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g @seemseam/ccb
- git clone https://github.com/SeemSeam/claude_codex_bridge.git

Requirements and caveats from upstream:
- Reused managed Python environments now refresh legacy pip versions for system certificate support and opt into truststore only when its backend is available.
- macOS release updates preserve healthy managed Python environments and retry watchdog installation through a configurable mirror after TLS or network failures.
- Release artifacts now include the optional Rust ccb-runtime-accelerator; installed Codex agents no longer silently fall back to the Python hot path when the sidecar is expected.

Basic usage or getting-started notes:
- [Quick Start](#quick-start) · [Mobile App](#mobile-app) · [Rich Mode](#rich-mode) · [Configure Agents](#configure-agents) · [User Guide](docs/manuals/user-guide/) · [Developer Guide](docs/manuals/developer-guide/)
- Hub capability: run multiple CLI providers concurrently from one command.
- After CCB is installed, use CCB's updater:

- Source: https://github.com/SeemSeam/claude_codex_bridge
- Extracted from upstream docs: https://raw.githubusercontent.com/SeemSeam/claude_codex_bridge/HEAD/README.md

## Documentation

- https://github.com/SeemSeam/claude_codex_bridge

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coordinate-visible-multi-agent-cli-workspaces-with-ccb/)
