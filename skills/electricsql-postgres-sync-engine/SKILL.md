---
title: ElectricSQL Real-Time Postgres Sync Engine
description: ElectricSQL is a Postgres sync engine that solves the hard problems of
  real-time data synchronization. It provides partial replication, fan-out, and data
  delivery so developers can build fast, modern applications — from collaborative
  tools like Figma and Linear to AI agents running on live local data — without rolling
  custom sync infrastructure. At its core, Electric is a read-path sync engine. It
  watches PostgreSQL logical replication and delivers changes to clients over a low-level
  HTTP API. This architecture integrates naturally with CDNs for highly scalable data
  delivery, letting applications serve thousands of concurrent clients without custom
  WebSocket infrastructure. Partial replication is managed through Shapes, which define
  subsets of data to sync. A Shape specifies a table and optional WHERE clause, and
  Electric streams matching rows and subsequent changes to subscribed clients. This
  avoids syncing entire databases while keeping subscribed data fresh in real time.
  The sync protocol supports multiple consumption modes. The HTTP API can be consumed
  directly with cURL or any HTTP client. Official TypeScript and Elixir client libraries
  provide higher-level abstractions, and framework integrations like the useShape
  React hook make it trivial to build reactive UIs that update in real time as data
  changes in Postgres. Getting started requires a PostgreSQL database with logical
  replication enabled and an Electric service connected via DATABASE_URL. Docker Compose
  handles deployment in development, and the service is stateless — it can be horizontally
  scaled behind a load balancer. Electric reads from the Postgres WAL (Write-Ahead
  Log) and maintains its own shape log for efficient client catch-up. For AI agent
  workflows, Electric enables agents to maintain a live local replica of relevant
  data subsets. Instead of polling databases or building custom notification systems,
  agents subscribe to Shapes and receive real-time updates as data changes. This pattern
  is effective for agents that monitor data conditions, react to changes, or maintain
  local state for fast decision-making. ElectricSQL reached version 1.0 in March 2025,
  signaling production readiness. The project is open source under the Apache 2.0
  license, with an active community on Discord and regular releases on GitHub.
verification: security_reviewed
source: https://github.com/electric-sql/electric
category:
- Developer Tools
framework:
- Multi-Framework
---

# ElectricSQL Real-Time Postgres Sync Engine

ElectricSQL is a Postgres sync engine that solves the hard problems of real-time data synchronization. It provides partial replication, fan-out, and data delivery so developers can build fast, modern applications — from collaborative tools like Figma and Linear to AI agents running on live local data — without rolling custom sync infrastructure. At its core, Electric is a read-path sync engine. It watches PostgreSQL logical replication and delivers changes to clients over a low-level HTTP API. This architecture integrates naturally with CDNs for highly scalable data delivery, letting applications serve thousands of concurrent clients without custom WebSocket infrastructure. Partial replication is managed through Shapes, which define subsets of data to sync. A Shape specifies a table and optional WHERE clause, and Electric streams matching rows and subsequent changes to subscribed clients. This avoids syncing entire databases while keeping subscribed data fresh in real time. The sync protocol supports multiple consumption modes. The HTTP API can be consumed directly with cURL or any HTTP client. Official TypeScript and Elixir client libraries provide higher-level abstractions, and framework integrations like the useShape React hook make it trivial to build reactive UIs that update in real time as data changes in Postgres. Getting started requires a PostgreSQL database with logical replication enabled and an Electric service connected via DATABASE_URL. Docker Compose handles deployment in development, and the service is stateless — it can be horizontally scaled behind a load balancer. Electric reads from the Postgres WAL (Write-Ahead Log) and maintains its own shape log for efficient client catch-up. For AI agent workflows, Electric enables agents to maintain a live local replica of relevant data subsets. Instead of polling databases or building custom notification systems, agents subscribe to Shapes and receive real-time updates as data changes. This pattern is effective for agents that monitor data conditions, react to changes, or maintain local state for fast decision-making. ElectricSQL reached version 1.0 in March 2025, signaling production readiness. The project is open source under the Apache 2.0 license, with an active community on Discord and regular releases on GitHub.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/electricsql-postgres-sync-engine/)
