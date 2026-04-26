---
title: "Run queued background coding sessions across GitHub, Slack, Linear, and webhooks with background-agents"
description: "Dispatch long-running coding work to background agents, check progress later, and pull reviewed outputs back into the main repo flow instead of babysitting one foreground session."
verification: "security_reviewed"
source: "https://github.com/ColeMurray/background-agents"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "ColeMurray/background-agents"
  github_stars: 1591
---

# Run queued background coding sessions across GitHub, Slack, Linear, and webhooks with background-agents

Use background-agents when the job is to hand off coding work into an asynchronous queue, let isolated agent sessions run in the background, and return later for progress, review, or pull request output. This is not just using a coding agent normally in one terminal. The bounded workflow is background delegation: spawn a coding session from GitHub, Slack, Linear, webhooks, or the web UI, let it run with its own sandbox and tooling, then inspect results and reconcile them back into the repo. That scope boundary, queued background execution and reviewable return flow, keeps this publishable as a distinct custom-agent workflow rather than a generic coding platform card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-queued-background-coding-sessions-across-github-slack-linear-and-webhooks-with-background-agents/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-queued-background-coding-sessions-across-github-slack-linear-and-webhooks-with-background-agents
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-queued-background-coding-sessions-across-github-slack-linear-and-webhooks-with-background-agents`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-queued-background-coding-sessions-across-github-slack-linear-and-webhooks-with-background-agents/)
