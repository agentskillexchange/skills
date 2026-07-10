---
name: "Temporal CLI Workflow and Server Control"
slug: "temporal-cli-workflow-server-control"
description: "Temporal CLI runs a local Temporal server and talks to workflows, activities, and namespaces. It is the practical command-line companion for Temporal development and debugging."
github_stars: 350
verification: "security_reviewed"
source: "https://github.com/temporalio/cli"
author: "Temporal"
publisher_type: "Company"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "temporalio/cli"
  github_stars: 350
---

# Temporal CLI Workflow and Server Control

Temporal CLI runs a local Temporal server and talks to workflows, activities, and namespaces. It is the practical command-line companion for Temporal development and debugging.

## Prerequisites

Go, Docker, or a downloaded Temporal binary depending on install path

## Installation

Use the upstream install or setup path that matches your environment:
- brew install temporal
- docker run --rm temporalio/temporal --help
- docker run --rm -p 7233:7233 -p 8233:8233 temporalio/temporal:latest server start-dev --ip 0.0.0.0

Requirements and caveats from upstream:
- ### Run via Docker
- [Temporal CLI on DockerHub](https://hub.docker.com/r/temporalio/temporal)

Basic usage or getting-started notes:
- Download the version for your OS and architecture:
- [Linux amd64](https://temporal.download/cli/archive/latest?platform=linux&arch=amd64)
- [Linux arm64](https://temporal.download/cli/archive/latest?platform=linux&arch=arm64)

- Source: https://github.com/temporalio/cli
- Extracted from upstream docs: https://raw.githubusercontent.com/temporalio/cli/HEAD/README.md

## Documentation

- https://github.com/temporalio/cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/temporal-cli-workflow-server-control/)
