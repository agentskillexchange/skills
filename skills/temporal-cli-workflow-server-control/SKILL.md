---
title: "Temporal CLI Workflow and Server Control"
description: "Temporal CLI runs a local Temporal server and talks to workflows, activities, and namespaces. It is the practical command-line companion for Temporal development and debugging."
verification: "security_reviewed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/temporal-cli-workflow-server-control/)
