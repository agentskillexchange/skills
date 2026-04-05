---
name: "Hatchet Durable Task Queue and Workflow Engine on Postgres"
description: "Hatchet is an open-source platform for running background tasks and durable workflows at scale, built on Postgres. It provides a durable task queue, observability dashboard, alerting, and SDKs for Python, TypeScript, and Go. YC W24 backed with 6,800+ GitHub stars."
category: "Developer Tools"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/hatchet-dev/hatchet"
---
# Hatchet Durable Task Queue and Workflow Engine on Postgres

Hatchet is an open-source platform for running background tasks and durable workflows at scale, built on Postgres. It provides a durable task queue, observability dashboard, alerting, and SDKs for Python, TypeScript, and Go. YC W24 backed with 6,800+ GitHub stars.

## Overview

Hatchet is an MIT-licensed platform for running background tasks and durable workflows at scale, built on top of PostgreSQL. Backed by Y Combinator (W24) and with over 6,800 GitHub stars, Hatchet bundles a durable task queue, real-time observability dashboard, alerting, and a CLI into a single cohesive platform. It serves as a modern alternative to Celery, BullMQ, and other library-based queue systems.

Why Hatchet

Most applications start with a simple FIFO queue backed by Redis or RabbitMQ. As tasks grow in complexity — chaining operations, handling failures gracefully, managing concurrency limits — these library-based queues become difficult to debug and monitor. Hatchet addresses this by providing a full-featured task management platform with built-in support for chaining tasks into DAG workflows, automatic retries with configurable backoff, concurrency and rate limiting, and real-time failure alerting.

Multi-Language SDKs

Hatchet provides first-class SDKs for three languages. The Python SDK uses Pydantic models for type-safe task inputs. The TypeScript SDK provides fully typed task definitions. The Go SDK uses generics for compile-time safety. All three follow the same pattern: define a task function, register it on a worker, then invoke it from your application code.

Agent Integration Points

AI agents can leverage Hatchet to orchestrate complex multi-step workflows: document processing pipelines, data enrichment chains, scheduled batch jobs, and event-driven automation. The durable execution model ensures that long-running agent tasks survive crashes and are automatically retried. The observability dashboard provides visibility into task progress, making it ideal for production agent deployments.

Installation
``curl -fsSL https://install.hatchet.run/install.sh | bash
hatchet server start``

Or use the cloud version at cloud.onhatchet.run. Full documentation at docs.hatchet.run.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill hatchet-durable-task-queue-workflow-engine-postgres
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill hatchet-durable-task-queue-workflow-engine-postgres -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill hatchet-durable-task-queue-workflow-engine-postgres -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill hatchet-durable-task-queue-workflow-engine-postgres -a codex
```

### OpenClaw

```bash
clawhub install hatchet-durable-task-queue-workflow-engine-postgres
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hatchet-durable-task-queue-workflow-engine-postgres/)
