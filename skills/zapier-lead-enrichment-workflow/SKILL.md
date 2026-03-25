---
name: "Zapier Multi-Step Lead Enrichment Workflow"
description: "Builds a Zapier automation using the Zapier NLA API to trigger on new HubSpot form submissions and enrich contact records via the Clearbit Enrichment API. Enriched data is written back to HubSpot and simultaneously posted to Slack via the Web API chat.postMessage endpoint."
category: "Integrations & Connectors"
framework: "MCP-compatible"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/zapier-lead-enrichment-workflow/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "hubspot"  # from ase_tool_match
  github_stars: 391  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 905578  # from ase_npm_downloads
  github_repo: "HubSpot/hubspot-api-nodejs"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Zapier Multi-Step Lead Enrichment Workflow

Builds a Zapier automation using the Zapier NLA API to trigger on new HubSpot form submissions and enrich contact records via the Clearbit Enrichment API. Enriched data is written back to HubSpot and simultaneously posted to Slack via the Web API chat.postMessage endpoint.

## Overview

Builds a Zapier automation using the Zapier NLA API to trigger on new HubSpot form submissions and enrich contact records via the Clearbit Enrichment API. Enriched data is written back to HubSpot and simultaneously posted to Slack via the Web API chat.postMessage endpoint.

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
