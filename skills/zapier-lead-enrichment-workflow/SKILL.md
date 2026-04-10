---
title: "Zapier Multi-Step Lead Enrichment Workflow"
description: "Builds a Zapier automation using the Zapier NLA API to trigger on new HubSpot form submissions and enrich contact records via the Clearbit Enrichment API. Enriched data is written back to HubSpot and simultaneously posted to Slack via the Web API chat.postMessage endpoint."
slug: "zapier-lead-enrichment-workflow"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/zapier-lead-enrichment-workflow/"
---

# Zapier Multi-Step Lead Enrichment Workflow

Builds a Zapier automation using the Zapier NLA API to trigger on new HubSpot form submissions and enrich contact records via the Clearbit Enrichment API. Enriched data is written back to HubSpot and simultaneously posted to Slack via the Web API chat.postMessage endpoint.

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
clawhub install zapier-lead-enrichment-workflow
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Zapier Multi-Step Lead Enrichment Workflow is built around HubSpot CRM and marketing APIs. The underlying ecosystem is represented by HubSpot/hubspot-api-nodejs (391+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like contacts, companies, deals, forms, workflows, search API, associations and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to hubspot so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Builds a Zapier automation using the Zapier NLA API to trigger on new HubSpot form submissions and enrich contact records via the Clearbit Enrichment API. Enriched data is written back to HubSpot and simultaneously posted to Slack via the Web API chat.postMessage endpoint. The implementation typically relies on contacts, companies, deals, forms, workflows, search API, associations, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses contacts, companies, deals, forms, workflows, search API, associations instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as sales automation, CRM sync, lead enrichment, and lifecycle tracking.
Key integration points include sales automation, CRM sync, lead enrichment, and lifecycle tracking. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/zapier-lead-enrichment-workflow/)
