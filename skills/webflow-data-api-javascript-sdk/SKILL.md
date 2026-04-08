---
title: Webflow Data API JavaScript SDK
description: Webflow Data API JavaScript SDK is built around Webflow’s official js-webflow-api
  repository and the companion Webflow Data API documentation. The upstream SDK exposes
  typed request builders and a JavaScript client for Webflow’s REST API, covering
  workflows such as listing sites, reading site metadata, publishing sites, handling
  custom domains, and authenticating with workspace tokens, site tokens, or OAuth.
  That makes it a strong tool-anchored skill for agents that need to operate Webflow
  programmatically instead of clicking through the dashboard. This skill is especially
  useful for content operations, CMS publishing pipelines, internal tooling, and integration
  work. An agent can use it to sync external content into Webflow CMS collections,
  verify site configuration, publish staged changes, or build app-style automations
  that act on behalf of workspace users. Because the official docs document authentication,
  rate limits, versioning, error handling, and SDK usage, the implementation surface
  is concrete rather than speculative. The SDK examples show a WebflowClient configured
  with an access token and then used for calls like sites.list() , sites.get() , and
  sites.publish() . Integration points include Webflow workspaces, site-level automations,
  CMS sync jobs, developer portals, and OAuth-based multi-tenant apps. For teams already
  using Node.js or TypeScript, the official package provides a direct path from agent
  instructions to live Webflow actions with retries, timeouts, and typed error handling.
verification: security_reviewed
source: https://github.com/webflow/js-webflow-api
category:
- WordPress &amp; CMS
framework:
- Multi-Framework
---

# Webflow Data API JavaScript SDK

Webflow Data API JavaScript SDK is built around Webflow’s official js-webflow-api repository and the companion Webflow Data API documentation. The upstream SDK exposes typed request builders and a JavaScript client for Webflow’s REST API, covering workflows such as listing sites, reading site metadata, publishing sites, handling custom domains, and authenticating with workspace tokens, site tokens, or OAuth. That makes it a strong tool-anchored skill for agents that need to operate Webflow programmatically instead of clicking through the dashboard. This skill is especially useful for content operations, CMS publishing pipelines, internal tooling, and integration work. An agent can use it to sync external content into Webflow CMS collections, verify site configuration, publish staged changes, or build app-style automations that act on behalf of workspace users. Because the official docs document authentication, rate limits, versioning, error handling, and SDK usage, the implementation surface is concrete rather than speculative. The SDK examples show a WebflowClient configured with an access token and then used for calls like sites.list() , sites.get() , and sites.publish() . Integration points include Webflow workspaces, site-level automations, CMS sync jobs, developer portals, and OAuth-based multi-tenant apps. For teams already using Node.js or TypeScript, the official package provides a direct path from agent instructions to live Webflow actions with retries, timeouts, and typed error handling.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/webflow-data-api-javascript-sdk/)
