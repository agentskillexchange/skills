---
title: "Run agent CLIs in a capability-based local sandbox with snapshots and controlled egress using nono"
description: "Constrain Claude Code, Codex, OpenClaw, and similar agent CLIs inside a kernel-enforced local sandbox with explicit filesystem, network, credential, and snapshot controls."
verification: "security_reviewed"
source: "https://github.com/always-further/nono"
author: "always-further"
publisher_type: "organization"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "always-further/nono"
  github_stars: 2080
---

# Run agent CLIs in a capability-based local sandbox with snapshots and controlled egress using nono

Constrain Claude Code, Codex, OpenClaw, and similar agent CLIs inside a kernel-enforced local sandbox with explicit filesystem, network, credential, and snapshot controls.

## Prerequisites

nono plus a supported local agent CLI such as Claude Code, Codex, OpenClaw, or another profiled tool.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with brew install nono, then run nono setup or the profile-specific workflow from the installation guide before starting your agent inside the sandbox.
```

## Documentation

- https://nono.sh

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agent-clis-in-a-capability-based-local-sandbox-with-snapshots-and-controlled-egress-using-nono/)
