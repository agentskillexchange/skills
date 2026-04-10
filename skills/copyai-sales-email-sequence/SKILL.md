---
title: "Copy.ai Sales Email Sequence Builder"
description: "Leverages Copy.ai’s Workflows API to generate multi-step cold outreach sequences with persona-specific messaging. Each sequence step is rendered using Copy.ai’s email-sequence template type and pushed to HubSpot CRM via the HubSpot Contacts and Emails API."
slug: "copyai-sales-email-sequence"
category:
  - "Content Writing &amp; SEO"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/copyai-sales-email-sequence/"
listed: true
---

# Copy.ai Sales Email Sequence Builder

Leverages Copy.ai’s Workflows API to generate multi-step cold outreach sequences with persona-specific messaging. Each sequence step is rendered using Copy.ai’s email-sequence template type and pushed to HubSpot CRM via the HubSpot Contacts and Emails API.

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
clawhub install copyai-sales-email-sequence
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Copy.ai Sales Email Sequence Builder is built around HubSpot CRM and marketing APIs. The underlying ecosystem is represented by HubSpot/hubspot-api-nodejs (391+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like contacts, companies, deals, forms, workflows, search API, associations and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to hubspot so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Leverages Copy.ai's Workflows API to generate multi-step cold outreach sequences with persona-specific messaging. Each sequence step is rendered using Copy.ai's email-sequence template type and pushed to HubSpot CRM via the HubSpot Contacts and Emails API. The implementation typically relies on contacts, companies, deals, forms, workflows, search API, associations, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses contacts, companies, deals, forms, workflows, search API, associations instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as sales automation, CRM sync, lead enrichment, and lifecycle tracking.
For generator-style use cases, the skill turns a vague request into repeatable scaffolding with defaults that match the upstream toolchain rather than inventing ad hoc files. Key integration points include sales automation, CRM sync, lead enrichment, and lifecycle tracking. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/copyai-sales-email-sequence/)
