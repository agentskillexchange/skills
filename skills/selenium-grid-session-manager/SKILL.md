---
title: "Selenium Grid Session Manager"
description: "The Selenium Grid Session Manager orchestrates distributed browser testing infrastructure using Selenium Grid 4&#8217;s modern architecture. It communicates with the Grid via the GraphQL API endpoint (/graphql) for detailed session and node information, and the /status REST endpoint for health monitoring. The skill handles dynamic node registration and capability matching, ensuring test sessions are routed to nodes with the correct browser version, platform, and custom capabilities. It manages session queuing with configurable timeout and retry policies, preventing queue overflow during peak testing periods. Advanced features include automatic node scaling based on queue depth (integrating with Docker API for container-based nodes), session video recording via Selenium Video docker images, and VNC live-view connections for debugging. The manager tracks session lifecycle events (created, assigned, completed, failed) and generates utilization dashboards. It supports both hub-node and fully distributed Grid architectures, with health checks that automatically drain unhealthy nodes and redistribute pending sessions."
source: "https://github.com/SeleniumHQ/selenium"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Session Manager

The Selenium Grid Session Manager orchestrates distributed browser testing infrastructure using Selenium Grid 4&#8217;s modern architecture. It communicates with the Grid via the GraphQL API endpoint (/graphql) for detailed session and node information, and the /status REST endpoint for health monitoring. The skill handles dynamic node registration and capability matching, ensuring test sessions are routed to nodes with the correct browser version, platform, and custom capabilities. It manages session queuing with configurable timeout and retry policies, preventing queue overflow during peak testing periods. Advanced features include automatic node scaling based on queue depth (integrating with Docker API for container-based nodes), session video recording via Selenium Video docker images, and VNC live-view connections for debugging. The manager tracks session lifecycle events (created, assigned, completed, failed) and generates utilization dashboards. It supports both hub-node and fully distributed Grid architectures, with health checks that automatically drain unhealthy nodes and redistribute pending sessions.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-session-manager/)
