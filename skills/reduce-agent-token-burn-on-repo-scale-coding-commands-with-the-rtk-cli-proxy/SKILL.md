---
title: "Reduce agent token burn on repo-scale coding commands with the rtk CLI proxy"
description: "Use rtk when an agent keeps wasting context on noisy shell output from large repos and you need smaller command responses before the model sees them."
verification: "security_reviewed"
source: "https://github.com/rtk-ai/rtk"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "rtk-ai/rtk"
  github_stars: 25419
---

# Reduce agent token burn on repo-scale coding commands with the rtk CLI proxy

rtk gives an agent a narrow shell-output compression workflow. It sits in front of commands like git status, git diff, grep, cat, and test runners, then filters and condenses the output before it reaches the model context. That makes it useful in repo-scale coding sessions where shell output, not reasoning, is what burns tokens. The boundary is clear enough to be skill-shaped. Invoke it when the task is shrinking noisy command output for an existing coding-agent workflow, not when the user wants a new coding agent, an IDE extension, or a general terminal replacement. The job-to-be-done is context-saving shell mediation for large-codebase work.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/reduce-agent-token-burn-on-repo-scale-coding-commands-with-the-rtk-cli-proxy/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/reduce-agent-token-burn-on-repo-scale-coding-commands-with-the-rtk-cli-proxy
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/reduce-agent-token-burn-on-repo-scale-coding-commands-with-the-rtk-cli-proxy`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reduce-agent-token-burn-on-repo-scale-coding-commands-with-the-rtk-cli-proxy/)
