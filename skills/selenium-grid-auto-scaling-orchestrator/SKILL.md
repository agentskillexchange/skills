---
title: "Selenium Grid Auto-Scaling Orchestrator"
description: "Orchestrates Selenium Grid 4 node scaling based on test queue depth using the Grid GraphQL API. Manages Docker container lifecycle for Chrome, Firefox, and Edge nodes with health monitoring."
verification: "security_reviewed"
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
tool_ecosystem:
  license: "Apache-2.0"
---

# Selenium Grid Auto-Scaling Orchestrator

The Selenium Grid Auto-Scaling Orchestrator provides intelligent scaling of Selenium Grid 4 infrastructure based on real-time test demand. It queries the Grid Status API and GraphQL endpoint to monitor session queues, node health, and resource utilization.

When queue depth exceeds configurable thresholds, the orchestrator provisions new browser nodes using the Docker Engine API, supporting Chrome (selenium/node-chrome), Firefox (selenium/node-firefox), and Edge (selenium/node-edge) images. Each node is health-checked via the /status endpoint before being registered with the Grid Hub.

Scale-down logic uses configurable idle timeouts with graceful session draining — nodes are marked as draining via the Grid Distributor API, allowing running sessions to complete before container removal. Resource limits (CPU, memory) are enforced per container using Docker cgroup constraints.

The skill includes Prometheus metrics export for node count, session duration histograms, and queue wait times. Integrates with Kubernetes HPA for cloud deployments using custom metrics from the Selenium Grid GraphQL API.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-auto-scaling-orchestrator/)
