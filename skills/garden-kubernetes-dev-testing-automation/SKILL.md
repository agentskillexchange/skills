---
name: "Garden Kubernetes Development and Testing Automation Platform"
description: "Garden is a DevOps automation tool for developing and testing Kubernetes apps faster. It spins up production-like environments on demand, provides smart build caching with parallel execution, and uses a unified YAML configuration across development, testing, and CI stages."
category: "CI/CD Integrations"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/garden-io/garden"
---
# Garden Kubernetes Development and Testing Automation Platform

Garden is a DevOps automation tool for developing and testing Kubernetes apps faster. It spins up production-like environments on demand, provides smart build caching with parallel execution, and uses a unified YAML configuration across development, testing, and CI stages.

## Overview

Garden is an open-source DevOps automation platform by Garden.io designed to streamline Kubernetes application development and testing. Licensed under MPL-2.0 and written primarily in TypeScript, Garden provides a declarative configuration framework that codifies complete stack descriptions, enabling reproducible and portable workflows across developer machines and CI environments.

Core Capabilities

Garden allows teams to spin up production-like environments for development, testing, and CI on demand using a single `garden.yml` configuration format. The tool builds a directed acyclic graph (DAG) of build and deploy dependencies, automatically executing independent steps in parallel while caching results for future reuse. This graph-based approach means only the minimum required steps execute when changes are detected, based on individual file hashes.

Configuration and Workflow

Garden configurations define four core action types: Build, Deploy, Test, and Run. These are composed using simple YAML with explicit dependency declarations. A typical workflow includes container builds, Helm chart deployments, Kubernetes manifest applications, and integration test execution. The `garden deploy` command handles the full build-deploy cycle, while `garden test` runs the test suite, and `garden dev` starts an interactive development console.

Sync Mode and Live Reloading

Garden includes a sync mode (`garden deploy --sync`) that live-reloads changes to running services, providing fast feedback during development without requiring full rebuild cycles. This makes the inner development loop nearly as fast as local development while running against real Kubernetes infrastructure.

Plugin Ecosystem

Garden is pluggable with action execution depending on configured plugins. The Kubernetes plugin handles container builds and Kubernetes deployments. The Terraform plugin manages infrastructure provisioning alongside application deployment. The Pulumi plugin provides an alternative infrastructure-as-code integration. This plugin architecture means Garden can orchestrate heterogeneous stacks spanning containers, serverless functions, and infrastructure resources.

Agent Integration

AI agents can leverage Garden’s CLI to automate environment provisioning for testing, spin up preview environments from pull requests (`garden deploy --env preview`), run integration test suites against isolated environments, and manage the full lifecycle of Kubernetes-based applications. The declarative YAML configuration makes it straightforward for agents to generate and modify Garden configs programmatically, while the smart caching ensures agents don’t waste time on redundant builds.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill garden-kubernetes-dev-testing-automation
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill garden-kubernetes-dev-testing-automation -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill garden-kubernetes-dev-testing-automation -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill garden-kubernetes-dev-testing-automation -a codex
```

### OpenClaw

```bash
clawhub install garden-kubernetes-dev-testing-automation
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/garden-kubernetes-dev-testing-automation/)
