---
name: "Run agents in disposable microVM sandboxes with network allowlists and secret injection using Matchlock"
slug: "run-agents-in-disposable-microvm-sandboxes-with-network-allowlists-and-secret-injection-using-matchlock"
description: "Launch risky agent work inside disposable microVMs when you need stronger isolation, sealed egress, and host-side secret injection instead of direct host access."
github_stars: 552
verification: "security_reviewed"
source: "https://github.com/jingkaihe/matchlock"
author: "jingkaihe"
publisher_type: "individual"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "jingkaihe/matchlock"
  github_stars: 552
---

# Run agents in disposable microVM sandboxes with network allowlists and secret injection using Matchlock

Launch risky agent work inside disposable microVMs when you need stronger isolation, sealed egress, and host-side secret injection instead of direct host access.

## Prerequisites

Local shell, Matchlock CLI, virtualization support for the target host, and the agent image or command you want to run inside the microVM

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Matchlock with Homebrew using `brew tap jingkaihe/essentials && brew install matchlock`, then run `matchlock diagnose` and complete any required host setup before launching a sandboxed agent run.
```

## Documentation

- https://github.com/jingkaihe/matchlock

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agents-in-disposable-microvm-sandboxes-with-network-allowlists-and-secret-injection-using-matchlock/)
