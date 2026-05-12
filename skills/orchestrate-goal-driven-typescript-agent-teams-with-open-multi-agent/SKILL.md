---
title: "Orchestrate goal-driven TypeScript agent teams with Open Multi Agent"
slug: "orchestrate-goal-driven-typescript-agent-teams-with-open-multi-agent"
description: "Turn a user goal into a planned multi-agent task DAG, execute independent tasks in parallel, and trace the run from a TypeScript backend."
verification: "listed"
source: "https://github.com/open-multi-agent/open-multi-agent"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "open-multi-agent/open-multi-agent"
  github_stars: 6088
  npm_package: "@open-multi-agent/core"
---

# Orchestrate goal-driven TypeScript agent teams with Open Multi Agent

Use Open Multi Agent when an operator needs a backend agent team to decompose a goal into a task DAG, assign work to specialized agents, run independent tasks in parallel, and synthesize a final result with progress and trace visibility. This is useful for repeatable engineering or analysis workflows such as code generation, contract review, meeting summarization, competitive monitoring, and other jobs where the agent should plan and coordinate multiple roles rather than answer in a single chat turn.

Invoke it instead of using a normal product UI when the workflow belongs inside a Node.js/TypeScript service or CLI and needs explicit teams, provider selection, tools, optional MCP connections, structured output, shared memory, and observable execution.

## Prerequisites

- Node.js >= 18
- npm
- API keys for selected model providers or local model provider
- Optional: MCP servers

## Installation

```bash
npm install @open-multi-agent/core
```

Define `AgentConfig` entries for the team, create an `OpenMultiAgent` orchestrator, then call `runTeam(team, goal)` or `runTasks()` from a TypeScript backend, or run examples with `npx tsx examples/<path>.ts`.

## Source

- [open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent)
- [Agent Skill Exchange](https://agentskillexchange.com/skills/orchestrate-goal-driven-typescript-agent-teams-with-open-multi-agent/)
