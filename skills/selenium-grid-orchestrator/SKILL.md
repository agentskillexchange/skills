---
name: "Selenium Grid Orchestrator"
description: "Manages Selenium Grid 4 hub and node registration for cross-browser parallel testing. Configures Chrome, Firefox, and Edge nodes with resource allocation policies."
category: "Browser Automation"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/selenium-grid-orchestrator/"
---
# Selenium Grid Orchestrator

Manages Selenium Grid 4 hub and node registration for cross-browser parallel testing. Configures Chrome, Firefox, and Edge nodes with resource allocation policies.

## Overview

The Selenium Grid Orchestrator skill automates the deployment and management of Selenium Grid 4 infrastructure for distributed browser testing. It handles hub configuration, node registration, and session distribution across multiple browser types and versions.

The skill configures Chrome, Firefox, and Edge nodes with specific resource allocation policies including max-sessions, stereotype matching, and drain timeouts. It supports Docker-based node scaling using Selenium Docker images with automatic pull and version pinning.

Health monitoring tracks node availability, session queue depth, and test throughput metrics. The orchestrator implements smart session routing based on browser capability matching and node load balancing. Integration with TestNG and JUnit parallel execution allows test suites to scale horizontally across the grid. Configuration is managed through TOML files with environment variable overrides for CI environments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install selenium-grid-orchestrator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-orchestrator/)
