---
title: "Block unsafe agent actions and scan newly added skills with AgentGuard"
description: "Add a runtime guard that evaluates agent actions, blocks dangerous commands or secret exposure, and audits new skills before they run."
verification: "security_reviewed"
source: "https://github.com/GoPlusSecurity/agentguard"
author: "GoPlusSecurity"
publisher_type: "open_source_project"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "GoPlusSecurity/agentguard"
  github_stars: 390
  npm_package: "@goplus/agentguard"
  npm_weekly_downloads: 2947
---

# Block unsafe agent actions and scan newly added skills with AgentGuard

Add a runtime guard that evaluates agent actions, blocks dangerous commands or secret exposure, and audits new skills before they run.

## Prerequisites

Node.js, supported agent runtime such as Claude Code or OpenClaw, local skill directories and agent action hooks

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with npm install @goplus/agentguard. For Claude Code, clone the repo and run ./setup.sh to install hooks, or install the skill manually from the repo. For OpenClaw, register the provided @goplus/agentguard/openclaw plugin entrypoint in plugin config.
```

## Documentation

- https://github.com/GoPlusSecurity/agentguard

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-unsafe-agent-actions-and-scan-newly-added-skills-with-agentguard/)
