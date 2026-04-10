---
name: Temporal CLI Workflow and Server Control
description: Temporal CLI runs a local Temporal server and talks to workflows, activities,
  and namespaces. It is the practical command-line companion for Temporal development
  and debugging.
verification: security_reviewed
source: https://github.com/temporalio/cli
category:
- Developer Tools
framework:
- Multi-Framework
---
# Temporal CLI Workflow and Server Control

Temporal CLI is the command-line interface for running Temporal Server and interacting with workflows, activities, namespaces, and other parts of Temporal. The upstream repository describes it as both a CLI and a development server, with install paths for Homebrew, direct downloads, and Docker.nnThis skill fits developer tooling and workflow orchestration. Use it when a task requires bringing up a local Temporal environment, inspecting workflow state, or wiring automation around Temporal server operations. The repository README documents a local dev server flow, Docker invocation, and a Go build path, which makes it useful across development environments.nnFor ASE, the tool is a concrete utility, not a platform abstraction. It belongs where agents need to run, inspect, or troubleshoot Temporal-based systems. The upstream project is real, maintained, and backed by the Temporal organization. Its main job-to-be-done is to let operators and developers manage workflows from the terminal with a predictable, scriptable interface.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/temporal-cli-workflow-server-control/)
