---
title: "Mailchimp Marketing API Node.js SDK"
description: "Connects agents to Mailchimp’s official Marketing API through the official Node.js client library. Useful for audience sync, tagging, campaign orchestration, automation triggers, webhooks, and batch operations at marketing scale."
verification: "security_reviewed"
source: "https://github.com/mailchimp/mailchimp-marketing-node"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mailchimp/mailchimp-marketing-node"
  github_stars: 165
---

# Mailchimp Marketing API Node.js SDK

Mailchimp Marketing API Node.js SDK is anchored to Mailchimp’s official mailchimp-marketing-node repository and the Mailchimp Marketing API documentation. The upstream docs describe concrete jobs-to-be-done: creating audiences, adding contacts, tagging subscribers, syncing external events that trigger automations, handling webhooks, and running large requests asynchronously through the batch endpoint. The official Node.js client library wraps that API surface for JavaScript applications, which makes it a practical foundation for agent workflows instead of a generic “email integration” placeholder. This skill fits best when an agent needs to keep product or CRM data in sync with Mailchimp, create or update audiences, manage segmentation inputs, schedule or trigger campaigns, or coordinate outbound marketing workflows based on external user behavior. Because Mailchimp exposes OAuth for acting on behalf of users and supports webhook-driven synchronization, the integration points are clear for SaaS connectors, internal marketing operations, and customer lifecycle automation. The official SDK is published on npm and documented by Mailchimp as the primary Node.js client for the Marketing API. Operationally, an agent can use this skill to bridge application events and email automation: for example, tagging contacts after product actions, syncing audience membership, triggering campaign-related workflows, or batching expensive synchronization jobs for better throughput. The combination of official docs, official repo, npm distribution, and released package versions gives this skill enough source-backed trust to publish directly as verified metadata.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/mailchimp-marketing-api-nodejs-sdk/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/mailchimp-marketing-api-nodejs-sdk
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/mailchimp-marketing-api-nodejs-sdk`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mailchimp-marketing-api-nodejs-sdk/)
