---
name: "Run deterministic multi-agent coding workflows with Bernstein"
slug: "run-deterministic-multi-agent-coding-workflows-with-bernstein"
description: "Orchestrate parallel CLI coding agents in isolated git worktrees with reproducible scheduling, gates, replay journals, and optional tamper-evident audit receipts."
github_stars: 704
verification: "security_reviewed"
source: "https://github.com/sipyourdrink-ltd/bernstein"
author: "SipYourDrink Ltd / Alex Chernysh"
publisher_type: "organization"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "sipyourdrink-ltd/bernstein"
  github_stars: 704
---

# Run deterministic multi-agent coding workflows with Bernstein

Orchestrate parallel CLI coding agents in isolated git worktrees with reproducible scheduling, gates, replay journals, and optional tamper-evident audit receipts.

## Prerequisites

Python 3.12+, pipx/pip/uv/Homebrew, git, and one or more supported CLI coding agents

## Installation

Use the upstream install or setup path that matches your environment:
- pip install bernstein # pip
- uv tool install bernstein # uv
- brew tap chernistry/tap && brew install bernstein # Homebrew

Requirements and caveats from upstream:
- [![GHCR](https://img.shields.io/badge/ghcr.io-bernstein-2496ed?logo=docker&logoColor=white)](https://ghcr.io/sipyourdrink-ltd/bernstein)
- [![Python 3.12+](https://img.shields.io/badge/python-3.12+-3776ab?logo=python&logoColor=white)](https://python.org)
- | [OpenAI Agents SDK v2](https://openai.github.io/openai-agents-python/) | GPT-5, GPT-5 mini, o4 | pip install 'bernstein[openai]' |

Basic usage or getting-started notes:
- [website](https://bernstein.run) &middot; [docs](https://bernstein.readthedocs.io/) &middot; [install](docs/getting-started/install.md) &middot; [first run](docs/getting-started/first-run.md) &middot; [glossary](docs/...
- You tell Bernstein what you want built. It splits the work across several AI coding agents, runs them in parallel inside isolated git worktrees, records every handoff in the always-on lineage spine and replay journal,...
- irm https://bernstein.run/install.ps1 | iex # Windows PowerShell

- Source: https://github.com/sipyourdrink-ltd/bernstein
- Extracted from upstream docs: https://raw.githubusercontent.com/sipyourdrink-ltd/bernstein/HEAD/README.md

## Documentation

- https://bernstein.run

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-deterministic-multi-agent-coding-workflows-with-bernstein/)
