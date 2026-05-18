---
name: "Coordinate multiple CLI agents through sessions, handoffs, and terminal control APIs with CLI Agent Orchestrator"
slug: "coordinate-multiple-cli-agents-through-sessions-handoffs-and-terminal-control-apis-with-cli-agent-orchestrator"
description: "Lets an agent supervisor spawn and steer isolated terminal-based worker agents with explicit handoff, assign, and message patterns."
github_stars: 473
verification: "listed"
source: "https://github.com/awslabs/cli-agent-orchestrator"
author: "AWS Labs"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "awslabs/cli-agent-orchestrator"
  github_stars: 473
---

# Coordinate multiple CLI agents through sessions, handoffs, and terminal control APIs with CLI Agent Orchestrator

Lets an agent supervisor spawn and steer isolated terminal-based worker agents with explicit handoff, assign, and message patterns.

## Prerequisites

Python 3.10+, tmux 3.3+, uv, supported CLI developer agents

## Installation

Use the upstream install or setup path that matches your environment:
- brew install python@3.12
- ### 3. Install uv
- uv tool install git+https://github.com/awslabs/cli-agent-orchestrator.git@main --upgrade
- uv tool install cli-agent-orchestrator --upgrade

Requirements and caveats from upstream:
- [![Python versions](https://img.shields.io/pypi/pyversions/cli-agent-orchestrator.svg)](https://pypi.org/project/cli-agent-orchestrator/)
- **Python 3.10 or higher** — see [pyproject.toml](pyproject.toml)
- **[uv](https://docs.astral.sh/uv/)** — fast Python package installer and virtual environment manager

Basic usage or getting-started notes:
- **Headless agent execution in CI** — cao launch --headless --async to run tasks unattended.
- **Cross-provider mixing** — run workers on different CLIs in the same session. Pin a profile to a provider via agent frontmatter. See [Cross-Provider Orchestration](#cross-provider-orchestration).
- **curl** and **git** — for downloading installers and cloning the repo

- Source: https://github.com/awslabs/cli-agent-orchestrator
- Extracted from upstream docs: https://raw.githubusercontent.com/awslabs/cli-agent-orchestrator/HEAD/README.md

## Documentation

- https://github.com/awslabs/cli-agent-orchestrator

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coordinate-multiple-cli-agents-through-sessions-handoffs-and-terminal-control-apis-with-cli-agent-orchestrator/)
