---
title: "Gate AI-generated pull requests with evidence checks and quality barriers using Swarm Orchestrator"
description: "Run Copilot, Claude Code, or Codex on isolated branches, verify each agent claim against real repo evidence, and block merges until automated quality gates pass."
verification: "security_reviewed"
source: "https://github.com/moonrunnerkc/swarm-orchestrator"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "moonrunnerkc/swarm-orchestrator"
  github_stars: 83
---

# Gate AI-generated pull requests with evidence checks and quality barriers using Swarm Orchestrator

Swarm Orchestrator is a concrete CI workflow for AI-generated code, not a generic coding-agent listing. It launches supported coding agents on isolated branches, captures transcripts, cross-checks claims like test success or commits against the real filesystem and git state, retries failures with targeted repair strategies, and only allows changes forward once verification and quality gates succeed. Use it when you want agents to produce implementation work but you do not want to trust their output blindly. This is the right fit when the job is to orchestrate parallel agent runs, inspect evidence, and gate merges with reviewable reports before code reaches the main branch. The scope boundary is the merge-governance workflow itself, not the underlying agent CLIs.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gate-ai-generated-pull-requests-with-evidence-checks-and-quality-barriers-using-swarm-orchestrator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gate-ai-generated-pull-requests-with-evidence-checks-and-quality-barriers-using-swarm-orchestrator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gate-ai-generated-pull-requests-with-evidence-checks-and-quality-barriers-using-swarm-orchestrator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-ai-generated-pull-requests-with-evidence-checks-and-quality-barriers-using-swarm-orchestrator/)
