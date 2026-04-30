---
title: "Diagnose Tailscale and proxy conflicts before remote development stalls out"
description: "Use tunnel-doctor in Claude Code when Tailscale partially works but SSH, browser, git, or Docker paths fail because proxy, route, or double-tunneling conflicts need a structured diagnosis."
verification: "security_reviewed"
source: "https://github.com/daymade/claude-code-skills/blob/main/tunnel-doctor/SKILL.md"
author: "daymade"
publisher_type: "github_skill"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
---

# Diagnose Tailscale and proxy conflicts before remote development stalls out

Use tunnel-doctor in Claude Code when Tailscale partially works but SSH, browser, git, or Docker paths fail because proxy, route, or double-tunneling conflicts need a structured diagnosis.

## Prerequisites

Read, Grep, Edit, Bash

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the tunnel-doctor skill from daymade/claude-code-skills into Claude Code, then invoke it when Tailscale and proxy or VPN layers coexist on macOS and remote development paths fail inconsistently.
```

## Documentation

- https://github.com/daymade/claude-code-skills/blob/main/tunnel-doctor/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-tailscale-and-proxy-conflicts-before-remote-development-stalls-out/)
