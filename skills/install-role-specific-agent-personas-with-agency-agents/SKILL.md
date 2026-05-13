---
title: "Install role-specific agent personas with Agency Agents"
slug: "install-role-specific-agent-personas-with-agency-agents"
description: "Install and activate specialized AI agent personas from Agency Agents when a coding or operations session needs a focused role, workflow, and deliverable standard instead of a generic assistant prompt."
github_stars: 96008
verification: "security_reviewed"
source: "https://github.com/msitarzewski/agency-agents"
author: "msitarzewski"
publisher_type: "independent_open_source"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "msitarzewski/agency-agents"
  github_stars: 96008
---

# Install role-specific agent personas with Agency Agents

Install and activate specialized AI agent personas from Agency Agents when a coding or operations session needs a focused role, workflow, and deliverable standard instead of a generic assistant prompt.

## Prerequisites

Agency Agents repository, supported agent runtime (Claude Code, OpenClaw, Cursor, Gemini CLI, Aider, Windsurf, Copilot, opencode, Kimi, or Antigravity)

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone the repository, run ./scripts/convert.sh to generate integration files, then run ./scripts/install.sh or ./scripts/install.sh --tool <runtime>. For Claude Code-only use, run ./scripts/install.sh --tool claude-code or copy selected category markdown files into ~/.claude/agents/.
```

## Documentation

- https://github.com/msitarzewski/agency-agents

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-role-specific-agent-personas-with-agency-agents/)
