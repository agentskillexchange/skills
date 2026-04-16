---
title: "Selenium Grid Orchestrator"
description: "Manages Selenium Grid 4 hub and node registration for cross-browser parallel testing. Configures Chrome, Firefox, and Edge nodes with resource allocation policies."
verification: "security_reviewed"
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
---

# Selenium Grid Orchestrator

The Selenium Grid Orchestrator skill automates the deployment and management of Selenium Grid 4 infrastructure for distributed browser testing. It handles hub configuration, node registration, and session distribution across multiple browser types and versions.


The skill configures Chrome, Firefox, and Edge nodes with specific resource allocation policies including max-sessions, stereotype matching, and drain timeouts. It supports Docker-based node scaling using Selenium Docker images with automatic pull and version pinning.


Health monitoring tracks node availability, session queue depth, and test throughput metrics. The orchestrator implements smart session routing based on browser capability matching and node load balancing. Integration with TestNG and JUnit parallel execution allows test suites to scale horizontally across the grid. Configuration is managed through TOML files with environment variable overrides for CI environments.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-orchestrator/)
