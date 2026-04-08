---
title: Selenium Grid Load Balancer
description: The Selenium Grid Load Balancer optimizes test distribution across multiple
  Selenium Grid 4 nodes. It queries the Grid Hub’s /status REST API endpoint to monitor
  node capacity, active sessions, and browser availability in real time. The skill
  implements a weighted round-robin algorithm that factors in node CPU usage, memory
  availability, and current session count. When a new WebDriver session is requested,
  the balancer routes it to the least-loaded node that supports the requested browser
  capability. Health checks run every 10 seconds via HTTP polling of each node’s /wd/hub/status
  endpoint, automatically removing unresponsive nodes from the rotation. The skill
  supports dynamic node registration and deregistration through the Grid’s event bus,
  scaling capacity based on queue depth. It includes configurable thresholds for max
  sessions per node, queue timeout limits, and automatic session cleanup for orphaned
  browsers. Dashboard metrics are exposed via a Prometheus /metrics endpoint for integration
  with Grafana monitoring stacks.
verification: security_reviewed
source: https://agentskillexchange.com/skills/selenium-grid-load-balancer/
category:
- Browser Automation
framework:
- Codex
---

# Selenium Grid Load Balancer

The Selenium Grid Load Balancer optimizes test distribution across multiple Selenium Grid 4 nodes. It queries the Grid Hub’s /status REST API endpoint to monitor node capacity, active sessions, and browser availability in real time. The skill implements a weighted round-robin algorithm that factors in node CPU usage, memory availability, and current session count. When a new WebDriver session is requested, the balancer routes it to the least-loaded node that supports the requested browser capability. Health checks run every 10 seconds via HTTP polling of each node’s /wd/hub/status endpoint, automatically removing unresponsive nodes from the rotation. The skill supports dynamic node registration and deregistration through the Grid’s event bus, scaling capacity based on queue depth. It includes configurable thresholds for max sessions per node, queue timeout limits, and automatic session cleanup for orphaned browsers. Dashboard metrics are exposed via a Prometheus /metrics endpoint for integration with Grafana monitoring stacks.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-load-balancer/)
