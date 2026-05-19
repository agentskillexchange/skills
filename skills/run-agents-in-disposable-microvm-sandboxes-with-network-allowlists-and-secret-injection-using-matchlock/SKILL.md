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

Use the upstream install or setup path that matches your environment:
- brew tap jingkaihe/essentials
- brew install matchlock
- docker save myapp:latest | matchlock image import myapp:latest # Import from tarball
- pip install matchlock

Requirements and caveats from upstream:
- matchlock run --image python:3.12-alpine \
- --allow-host "api.openai.com" python agent.py
- --secret ANTHROPIC_API_KEY@api.anthropic.com python call_api.py

Basic usage or getting-started notes:
- AI agents need to run code, but giving them unrestricted access to your machine is a risk. Matchlock lets you hand an agent a full Linux environment that boots in under a second - isolated and disposable.
- ### System Requirements
- **Linux** with KVM support

- Source: https://github.com/jingkaihe/matchlock
- Extracted from upstream docs: https://raw.githubusercontent.com/jingkaihe/matchlock/HEAD/README.md

## Documentation

- https://github.com/jingkaihe/matchlock

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agents-in-disposable-microvm-sandboxes-with-network-allowlists-and-secret-injection-using-matchlock/)
