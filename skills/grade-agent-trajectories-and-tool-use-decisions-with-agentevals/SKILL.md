---
title: "Grade agent trajectories and tool-use decisions with AgentEvals"
description: "Score whether an agent took a sensible intermediate path, called tools correctly, and reached the outcome without relying only on final-answer checks."
verification: "listed"
source: "https://github.com/langchain-ai/agentevals"
category:
  - "Code Quality & Review"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "langchain-ai/agentevals"
  github_stars: 550
  npm_package: "agentevals"
  npm_weekly_downloads: 251033
---

# Grade agent trajectories and tool-use decisions with AgentEvals

Use AgentEvals when you need to judge the path an agent took, not just whether the final answer looked good. The upstream package is specifically about evaluating agent trajectories, including message sequences, tool calls, graph paths, and LLM-as-judge scoring.

Invoke this instead of a general observability stack or broad eval product when the immediate job is trajectory grading inside tests or evaluation suites. The scope boundary is tight: AgentEvals evaluates agent steps and tool-use paths. It is not a general framework, hosted platform, or catch-all agent builder listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/grade-agent-trajectories-and-tool-use-decisions-with-agentevals/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grade-agent-trajectories-and-tool-use-decisions-with-agentevals
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/grade-agent-trajectories-and-tool-use-decisions-with-agentevals`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grade-agent-trajectories-and-tool-use-decisions-with-agentevals/)
