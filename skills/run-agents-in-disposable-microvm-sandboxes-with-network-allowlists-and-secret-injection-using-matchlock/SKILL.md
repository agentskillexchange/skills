---
title: "Run agents in disposable microVM sandboxes with network allowlists and secret injection using Matchlock"
description: "Launch risky agent work inside disposable microVMs when you need stronger isolation, sealed egress, and host-side secret injection instead of direct host access."
verification: "listed"
source: "https://github.com/jingkaihe/matchlock"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jingkaihe/matchlock"
  github_stars: 552
---

# Run agents in disposable microVM sandboxes with network allowlists and secret injection using Matchlock

Use Matchlock when an agent must run code, install packages, and touch external APIs, but you do not want it operating directly on the host. The workflow is explicit: install Matchlock, verify host support, declare allowed hosts and secret mappings, run the agent inside a disposable microVM, and tear the environment down when the task is done.

The skill boundary is concrete and narrower than a generic VM or sandbox product listing. This is about microVM-based agent execution with network allowlisting and in-flight secret injection, not general virtualization, not a broad agent framework, and not a generic container runtime card.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agents-in-disposable-microvm-sandboxes-with-network-allowlists-and-secret-injection-using-matchlock/)
