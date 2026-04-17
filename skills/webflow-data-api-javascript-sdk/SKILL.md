---
title: "Webflow Data API JavaScript SDK"
description: "Automates site, CMS, and publishing workflows with Webflow’s official JavaScript SDK for the Webflow Data API. Useful for agents that need to list sites, publish changes, manage CMS data, and authenticate with workspace tokens, site tokens, or OAuth."
verification: security_reviewed
source: "https://github.com/webflow/js-webflow-api"
category:
  - "WordPress & CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "webflow/js-webflow-api"
  github_stars: 340
---

# Webflow Data API JavaScript SDK

Webflow Data API JavaScript SDK is built around Webflow’s official js-webflow-api repository and the companion Webflow Data API documentation. The upstream SDK exposes typed request builders and a JavaScript client for Webflow’s REST API, covering workflows such as listing sites, reading site metadata, publishing sites, handling custom domains, and authenticating with workspace tokens, site tokens, or OAuth. That makes it a strong tool-anchored skill for agents that need to operate Webflow programmatically instead of clicking through the dashboard.

This skill is especially useful for content operations, CMS publishing pipelines, internal tooling, and integration work. An agent can use it to sync external content into Webflow CMS collections, verify site configuration, publish staged changes, or build app-style automations that act on behalf of workspace users. Because the official docs document authentication, rate limits, versioning, error handling, and SDK usage, the implementation surface is concrete rather than speculative. The SDK examples show a WebflowClient configured with an access token and then used for calls like sites.list(), sites.get(), and sites.publish().

Integration points include Webflow workspaces, site-level automations, CMS sync jobs, developer portals, and OAuth-based multi-tenant apps. For teams already using Node.js or TypeScript, the official package provides a direct path from agent instructions to live Webflow actions with retries, timeouts, and typed error handling.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/webflow-data-api-javascript-sdk
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/webflow-data-api-javascript-sdk` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/webflow-data-api-javascript-sdk/)
