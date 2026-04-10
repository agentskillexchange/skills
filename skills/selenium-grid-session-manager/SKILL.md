---
title: "Selenium Grid Session Manager"
description: "Manages distributed browser sessions on Selenium Grid 4 via the GraphQL API and /status endpoint. Handles node scaling, session queuing, and capability matching for parallel test execution."
slug: "selenium-grid-session-manager"
category:
  - "Browser Automation"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/selenium-grid-session-manager/"
---

# Selenium Grid Session Manager

Manages distributed browser sessions on Selenium Grid 4 via the GraphQL API and /status endpoint. Handles node scaling, session queuing, and capability matching for parallel test execution.

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
clawhub install selenium-grid-session-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Selenium Grid Session Manager orchestrates distributed browser testing infrastructure using Selenium Grid 4’s modern architecture. It communicates with the Grid via the GraphQL API endpoint (/graphql) for detailed session and node information, and the /status REST endpoint for health monitoring.
The skill handles dynamic node registration and capability matching, ensuring test sessions are routed to nodes with the correct browser version, platform, and custom capabilities. It manages session queuing with configurable timeout and retry policies, preventing queue overflow during peak testing periods.
Advanced features include automatic node scaling based on queue depth (integrating with Docker API for container-based nodes), session video recording via Selenium Video docker images, and VNC live-view connections for debugging. The manager tracks session lifecycle events (created, assigned, completed, failed) and generates utilization dashboards. It supports both hub-node and fully distributed Grid architectures, with health checks that automatically drain unhealthy nodes and redistribute pending sessions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-session-manager/)
