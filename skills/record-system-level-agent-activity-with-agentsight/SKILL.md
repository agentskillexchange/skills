---
title: "Record system-level agent activity with AgentSight"
description: "Wrap Claude Code, Codex, Gemini CLI, OpenClaw, or another agent command with AgentSight to capture processes, files, network destinations, prompts, and reports."
verification: "security_reviewed"
source: "https://github.com/eunomia-bpf/agentsight"
author: "eunomia-bpf"
publisher_type: "organization"
category:
  - "Monitoring & Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "eunomia-bpf/agentsight"
  github_stars: 469
  npm_package: "@eunomia-bpf/agentsight"
  npm_weekly_downloads: 18
---

# Record system-level agent activity with AgentSight

Wrap Claude Code, Codex, Gemini CLI, OpenClaw, or another agent command with AgentSight to capture processes, files, network destinations, prompts, and reports.

## Prerequisites

Linux with eBPF support, sudo or equivalent probe permissions, Rust Cargo or AgentSight release binary, target agent CLI such as Claude Code, Codex, Gemini CLI, OpenCode, or OpenClaw

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with cargo install agentsight or download the latest release binary, verify Linux eBPF and sudo access, run sudo agentsight top for live sessions or run sudo agentsight record followed by the target agent command to capture a run, then inspect the saved session with agentsight report commands.
```

## Documentation

- https://eunomia.dev/agentsight/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/record-system-level-agent-activity-with-agentsight/)
