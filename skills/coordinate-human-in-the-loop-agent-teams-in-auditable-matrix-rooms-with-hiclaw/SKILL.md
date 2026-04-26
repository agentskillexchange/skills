---
title: "Coordinate human-in-the-loop agent teams in auditable Matrix rooms with HiClaw"
description: "Run manager-worker agent collaboration in Matrix rooms where humans can watch, intervene, and keep credentials out of worker hands."
verification: "security_reviewed"
source: "https://github.com/agentscope-ai/HiClaw"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "agentscope-ai/HiClaw"
  github_stars: 4231
---

# Coordinate human-in-the-loop agent teams in auditable Matrix rooms with HiClaw

HiClaw is a manager-worker collaboration system for running multiple agents inside Matrix rooms with full human visibility and intervention. Use this when a task needs auditable handoffs, live supervision, and secure worker isolation across several agents, not when you just want to chat with one agent or adopt a general-purpose SDK. The scope boundary here is specific: this skill is about coordinating multi-agent work through transparent Matrix-room workflows and human checkpoints, rather than listing HiClaw as a broad agent platform.

What the agent actually does:

– Creates a Manager/Worker collaboration pattern for complex tasks

– Routes agent work through Matrix rooms that humans can inspect in real time

– Keeps real credentials behind the gateway so workers do not hold API keys or PATs

– Lets operators step into rooms, correct behavior, and supervise execution

When to invoke it:

– You need several agents to collaborate on one task with visible handoffs

– You need human-in-the-loop review without losing chat history or coordination context

– You want room-based collaboration and secure credential pass-through instead of opaque agent-to-agent orchestration

Why this is skill-shaped instead of a product card:

– The publishable unit is the auditable Matrix-room coordination workflow

– The user-facing job is operating supervised multi-agent task rooms, not ‘install a platform’

– The upstream docs repeatedly center Matrix, manager-worker decomposition, human supervision, and credential isolation as the invocation shape

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/coordinate-human-in-the-loop-agent-teams-in-auditable-matrix-rooms-with-hiclaw/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/coordinate-human-in-the-loop-agent-teams-in-auditable-matrix-rooms-with-hiclaw
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/coordinate-human-in-the-loop-agent-teams-in-auditable-matrix-rooms-with-hiclaw`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coordinate-human-in-the-loop-agent-teams-in-auditable-matrix-rooms-with-hiclaw/)
