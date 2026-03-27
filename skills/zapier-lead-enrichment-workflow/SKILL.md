---
name: "Zapier Multi-Step Lead Enrichment Workflow"
description: "Builds a Zapier automation using the Zapier NLA API to trigger on new HubSpot form submissions and enrich contact records via the Clearbit Enrichment API. Enriched data is written back to HubSpot and simultaneously posted to Slack via the Web API chat.postMessage endpoint."
category: "Integrations & Connectors"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/zapier-lead-enrichment-workflow/"
tool_ecosystem:
  tool: hubspot
  github_stars: 391
  npm_weekly_downloads: 905578
  github_repo: HubSpot/hubspot-api-nodejs
  license: Apache-2.0
  maintained: true
---

# Zapier Multi-Step Lead Enrichment Workflow

Builds a Zapier automation using the Zapier NLA API to trigger on new HubSpot form submissions and enrich contact records via the Clearbit Enrichment API. Enriched data is written back to HubSpot and simultaneously posted to Slack via the Web API chat.postMessage endpoint.

## Overview

**Zapier Multi-Step Lead Enrichment Workflow** is built around HubSpot CRM and marketing APIs. The underlying ecosystem is represented by `HubSpot/hubspot-api-nodejs` (391+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like contacts, companies, deals, forms, workflows, search API, associations and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to hubspot so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Builds a Zapier automation using the Zapier NLA API to trigger on new HubSpot form submissions and enrich contact records via the Clearbit Enrichment API. Enriched data is written back to HubSpot and simultaneously posted to Slack via the Web API chat.postMessage endpoint. The implementation typically relies on contacts, companies, deals, forms, workflows, search API, associations, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses contacts, companies, deals, forms, workflows, search API, associations instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as sales automation, CRM sync, lead enrichment, and lifecycle tracking.

Key integration points include sales automation, CRM sync, lead enrichment, and lifecycle tracking. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill zapier-lead-enrichment-workflow
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill zapier-lead-enrichment-workflow -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill zapier-lead-enrichment-workflow -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill zapier-lead-enrichment-workflow -a codex
```

### OpenClaw

```bash
clawhub install zapier-lead-enrichment-workflow
```

## Source

- Marketplace: https://agentskillexchange.com/skills/zapier-lead-enrichment-workflow/
