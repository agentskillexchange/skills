---
title: "Temporal CLI Workflow and Server Control"
description: "Temporal CLI runs a local Temporal server and talks to workflows, activities, and namespaces. It is the practical command-line companion for Temporal development and debugging."
slug: "temporal-cli-workflow-server-control"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/temporalio/cli"
listed: true
---

# Temporal CLI Workflow and Server Control

Temporal CLI runs a local Temporal server and talks to workflows, activities, and namespaces. It is the practical command-line companion for Temporal development and debugging.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install temporal-cli-workflow-server-control
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Temporal CLI is the command-line interface for running Temporal Server and interacting with workflows, activities, namespaces, and other parts of Temporal. The upstream repository describes it as both a CLI and a development server, with install paths for Homebrew, direct downloads, and Docker.nnThis skill fits developer tooling and workflow orchestration. Use it when a task requires bringing up a local Temporal environment, inspecting workflow state, or wiring automation around Temporal server operations. The repository README documents a local dev server flow, Docker invocation, and a Go build path, which makes it useful across development environments.nnFor ASE, the tool is a concrete utility, not a platform abstraction. It belongs where agents need to run, inspect, or troubleshoot Temporal-based systems. The upstream project is real, maintained, and backed by the Temporal organization. Its main job-to-be-done is to let operators and developers manage workflows from the terminal with a predictable, scriptable interface.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/temporal-cli-workflow-server-control/)
