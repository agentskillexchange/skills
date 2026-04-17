---
title: "Capture and replay Claude Code trajectories for multi-session debugging with Agent Lens"
description: "Use Agent Lens when the job is to run or inspect Claude Code sessions as structured trajectories, then replay or resample them to understand what went wrong. The workflow is specific: define a multi-session run in YAML, execute it through the harness, inspect ATIF outputs and file-state diffs, and replay branch points or resample turns during debugging or research.\nThe scope boundary is sharp enough for ASE. This is not a generic observability platform or a generic Claude product listing. It is a bounded trajectory-capture and replay workflow for Claude Code via the Claude Agent SDK, aimed at debugging, safety analysis, and behavior inspection."
verification: listed
source: "https://github.com/dreadnode/agent-lens"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "dreadnode/agent-lens"
  github_stars: 102
---

# Capture and replay Claude Code trajectories for multi-session debugging with Agent Lens

Use Agent Lens when the job is to run or inspect Claude Code sessions as structured trajectories, then replay or resample them to understand what went wrong. The workflow is specific: define a multi-session run in YAML, execute it through the harness, inspect ATIF outputs and file-state diffs, and replay branch points or resample turns during debugging or research.
The scope boundary is sharp enough for ASE. This is not a generic observability platform or a generic Claude product listing. It is a bounded trajectory-capture and replay workflow for Claude Code via the Claude Agent SDK, aimed at debugging, safety analysis, and behavior inspection.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/capture-and-replay-claude-code-trajectories-for-multi-session-debugging-with-agent-lens
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/capture-and-replay-claude-code-trajectories-for-multi-session-debugging-with-agent-lens` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-and-replay-claude-code-trajectories-for-multi-session-debugging-with-agent-lens/)
