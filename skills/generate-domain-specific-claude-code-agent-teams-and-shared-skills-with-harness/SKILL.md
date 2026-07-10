---
title: "Generate domain-specific Claude Code agent teams and shared skills with Harness"
description: "Turn a project description into a Claude Code team architecture with generated agents, shared skills, and orchestration patterns instead of hand-designing the whole setup."
verification: "security_reviewed"
source: "https://github.com/revfactory/harness"
author: "revfactory"
publisher_type: "organization"
category:
  - "Templates & Workflows"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "revfactory/harness"
  github_stars: 2807
---

# Generate domain-specific Claude Code agent teams and shared skills with Harness

Turn a project description into a Claude Code team architecture with generated agents, shared skills, and orchestration patterns instead of hand-designing the whole setup.

## Prerequisites

Claude Code, Harness plugin or copied skill files, a project or domain description to turn into agent-team definitions

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the Harness Claude Code plugin from the repository instructions or copy the skill files into ~/.claude/skills/harness, then invoke the documented prompts such as 'build a harness for this project' to generate .claude/agents and .claude/skills for the target domain.
```

## Documentation

- https://github.com/revfactory/harness#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-domain-specific-claude-code-agent-teams-and-shared-skills-with-harness/)
