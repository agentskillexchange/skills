---
title: "BullMQ Redis-Based Message Queue and Job Processor for Node.js"
description: "BullMQ is the fastest, most reliable Redis-based distributed queue for Node.js, Python, Elixir, and PHP. It provides priority queues, rate limiting, delayed jobs, parent-child dependencies, repeatable jobs, and sandboxed workers for background processing at scale."
verification: "security_reviewed"
source: "https://github.com/taskforcesh/bullmq"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "taskforcesh/bullmq"
  github_stars: 8714
---

# BullMQ Redis-Based Message Queue and Job Processor for Node.js

BullMQ is a high-performance message queue and batch processing library built on Redis, designed for Node.js with additional support for Python, Elixir, and PHP. Originally created by Taskforce.sh, it has become the standard Redis-based job queue in the Node.js ecosystem, used by organizations including Microsoft, NocoDB, Novu, Infisical, and Langfuse.


Queue Architecture
BullMQ uses Redis as its backing store with carefully designed Lua scripts for atomic operations, ensuring rock-solid reliability even under high concurrency. Jobs are added to named queues and processed by workers that can run in separate processes or machines. The library supports multiple queue patterns including FIFO, LIFO, priority-based, and rate-limited processing.


Job Processing Features
The library provides a comprehensive set of job processing capabilities: priority queues for ordering execution, delayed jobs that fire after a specified time, repeatable jobs with cron-like scheduling, configurable concurrency per worker, automatic retries with exponential backoff, job deduplication through both debouncing and throttling, and sandboxed workers that run in separate processes for isolation.


Flow Processing
BullMQ supports parent-child job dependencies through its FlowProducer API. This enables building complex workflow DAGs where child jobs must complete before their parent begins processing. Jobs can be organized into hierarchical trees with grandchild relationships, enabling sophisticated multi-step processing pipelines.


Event System and Monitoring
The QueueEvents class provides real-time event streaming for job lifecycle tracking including completion, failure, progress updates, and state transitions. The companion Taskforce.sh dashboard offers a professional web UI for queue monitoring, job inspection, search, retry operations, and metrics visualization.


Agent Integration
AI agents can leverage BullMQ to offload long-running tasks to background workers, implement reliable webhook processing, build multi-step pipelines with dependency management, and schedule recurring maintenance jobs. The npm package installs with a single command and requires only a Redis connection to get started.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bullmq-redis-message-queue-job-processor-nodejs/)
