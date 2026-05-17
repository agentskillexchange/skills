---
name: "Coordinate persistent Copilot agent teams with Squad"
slug: "coordinate-persistent-copilot-agent-teams-with-squad"
description: "Use Squad to create human-directed specialist agents that persist in a repository, share decisions through files, and help coordinate implementation, testing, and review work in GitHub Copilot."
github_stars: 2518
verification: "security_reviewed"
source: "https://github.com/bradygaster/squad"
author: "Brady Gaster"
publisher_type: "independent_open_source"
category: "Templates & Workflows"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "bradygaster/squad"
  github_stars: 2518
  npm_package: "@bradygaster/squad-cli"
  npm_weekly_downloads: 0
---

# Coordinate persistent Copilot agent teams with Squad

Use Squad to create human-directed specialist agents that persist in a repository, share decisions through files, and help coordinate implementation, testing, and review work in GitHub Copilot.

## Prerequisites

Node/npm; Squad CLI; GitHub CLI authentication; GitHub Copilot agent mode

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run npm install -g @bradygaster/squad-cli, run squad init in a git repository, authenticate with gh auth login, then invoke the Squad agent in GitHub Copilot and approve the proposed team.
```

## Documentation

- https://bradygaster.github.io/squad/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coordinate-persistent-copilot-agent-teams-with-squad/)
