---
title: "Review risky coding-agent sessions with local action logs using Gryph"
description: "Capture and inspect file reads, writes, and shell activity from coding agents so developers can audit what actually happened after a session goes sideways."
verification: listed
source: "https://github.com/safedep/gryph"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "safedep/gryph"
  github_stars: 105
---

# Review risky coding-agent sessions with local action logs using Gryph

Use Gryph when a coding-agent session touched too much, failed unexpectedly, or needs a security review, and you want a local audit trail of file access, writes, and command execution. Invoke it instead of using the agent normally when the task is post-session review, querying, and export of agent actions across supported clients, not generic endpoint security or a broad agent platform. The boundary is the action-audit workflow itself: Gryph installs hooks, records events locally, and lets operators inspect what the agent did.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/review-risky-coding-agent-sessions-with-local-action-logs-using-gryph
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/review-risky-coding-agent-sessions-with-local-action-logs-using-gryph` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-risky-coding-agent-sessions-with-local-action-logs-using-gryph/)
