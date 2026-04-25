---
title: "Run agent CLIs in a capability-based local sandbox with snapshots and controlled egress using nono"
description: "Constrain Claude Code, Codex, OpenClaw, and similar agent CLIs inside a kernel-enforced local sandbox with explicit filesystem, network, credential, and snapshot controls."
verification: "security_reviewed"
source: "https://github.com/always-further/nono"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "always-further/nono"
  github_stars: 2080
---

# Run agent CLIs in a capability-based local sandbox with snapshots and controlled egress using nono

nono is a skill-shaped operator tool for running agent CLIs under capability-based local confinement. It applies kernel-enforced sandbox rules, supports controlled credential injection, network filtering, verifiable audit logs, snapshots, and multiplexed agent sessions, with built-in profiles for coding-agent workflows. Invoke it when an agent should work against local code or files but must not get broad host access by default. This is a better fit than running the agent normally when you need least-privilege execution, rollback points, and explicit egress boundaries on a developer machine or CI runner. The scope boundary is secure agent execution control, not a general-purpose IDE, framework, or agent platform.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-agent-clis-in-a-capability-based-local-sandbox-with-snapshots-and-controlled-egress-using-nono/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-agent-clis-in-a-capability-based-local-sandbox-with-snapshots-and-controlled-egress-using-nono
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-agent-clis-in-a-capability-based-local-sandbox-with-snapshots-and-controlled-egress-using-nono`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agent-clis-in-a-capability-based-local-sandbox-with-snapshots-and-controlled-egress-using-nono/)
