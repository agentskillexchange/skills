---
title: "Run agents in disposable microVM sandboxes with network allowlists and secret injection using Matchlock"
description: "Use Matchlock when an agent must run code, install packages, and touch external APIs, but you do not want it operating directly on the host. The workflow is explicit: install Matchlock, verify host support, declare allowed hosts and secret mappings, run the agent inside a disposable microVM, and tear the environment down when the task is done. The skill boundary is concrete and narrower than a generic VM or sandbox product listing. This is about microVM-based agent execution with network allowlisting and in-flight secret injection, not general virtualization, not a broad agent framework, and not a generic container runtime card."
source: "https://github.com/jingkaihe/matchlock"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jingkaihe/matchlock"
  github_stars: 552
---

# Run agents in disposable microVM sandboxes with network allowlists and secret injection using Matchlock

Use Matchlock when an agent must run code, install packages, and touch external APIs, but you do not want it operating directly on the host. The workflow is explicit: install Matchlock, verify host support, declare allowed hosts and secret mappings, run the agent inside a disposable microVM, and tear the environment down when the task is done. The skill boundary is concrete and narrower than a generic VM or sandbox product listing. This is about microVM-based agent execution with network allowlisting and in-flight secret injection, not general virtualization, not a broad agent framework, and not a generic container runtime card.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agents-in-disposable-microvm-sandboxes-with-network-allowlists-and-secret-injection-using-matchlock/)
