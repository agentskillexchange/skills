---
title: "Temporal CLI Workflow and Server Control"
description: "Temporal CLI is the command-line interface for running Temporal Server and interacting with workflows, activities, namespaces, and other parts of Temporal. The upstream repository describes it as both a CLI and a development server, with install paths for Homebrew, direct downloads, and Docker.nnThis skill fits developer tooling and workflow orchestration. Use it when a task requires bringing up a local Temporal environment, inspecting workflow state, or wiring automation around Temporal server operations. The repository README documents a local dev server flow, Docker invocation, and a Go build path, which makes it useful across development environments.nnFor ASE, the tool is a concrete utility, not a platform abstraction. It belongs where agents need to run, inspect, or troubleshoot Temporal-based systems. The upstream project is real, maintained, and backed by the Temporal organization. Its main job-to-be-done is to let operators and developers manage workflows from the terminal with a predictable, scriptable interface."
verification: security_reviewed
source: "https://github.com/temporalio/cli"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "temporalio/cli"
  github_stars: 350
---

# Temporal CLI Workflow and Server Control

Temporal CLI is the command-line interface for running Temporal Server and interacting with workflows, activities, namespaces, and other parts of Temporal. The upstream repository describes it as both a CLI and a development server, with install paths for Homebrew, direct downloads, and Docker.nnThis skill fits developer tooling and workflow orchestration. Use it when a task requires bringing up a local Temporal environment, inspecting workflow state, or wiring automation around Temporal server operations. The repository README documents a local dev server flow, Docker invocation, and a Go build path, which makes it useful across development environments.nnFor ASE, the tool is a concrete utility, not a platform abstraction. It belongs where agents need to run, inspect, or troubleshoot Temporal-based systems. The upstream project is real, maintained, and backed by the Temporal organization. Its main job-to-be-done is to let operators and developers manage workflows from the terminal with a predictable, scriptable interface.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/temporal-cli-workflow-server-control
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/temporal-cli-workflow-server-control` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/temporal-cli-workflow-server-control/)
