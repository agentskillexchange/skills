---
title: "Verify local web apps with Playwright scripts and managed dev servers"
description: "Tool name: Anthropic’s webapp-testing skill in the public anthropics/skills repository. The upstream source is unusually concrete about agent behavior. It tells the agent to write native Python Playwright scripts, use scripts/with_server.py to manage one or more local servers, and follow a reconnaissance-then-action workflow for dynamic apps. That means the skill is not just “use Playwright.” It is a repeatable operator playbook for verifying local web applications.\nWhat the agent does: start the frontend and, if needed, backend servers; wait for ports to come up; open the rendered app in headless Chromium; wait for networkidle so JavaScript has actually settled; inspect the live DOM; capture screenshots; identify reliable selectors from rendered state; click, type, and assert expected behavior; and return logs or screenshots when something breaks. The helper supports single-server and multi-server setups, which matters for modern apps that split frontend and API services.\nWhen to use it: invoke this skill when the job is to verify a local web app, reproduce a UI bug, smoke-test a new feature before merge, or debug why a dynamic page behaves differently after JavaScript runs. This is the right fit when the user should not have to manage server lifecycle, port readiness, and Playwright orchestration manually.\nScope boundary: this is not a generic Playwright product card, not a browser-grid listing, and not a catch-all web scraping framework entry. Its boundary is local webapp verification and debugging through the specific workflow defined in the upstream skill. Integration points: Python, Playwright, local npm or Python dev servers, screenshots, browser logs, and optional CI usage for repeatable smoke checks."
verification: security_reviewed
source: "https://github.com/anthropics/skills/tree/main/skills/webapp-testing"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "anthropics/skills"
  github_stars: 116154
---

# Verify local web apps with Playwright scripts and managed dev servers

Tool name: Anthropic’s webapp-testing skill in the public anthropics/skills repository. The upstream source is unusually concrete about agent behavior. It tells the agent to write native Python Playwright scripts, use scripts/with_server.py to manage one or more local servers, and follow a reconnaissance-then-action workflow for dynamic apps. That means the skill is not just “use Playwright.” It is a repeatable operator playbook for verifying local web applications.
What the agent does: start the frontend and, if needed, backend servers; wait for ports to come up; open the rendered app in headless Chromium; wait for networkidle so JavaScript has actually settled; inspect the live DOM; capture screenshots; identify reliable selectors from rendered state; click, type, and assert expected behavior; and return logs or screenshots when something breaks. The helper supports single-server and multi-server setups, which matters for modern apps that split frontend and API services.
When to use it: invoke this skill when the job is to verify a local web app, reproduce a UI bug, smoke-test a new feature before merge, or debug why a dynamic page behaves differently after JavaScript runs. This is the right fit when the user should not have to manage server lifecycle, port readiness, and Playwright orchestration manually.
Scope boundary: this is not a generic Playwright product card, not a browser-grid listing, and not a catch-all web scraping framework entry. Its boundary is local webapp verification and debugging through the specific workflow defined in the upstream skill. Integration points: Python, Playwright, local npm or Python dev servers, screenshots, browser logs, and optional CI usage for repeatable smoke checks.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/verify-local-web-apps-with-playwright-scripts-and-managed-dev-servers
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/verify-local-web-apps-with-playwright-scripts-and-managed-dev-servers` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-local-web-apps-with-playwright-scripts-and-managed-dev-servers/)
