---
name: "Selenium Grid Session Distributor"
slug: "selenium-grid-session-distributor"
description: "Manages browser session allocation across Selenium Grid 4 nodes using the GraphQL status endpoint and SE_NODE_MAX_SESSIONS configuration. Implements weighted round-robin distribution with health-check-based failover for Chrome, Firefox, and Edge instances."
github_stars: 34076
verification: "listed"
source: "https://github.com/SeleniumHQ/selenium"
category: "Browser Automation"
framework: "Cursor"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Session Distributor

Manages browser session allocation across Selenium Grid 4 nodes using the GraphQL status endpoint and SE_NODE_MAX_SESSIONS configuration. Implements weighted round-robin distribution with health-check-based failover for Chrome, Firefox, and Edge instances.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install -r py/requirements_lock.txt

Requirements and caveats from upstream:
- As an alternative you can build a [Dev Container](https://containers.dev/) - basically a docker container -
- #### Using Docker Image
- You can also build a Docker image suitable

Basic usage or getting-started notes:
- to make sure this isn't required in the long run.
- Often we wrap Bazel commands with our custom [Rake](http://rake.rubyforge.org/) wrapper. These are run with the ./go command.
- bazel run — builds the target and then executes it.

- Source: https://github.com/SeleniumHQ/selenium
- Extracted from upstream docs: https://raw.githubusercontent.com/SeleniumHQ/selenium/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-session-distributor/)
