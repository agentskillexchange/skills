---
title: "Extract data and complete workflows in your real logged-in browser"
description: "Use bb-browser when an agent needs to inspect pages, pull data, or complete form-driven tasks inside the user’s actual logged-in Chrome session. It is for browser work where normal HTTP fetches fail because the important context lives behind auth, cookies, or internal web apps."
verification: "security_reviewed"
source: "https://github.com/epiral/bb-browser/tree/main/skills/bb-browser"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "epiral/bb-browser"
  github_stars: 4412
---

# Extract data and complete workflows in your real logged-in browser

bb-browser is a browser-control tool and MCP/CLI workflow for agents that need access to the user’s real authenticated browser state. This skill is not a generic “browser tool” listing. The job here is specific: an agent opens a site in the user’s real browser session, inspects interactive elements, extracts data from pages that require login, and completes bounded browser actions such as search, clicking through internal dashboards, or filling routine forms.

Use this when a normal API call or public scraper is not enough. Typical cases include internal admin panels, SaaS dashboards, pages that depend on existing cookies, and account views that only exist after sign-in. The point of invoking the agent skill is that the agent can reuse the user’s logged-in context instead of asking the user to manually navigate every page.

The scope boundary matters. This entry is not a catalog card for bb-browser as a product, browser, or SDK. It is narrowly about authenticated browser retrieval and action-taking through the user’s existing session. If you just need a public web fetch, a generic browser automation library, or a development framework for building your own browser tool, use those directly instead.

Integration points are clear in the upstream docs: the agent can open URLs, snapshot interactive elements, click, fill, close tabs, and use bb-browser’s site adapters when a workflow already exists for a specific platform. That makes it useful for research, internal operations, support workflows, and other tasks where the browser itself is the only realistic integration surface.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/extract-data-and-complete-workflows-in-your-real-logged-in-browser/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/extract-data-and-complete-workflows-in-your-real-logged-in-browser
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/extract-data-and-complete-workflows-in-your-real-logged-in-browser`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-data-and-complete-workflows-in-your-real-logged-in-browser/)
