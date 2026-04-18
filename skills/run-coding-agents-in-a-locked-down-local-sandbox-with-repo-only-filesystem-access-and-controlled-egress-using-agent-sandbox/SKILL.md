---
title: "Run coding agents in a locked-down local sandbox with repo-only filesystem access and controlled egress using agent-sandbox"
description: "Put Claude Code, Codex, Gemini, or other supported agent CLIs inside a persistent local sandbox instead of letting them operate directly on the host."
verification: listed
source: "https://github.com/mattolson/agent-sandbox"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mattolson/agent-sandbox"
  github_stars: 163
---

# Run coding agents in a locked-down local sandbox with repo-only filesystem access and controlled egress using agent-sandbox

Use agent-sandbox when you want local coding agents to keep their auth and state, but still confine them to a repository-scoped filesystem and a policy-controlled egress path. The workflow is concrete: initialize the sandbox, generate the compose and policy files, then enter the containerized agent environment through the CLI or devcontainer path. The scope boundary is tighter than a generic dev environment product because the point is specifically safe local agent execution with bounded filesystem and network policy.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-coding-agents-in-a-locked-down-local-sandbox-with-repo-only-filesystem-access-and-controlled-egress-using-agent-sandbox
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/run-coding-agents-in-a-locked-down-local-sandbox-with-repo-only-filesystem-access-and-controlled-egress-using-agent-sandbox` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-coding-agents-in-a-locked-down-local-sandbox-with-repo-only-filesystem-access-and-controlled-egress-using-agent-sandbox/)
