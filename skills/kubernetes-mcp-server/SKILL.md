---
title: Kubernetes MCP Server
description: Kubernetes MCP Server is built around Kubernetes orchestration platform.
  The underlying ecosystem is represented by kubernetes/kubernetes (121,313+ GitHub
  stars). It gives an agent a more technical and reliable way to work with the tool
  than a thin one-line wrapper, using stable interfaces like kubectl, API server,
  pods, deployments, events, logs, probes, RBAC and preserving the operational context
  that matters for real tasks. In practice, the skill gives an agent a stable interface
  to kubernetes so it can inspect state, run the right operation, and produce a result
  that fits into a larger engineering or operations pipeline. The implementation typically
  relies on kubectl, API server, pods, deployments, events, logs, probes, RBAC, with
  configuration passed through environment variables, connection strings, service
  tokens, or workspace config depending on the upstream platform. Accesses kubectl,
  API server, pods, deployments, events, logs, probes, RBAC instead of scraping a
  UI, which makes runs easier to audit and retry. Supports structured inputs and outputs
  so another tool, agent, or CI step can consume the result. Can be wired into cron
  jobs, webhook handlers, MCP transports, or local CLI workflows depending on the
  skill format. Fits into broader integration points such as cluster operations, workload
  health, scaling, and production troubleshooting. Because this is exposed as an MCP
  skill, the tool surface is designed for agent-safe, structured calls instead of
  free-form shell usage. That means models can inspect schemas, call a narrow set
  of operations, and keep context across a longer workflow without re-implementing
  credentials or connection logic on every step. Key integration points include cluster
  operations, workload health, scaling, and production troubleshooting. In a real
  environment that usually means passing credentials through env vars or app config,
  respecting rate limits and permission scopes, and returning structured artifacts
  that can be attached to tickets, pull requests, dashboards, or follow-up automations.
verification: security_reviewed
source: https://github.com/kubernetes/kubernetes
category:
- Developer Tools
framework:
- MCP
tool_ecosystem:
  github_repo: kubernetes/kubernetes
  github_stars: 121504
---

# Kubernetes MCP Server

Kubernetes MCP Server is built around Kubernetes orchestration platform. The underlying ecosystem is represented by kubernetes/kubernetes (121,313+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like kubectl, API server, pods, deployments, events, logs, probes, RBAC and preserving the operational context that matters for real tasks. In practice, the skill gives an agent a stable interface to kubernetes so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on kubectl, API server, pods, deployments, events, logs, probes, RBAC, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform. Accesses kubectl, API server, pods, deployments, events, logs, probes, RBAC instead of scraping a UI, which makes runs easier to audit and retry. Supports structured inputs and outputs so another tool, agent, or CI step can consume the result. Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format. Fits into broader integration points such as cluster operations, workload health, scaling, and production troubleshooting. Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include cluster operations, workload health, scaling, and production troubleshooting. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-mcp-server/)
