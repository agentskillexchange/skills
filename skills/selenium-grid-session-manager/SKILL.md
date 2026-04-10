---
name: Selenium Grid Session Manager
description: Manages distributed browser sessions on Selenium Grid 4 via the GraphQL
  API and /status endpoint. Handles node scaling, session queuing, and capability
  matching for parallel test execution.
verification: security_reviewed
source: https://agentskillexchange.com/skills/selenium-grid-session-manager/
category:
- Browser Automation
framework:
- Gemini
---
# Selenium Grid Session Manager

The Selenium Grid Session Manager orchestrates distributed browser testing infrastructure using Selenium Grid 4's modern architecture. It communicates with the Grid via the GraphQL API endpoint (/graphql) for detailed session and node information, and the /status REST endpoint for health monitoring.
The skill handles dynamic node registration and capability matching, ensuring test sessions are routed to nodes with the correct browser version, platform, and custom capabilities. It manages session queuing with configurable timeout and retry policies, preventing queue overflow during peak testing periods.
Advanced features include automatic node scaling based on queue depth (integrating with Docker API for container-based nodes), session video recording via Selenium Video docker images, and VNC live-view connections for debugging. The manager tracks session lifecycle events (created, assigned, completed, failed) and generates utilization dashboards. It supports both hub-node and fully distributed Grid architectures, with health checks that automatically drain unhealthy nodes and redistribute pending sessions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-session-manager/)
