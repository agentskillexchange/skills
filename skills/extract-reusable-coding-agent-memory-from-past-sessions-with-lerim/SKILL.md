---
name: "Extract reusable coding-agent memory from past sessions with Lerim"
slug: "extract-reusable-coding-agent-memory-from-past-sessions-with-lerim"
description: "Watch Claude Code, Codex CLI, Cursor, or OpenCode sessions, extract durable project memory, and keep it locally as reusable markdown."
github_stars: 73
verification: "security_reviewed"
source: "https://github.com/lerim-dev/lerim-cli"
author: "lerim-dev"
publisher_type: "organization"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "lerim-dev/lerim-cli"
  github_stars: 73
---

# Extract reusable coding-agent memory from past sessions with Lerim

Watch Claude Code, Codex CLI, Cursor, or OpenCode sessions, extract durable project memory, and keep it locally as reusable markdown.

## Prerequisites

Python 3.10+, Docker recommended

## Installation

Use the upstream install or setup path that matches your environment:
- pip install lerim
- uv venv && source .venv/bin/activate
- uv pip install -e '.[test]'

Requirements and caveats from upstream:
- <a href="https://pypi.org/project/lerim/"><img src="https://img.shields.io/pypi/pyversions/lerim?style=flat-square" alt="Python versions"></a>
- python clean_to_lerim_jsonl.py \

Basic usage or getting-started notes:
- Instead of replaying raw traces or losing what happened after each run, Lerim keeps:
- Every run leaves a trace. Most traces are too long, too noisy, and too platform-specific for the next agent to reuse directly.
- bash

- Source: https://github.com/lerim-dev/lerim-cli
- Extracted from upstream docs: https://raw.githubusercontent.com/lerim-dev/lerim-cli/HEAD/README.md

## Documentation

- https://github.com/lerim-dev/lerim-cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-reusable-coding-agent-memory-from-past-sessions-with-lerim/)
