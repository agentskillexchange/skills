---
title: "Orchestrate goal-driven TypeScript agent teams with Open Multi Agent"
slug: "orchestrate-goal-driven-typescript-agent-teams-with-open-multi-agent"
description: "Turn a user goal into a planned multi-agent task DAG, execute independent tasks in parallel, and trace the run from a TypeScript backend."
github_stars: 6088
verification: "security_reviewed"
source: "https://github.com/open-multi-agent/open-multi-agent"
author: "open-multi-agent"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "open-multi-agent/open-multi-agent"
  github_stars: 6088
  npm_package: "@open-multi-agent/core"
  npm_weekly_downloads: 0
---

# Orchestrate goal-driven TypeScript agent teams with Open Multi Agent

Turn a user goal into a planned multi-agent task DAG, execute independent tasks in parallel, and trace the run from a TypeScript backend.

## Prerequisites

Node.js >= 18, npm, API keys for selected model providers or local model provider, optional MCP servers

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `npm install @open-multi-agent/core`, define AgentConfig entries for the team, create an OpenMultiAgent orchestrator, then call `runTeam(team, goal)` or `runTasks()` from a TypeScript backend or run examples with `npx tsx examples/<path>.ts`.
```

## Documentation

- https://github.com/open-multi-agent/open-multi-agent

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/orchestrate-goal-driven-typescript-agent-teams-with-open-multi-agent/)
