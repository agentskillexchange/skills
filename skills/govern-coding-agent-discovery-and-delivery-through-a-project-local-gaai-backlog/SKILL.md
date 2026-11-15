---
name: "Govern coding-agent discovery and delivery through a project-local GAAI backlog"
slug: "govern-coding-agent-discovery-and-delivery-through-a-project-local-gaai-backlog"
description: "Drop a `.gaai/` folder into a project so agents separate scope discovery from isolated delivery, with acceptance criteria, memory, QA gates, and daemonized execution."
github_stars: 152
verification: "security_reviewed"
source: "https://github.com/Fr-e-d/GAAI-framework"
author: "Fr-e-d"
publisher_type: "individual"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Fr-e-d/GAAI-framework"
  github_stars: 152
---

# Govern coding-agent discovery and delivery through a project-local GAAI backlog

Drop a `.gaai/` folder into a project so agents separate scope discovery from isolated delivery, with acceptance criteria, memory, QA gates, and daemonized execution.

## Prerequisites

AI coding tool, git, bash, python3; Claude Code CLI and tmux for autonomous delivery daemon

## Installation

Clone the upstream framework, then run its project installer from the repository root:

- git clone https://github.com/Fr-e-d/GAAI-framework.git /tmp/gaai
- cd /tmp/gaai
- bash .gaai/core/scripts/install.sh --target /path/to/your-project --tool claude-code --yes

The installer copies .gaai/ into the target project and deploys the appropriate tool adapter. Supported tool values documented by upstream include claude-code, cursor, windsurf, and other.

- Source: https://github.com/Fr-e-d/GAAI-framework
- Extracted from upstream docs: https://raw.githubusercontent.com/Fr-e-d/GAAI-framework/HEAD/README.md

## Documentation

- https://github.com/Fr-e-d/GAAI-framework

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/govern-coding-agent-discovery-and-delivery-through-a-project-local-gaai-backlog/)
