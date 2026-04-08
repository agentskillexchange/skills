---
title: Selenium Grid Auto-Scaling Orchestrator
description: The Selenium Grid Auto-Scaling Orchestrator provides intelligent scaling
  of Selenium Grid 4 infrastructure based on real-time test demand. It queries the
  Grid Status API and GraphQL endpoint to monitor session queues, node health, and
  resource utilization. When queue depth exceeds configurable thresholds, the orchestrator
  provisions new browser nodes using the Docker Engine API, supporting Chrome (selenium/node-chrome),
  Firefox (selenium/node-firefox), and Edge (selenium/node-edge) images. Each node
  is health-checked via the /status endpoint before being registered with the Grid
  Hub. Scale-down logic uses configurable idle timeouts with graceful session draining
  — nodes are marked as draining via the Grid Distributor API, allowing running sessions
  to complete before container removal. Resource limits (CPU, memory) are enforced
  per container using Docker cgroup constraints. The skill includes Prometheus metrics
  export for node count, session duration histograms, and queue wait times. Integrates
  with Kubernetes HPA for cloud deployments using custom metrics from the Selenium
  Grid GraphQL API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/selenium-grid-auto-scaling-orchestrator/
category:
- Browser Automation
framework:
- OpenClaw
---

# Selenium Grid Auto-Scaling Orchestrator

The Selenium Grid Auto-Scaling Orchestrator provides intelligent scaling of Selenium Grid 4 infrastructure based on real-time test demand. It queries the Grid Status API and GraphQL endpoint to monitor session queues, node health, and resource utilization. When queue depth exceeds configurable thresholds, the orchestrator provisions new browser nodes using the Docker Engine API, supporting Chrome (selenium/node-chrome), Firefox (selenium/node-firefox), and Edge (selenium/node-edge) images. Each node is health-checked via the /status endpoint before being registered with the Grid Hub. Scale-down logic uses configurable idle timeouts with graceful session draining — nodes are marked as draining via the Grid Distributor API, allowing running sessions to complete before container removal. Resource limits (CPU, memory) are enforced per container using Docker cgroup constraints. The skill includes Prometheus metrics export for node count, session duration histograms, and queue wait times. Integrates with Kubernetes HPA for cloud deployments using custom metrics from the Selenium Grid GraphQL API.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-auto-scaling-orchestrator/)
