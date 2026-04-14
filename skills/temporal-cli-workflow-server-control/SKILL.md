---
title: "Temporal CLI Workflow and Server Control"
description: "Temporal CLI runs a local Temporal server and talks to workflows, activities, and namespaces. It is the practical command-line companion for Temporal development and debugging."
verification: security_reviewed
source: "https://github.com/temporalio/cli"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "temporalio/cli"
  github_stars: 350
---

# Temporal CLI Workflow and Server Control

Temporal CLI is the command-line interface for running Temporal Server and interacting with workflows, activities, namespaces, and other parts of Temporal. The upstream repository describes it as both a CLI and a development server, with install paths for Homebrew, direct downloads, and Docker.nnThis skill fits developer tooling and workflow orchestration. Use it when a task requires bringing up a local Temporal environment, inspecting workflow state, or wiring automation around Temporal server operations. The repository README documents a local dev server flow, Docker invocation, and a Go build path, which makes it useful across development environments.nnFor ASE, the tool is a concrete utility, not a platform abstraction. It belongs where agents need to run, inspect, or troubleshoot Temporal-based systems. The upstream project is real, maintained, and backed by the Temporal organization. Its main job-to-be-done is to let operators and developers manage workflows from the terminal with a predictable, scriptable interface.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/temporal-cli-workflow-server-control/)
