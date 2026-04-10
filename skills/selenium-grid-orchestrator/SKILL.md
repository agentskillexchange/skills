---
title: "Selenium Grid Orchestrator"
description: "Manages Selenium Grid 4 hub and node registration for cross-browser parallel testing. Configures Chrome, Firefox, and Edge nodes with resource allocation policies."
slug: "selenium-grid-orchestrator"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/selenium-grid-orchestrator/"
listed: true
---

# Selenium Grid Orchestrator

Manages Selenium Grid 4 hub and node registration for cross-browser parallel testing. Configures Chrome, Firefox, and Edge nodes with resource allocation policies.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install selenium-grid-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Selenium Grid Orchestrator skill automates the deployment and management of Selenium Grid 4 infrastructure for distributed browser testing. It handles hub configuration, node registration, and session distribution across multiple browser types and versions.
The skill configures Chrome, Firefox, and Edge nodes with specific resource allocation policies including max-sessions, stereotype matching, and drain timeouts. It supports Docker-based node scaling using Selenium Docker images with automatic pull and version pinning.
Health monitoring tracks node availability, session queue depth, and test throughput metrics. The orchestrator implements smart session routing based on browser capability matching and node load balancing. Integration with TestNG and JUnit parallel execution allows test suites to scale horizontally across the grid. Configuration is managed through TOML files with environment variable overrides for CI environments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-orchestrator/)
