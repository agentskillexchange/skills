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
  npm_package: "matchlock-sdk"
  npm_weekly_downloads: 1
---

# Run agents in disposable microVM sandboxes with network allowlists and secret injection using Matchlock

Launch risky agent work inside disposable microVMs when you need stronger isolation, sealed egress, and host-side secret injection instead of direct host access.

## Prerequisites

Local shell, Matchlock CLI, virtualization support for the target host, and the agent image or command you want to run inside the microVM

## Installation

Install or set up from the source-backed instructions:

Install Matchlock with Homebrew using `brew tap jingkaihe/essentials && brew install matchlock`, then run `matchlock diagnose` and complete any required host setup before launching a sandboxed agent run.

- Source: https://github.com/jingkaihe/matchlock

## Documentation

- https://github.com/jingkaihe/matchlock

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agents-in-disposable-microvm-sandboxes-with-network-allowlists-and-secret-injection-using-matchlock/)
