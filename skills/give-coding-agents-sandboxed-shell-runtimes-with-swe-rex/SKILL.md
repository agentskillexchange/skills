---
name: "Give coding agents sandboxed shell runtimes with SWE-ReX"
slug: "give-coding-agents-sandboxed-shell-runtimes-with-swe-rex"
description: "Use SWE-ReX when a coding agent needs a consistent runtime interface for local, containerized, or remote shell sessions with command output, exit codes, interactive tools, and parallel execution."
github_stars: 543
verification: "security_reviewed"
source: "https://github.com/SWE-agent/SWE-ReX"
author: "SWE-agent"
publisher_type: "open_source"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "SWE-agent/SWE-ReX"
  github_stars: 543
---

# Give coding agents sandboxed shell runtimes with SWE-ReX

Use SWE-ReX when a coding agent needs a consistent runtime interface for local, containerized, or remote shell sessions with command output, exit codes, interactive tools, and parallel execution.

## Prerequisites

Python, swe-rex, optional Modal or Fargate backend, local or remote shell environment

## Installation

Use the upstream install or setup path that matches your environment:
- pip install swe-rex
- pip install 'swe-rex[modal]'
- pip install 'swe-rex[fargate]'
- pip install 'swe-rex[daytona]'

Requirements and caveats from upstream:
- [![PyPI - Version](https://img.shields.io/pypi/v/swe-rex?style=for-the-badge&logo=python&logoColor=white&labelColor=black&color=deeppink)](https://pypi.org/project/swe-rex/)
- Whether commands are executed locally or remotely in Docker containers, AWS remote machines, Modal, or something else, your agent code remains the same.
- 🦖 Support a **broad range of platforms**, including non-Linux machines without Docker.

Basic usage or getting-started notes:
- SWE-ReX is a runtime interface for interacting with sandboxed shell environments, allowing you to effortlessly let your AI agent run *any command* on *any environment*.
- This is [SWE-agent][] using SWE-ReX to run on 30 [SWE-bench][] instances in parallel:

- Source: https://github.com/SWE-agent/SWE-ReX
- Extracted from upstream docs: https://raw.githubusercontent.com/SWE-agent/SWE-ReX/HEAD/README.md

## Documentation

- https://swe-rex.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-coding-agents-sandboxed-shell-runtimes-with-swe-rex/)
