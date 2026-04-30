---
title: "Selenium Grid Session Distributor"
description: "Manages browser session allocation across Selenium Grid 4 nodes using the GraphQL status endpoint and SE_NODE_MAX_SESSIONS configuration. Implements weighted round-robin distribution with health-check-based failover for Chrome, Firefox, and Edge instances."
verification: "security_reviewed"
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Session Distributor

Manages browser session allocation across Selenium Grid 4 nodes using the GraphQL status endpoint and SE_NODE_MAX_SESSIONS configuration. Implements weighted round-robin distribution with health-check-based failover for Chrome, Firefox, and Edge instances.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-session-distributor/)
