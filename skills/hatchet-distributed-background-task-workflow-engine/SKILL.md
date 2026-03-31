---
name: "Hatchet Distributed Background Task and Workflow Engine"
description: "Hatchet is an open-source platform for running background tasks and durable workflows at scale, built on Postgres. It provides a task queue, DAG-based workflow orchestration, observability dashboard, alerting, and a CLI for managing distributed workloads across TypeScript, Python, and Go."
category: "Templates & Workflows"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/hatchet-dev/hatchet"
---
# Hatchet Distributed Background Task and Workflow Engine

Hatchet is an open-source platform for running background tasks and durable workflows at scale, built on Postgres. It provides a task queue, DAG-based workflow orchestration, observability dashboard, alerting, and a CLI for managing distributed workloads across TypeScript, Python, and Go.

## Overview

Hatchet is an open-source distributed task queue and workflow orchestration platform built on top of PostgreSQL. Created by Hatchet Dev, it bundles durable task execution, DAG-based workflow orchestration, a real-time observability dashboard, alerting, and a CLI into a single deployable platform.

What Hatchet Does

Hatchet replaces fragile combinations of Redis-backed queues (like Celery or BullMQ) with a full-featured background task management system. It handles task scheduling, retries with configurable backoff, concurrency control, rate limiting, priority queues, and chaining complex multi-step tasks into directed acyclic graph (DAG) workflows. All task state is persisted in Postgres, making tasks durable across worker restarts and failures.

Core Capabilities

The platform provides SDKs for TypeScript/Node.js, Python, and Go. Workers register task handlers that Hatchet dispatches to via gRPC streaming. Each workflow can define steps with dependencies, timeouts, retry policies, and conditional branching. The built-in web dashboard shows real-time task status, execution timelines, error details, and system metrics. Hatchet also supports cron-scheduled workflows, event-triggered execution, and webhook-based task dispatch.

Getting Started

The fastest path is the Hatchet CLI: `curl -fsSL https://install.hatchet.run/install.sh | bash && hatchet server start` (requires Docker). This spins up the full Hatchet stack locally. Alternatively, Hatchet Cloud provides a managed deployment at cloud.onhatchet.run. Self-hosting documentation is available at docs.hatchet.run covering Docker Compose, Kubernetes Helm charts, and bare-metal setups.

Agent Use Cases

For AI agents, Hatchet provides reliable background task execution for long-running operations—document processing pipelines, batch API calls, data ETL workflows, and multi-step AI inference chains. Agents can dispatch tasks to Hatchet workers, chain dependent steps into workflows, monitor execution progress through the API, and handle failures gracefully with automatic retries. The platform is particularly valuable when agents need to orchestrate work across multiple services or run tasks that outlast a single request-response cycle.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill hatchet-distributed-background-task-workflow-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill hatchet-distributed-background-task-workflow-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill hatchet-distributed-background-task-workflow-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill hatchet-distributed-background-task-workflow-engine -a codex
```

### OpenClaw

```bash
clawhub install hatchet-distributed-background-task-workflow-engine
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hatchet-distributed-background-task-workflow-engine/)
