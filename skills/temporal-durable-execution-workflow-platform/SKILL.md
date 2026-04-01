---
name: "Temporal Durable Execution Workflow Orchestration Platform"
description: "Temporal is an open-source durable execution platform that lets developers build scalable, fault-tolerant workflows. It automatically handles retries, timeouts, and intermittent failures, with SDKs for Go, Java, Python, TypeScript, .NET, and PHP."
category: "Templates & Workflows"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/temporalio/temporal"
---
# Temporal Durable Execution Workflow Orchestration Platform

Temporal is an open-source durable execution platform that lets developers build scalable, fault-tolerant workflows. It automatically handles retries, timeouts, and intermittent failures, with SDKs for Go, Java, Python, TypeScript, .NET, and PHP.

## Overview

Overview

Temporal is a durable execution platform that enables developers to build scalable applications without sacrificing productivity or reliability. The Temporal server executes units of application logic called Workflows in a resilient manner, automatically handling intermittent failures and retrying failed operations. It originated as a fork of Uber’s Cadence and is developed by Temporal Technologies.

Core Concepts

Temporal’s programming model centers on Workflows (reliable, long-running functions), Activities (individual units of work that can fail), Workers (processes that execute Workflow and Activity code), and Signals/Queries (ways to interact with running Workflows). Workflows maintain their state through event sourcing, surviving process crashes and server restarts without data loss.

Key Capabilities

Temporal provides durable timers (sleep for days without consuming resources), automatic retry policies with configurable backoff, saga patterns for distributed transactions, cron and scheduled workflows, child workflow orchestration, versioning for safe code updates, and visibility APIs for monitoring workflow state. It handles the hardest distributed systems problems so developers can focus on business logic.

Agent Integration

For AI agents, Temporal excels at orchestrating multi-step workflows that involve external API calls, human-in-the-loop approvals, long-running data processing, and complex branching logic. Agents can trigger Temporal workflows via SDK or REST API, monitor execution state, and handle failures gracefully. The TypeScript and Python SDKs integrate well with LLM agent frameworks for building reliable AI pipelines.

Architecture

The Temporal server consists of a frontend service, history service, matching service, and worker service, backed by a persistence layer (Cassandra, MySQL, or PostgreSQL). It includes a Web UI for visualizing workflow executions and a CLI (`temporal`) for administration. Deployment options include single binary for development, Docker Compose, Kubernetes with Helm charts, or Temporal Cloud (managed service).

Installation
``brew install temporal
temporal server start-dev``

Or with Docker: `docker compose up` from the temporalio/docker-compose repository.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill temporal-durable-execution-workflow-platform
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill temporal-durable-execution-workflow-platform -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill temporal-durable-execution-workflow-platform -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill temporal-durable-execution-workflow-platform -a codex
```

### OpenClaw

```bash
clawhub install temporal-durable-execution-workflow-platform
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/temporal-durable-execution-workflow-platform/)
