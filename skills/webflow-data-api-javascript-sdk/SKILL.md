---
title: "Webflow Data API JavaScript SDK"
description: "Automates site, CMS, and publishing workflows with Webflow’s official JavaScript SDK for the Webflow Data API. Useful for agents that need to list sites, publish changes, manage CMS data, and authenticate with workspace tokens, site tokens, or OAuth."
slug: "webflow-data-api-javascript-sdk"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/webflow/js-webflow-api"
tool_ecosystem:
  github_repo: "webflow/js-webflow-api"
  github_stars: 338
---

# Webflow Data API JavaScript SDK

Automates site, CMS, and publishing workflows with Webflow’s official JavaScript SDK for the Webflow Data API. Useful for agents that need to list sites, publish changes, manage CMS data, and authenticate with workspace tokens, site tokens, or OAuth.

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
clawhub install webflow-data-api-javascript-sdk
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Webflow Data API JavaScript SDK is built around Webflow’s official js-webflow-api repository and the companion Webflow Data API documentation. The upstream SDK exposes typed request builders and a JavaScript client for Webflow’s REST API, covering workflows such as listing sites, reading site metadata, publishing sites, handling custom domains, and authenticating with workspace tokens, site tokens, or OAuth. That makes it a strong tool-anchored skill for agents that need to operate Webflow programmatically instead of clicking through the dashboard.
This skill is especially useful for content operations, CMS publishing pipelines, internal tooling, and integration work. An agent can use it to sync external content into Webflow CMS collections, verify site configuration, publish staged changes, or build app-style automations that act on behalf of workspace users. Because the official docs document authentication, rate limits, versioning, error handling, and SDK usage, the implementation surface is concrete rather than speculative. The SDK examples show a WebflowClient configured with an access token and then used for calls like sites.list(), sites.get(), and sites.publish().
Integration points include Webflow workspaces, site-level automations, CMS sync jobs, developer portals, and OAuth-based multi-tenant apps. For teams already using Node.js or TypeScript, the official package provides a direct path from agent instructions to live Webflow actions with retries, timeouts, and typed error handling.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/webflow-data-api-javascript-sdk/)
