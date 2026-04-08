---
title: Selenium Grid Orchestrator
description: The Selenium Grid Orchestrator skill automates the deployment and management
  of Selenium Grid 4 infrastructure for distributed browser testing. It handles hub
  configuration, node registration, and session distribution across multiple browser
  types and versions. The skill configures Chrome, Firefox, and Edge nodes with specific
  resource allocation policies including max-sessions, stereotype matching, and drain
  timeouts. It supports Docker-based node scaling using Selenium Docker images with
  automatic pull and version pinning. Health monitoring tracks node availability,
  session queue depth, and test throughput metrics. The orchestrator implements smart
  session routing based on browser capability matching and node load balancing. Integration
  with TestNG and JUnit parallel execution allows test suites to scale horizontally
  across the grid. Configuration is managed through TOML files with environment variable
  overrides for CI environments.
verification: security_reviewed
source: https://agentskillexchange.com/skills/selenium-grid-orchestrator/
category:
- Browser Automation
framework:
- OpenClaw
---

# Selenium Grid Orchestrator

The Selenium Grid Orchestrator skill automates the deployment and management of Selenium Grid 4 infrastructure for distributed browser testing. It handles hub configuration, node registration, and session distribution across multiple browser types and versions. The skill configures Chrome, Firefox, and Edge nodes with specific resource allocation policies including max-sessions, stereotype matching, and drain timeouts. It supports Docker-based node scaling using Selenium Docker images with automatic pull and version pinning. Health monitoring tracks node availability, session queue depth, and test throughput metrics. The orchestrator implements smart session routing based on browser capability matching and node load balancing. Integration with TestNG and JUnit parallel execution allows test suites to scale horizontally across the grid. Configuration is managed through TOML files with environment variable overrides for CI environments.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-orchestrator/)
