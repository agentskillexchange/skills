---
title: "Diagnose Tailscale and proxy conflicts before remote development stalls out"
description: "Use tunnel-doctor in Claude Code when Tailscale partially works but SSH, browser, git, or Docker paths fail because proxy, route, or double-tunneling conflicts need a structured diagnosis."
verification: "listed"
source: "https://github.com/daymade/claude-code-skills/blob/main/tunnel-doctor/SKILL.md"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Code"
---

# Diagnose Tailscale and proxy conflicts before remote development stalls out

Use tunnel-doctor in Claude Code when Tailscale partially works but SSH, browser, git, or Docker paths fail because proxy, route, or double-tunneling conflicts need a structured diagnosis.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-tailscale-and-proxy-conflicts-before-remote-development-stalls-out/)
