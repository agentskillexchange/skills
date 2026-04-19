---
title: "Extract data and complete workflows in your real logged-in browser"
description: "bb-browser is a browser-control tool and MCP/CLI workflow for agents that need access to the user&#8217;s real authenticated browser state. This skill is not a generic “browser tool” listing. The job here is specific: an agent opens a site in the user&#8217;s real browser session, inspects interactive elements, extracts data from pages that require login, and completes bounded browser actions such as search, clicking through internal dashboards, or filling routine forms. Use this when a normal API call or public scraper is not enough. Typical cases include internal admin panels, SaaS dashboards, pages that depend on existing cookies, and account views that only exist after sign-in. The point of invoking the agent skill is that the agent can reuse the user&#8217;s logged-in context instead of asking the user to manually navigate every page. The scope boundary matters. This entry is not a catalog card for bb-browser as a product, browser, or SDK. It is narrowly about authenticated browser retrieval and action-taking through the user&#8217;s existing session. If you just need a public web fetch, a generic browser automation library, or a development framework for building your own browser tool, use those directly instead. Integration points are clear in the upstream docs: the agent can open URLs, snapshot interactive elements, click, fill, close tabs, and use bb-browser&#8217;s site adapters when a workflow already exists for a specific platform. That makes it useful for research, internal operations, support workflows, and other tasks where the browser itself is the only realistic integration surface."
source: "https://github.com/epiral/bb-browser/tree/main/skills/bb-browser"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "epiral/bb-browser"
  github_stars: 4412
---

# Extract data and complete workflows in your real logged-in browser

bb-browser is a browser-control tool and MCP/CLI workflow for agents that need access to the user&#8217;s real authenticated browser state. This skill is not a generic “browser tool” listing. The job here is specific: an agent opens a site in the user&#8217;s real browser session, inspects interactive elements, extracts data from pages that require login, and completes bounded browser actions such as search, clicking through internal dashboards, or filling routine forms. Use this when a normal API call or public scraper is not enough. Typical cases include internal admin panels, SaaS dashboards, pages that depend on existing cookies, and account views that only exist after sign-in. The point of invoking the agent skill is that the agent can reuse the user&#8217;s logged-in context instead of asking the user to manually navigate every page. The scope boundary matters. This entry is not a catalog card for bb-browser as a product, browser, or SDK. It is narrowly about authenticated browser retrieval and action-taking through the user&#8217;s existing session. If you just need a public web fetch, a generic browser automation library, or a development framework for building your own browser tool, use those directly instead. Integration points are clear in the upstream docs: the agent can open URLs, snapshot interactive elements, click, fill, close tabs, and use bb-browser&#8217;s site adapters when a workflow already exists for a specific platform. That makes it useful for research, internal operations, support workflows, and other tasks where the browser itself is the only realistic integration surface.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-data-and-complete-workflows-in-your-real-logged-in-browser/)
