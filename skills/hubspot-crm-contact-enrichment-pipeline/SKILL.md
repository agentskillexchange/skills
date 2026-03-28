---
name: "HubSpot CRM Contact Enrichment Pipeline"
description: "Enriches HubSpot CRM contacts using the v3 Contacts API with batch read/update operations. Cross-references company associations via crm.associations.batchRead(), and syncs lifecycle stage transitions with custom property updates."
category: "Integrations & Connectors"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/HubSpot/hubspot-api-nodejs"
tool_ecosystem:
  tool: hubspot
  github_stars: 391
  npm_weekly_downloads: 905578
  github_repo: HubSpot/hubspot-api-nodejs
  license: Apache-2.0
  maintained: true
---

# HubSpot CRM Contact Enrichment Pipeline

Enriches HubSpot CRM contacts using the v3 Contacts API with batch read/update operations. Cross-references company associations via crm.associations.batchRead(), and syncs lifecycle stage transitions with custom property updates.

## Overview

The HubSpot CRM Contact Enrichment Pipeline automates contact data enhancement using the HubSpot CRM v3 API. It performs batch operations via `crm.contacts.batchApi.read()` and `batchApi.update()` to efficiently process thousands of contacts with minimal API calls.

The skill manages company-to-contact associations using `crm.associations.batchApi.read()` with `HUBSPOT_DEFINED` association types, enabling cross-referencing of company data (industry, revenue, employee count) to enrich contact records. It tracks lifecycle stage transitions from subscriber through opportunity to customer.

Advanced features include custom property creation via `crm.properties.create()` for enrichment fields, deal pipeline stage monitoring through `crm.deals.searchApi.doSearch()` with filter groups, and engagement tracking via timeline events. The agent handles HubSpot’s 100-request-per-10-seconds rate limit with token bucket throttling and implements OAuth 2.0 token refresh for long-running pipelines. Supports list segmentation via `crm.lists.searchApi` and workflow enrollment triggers based on enrichment scores.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill hubspot-crm-contact-enrichment-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill hubspot-crm-contact-enrichment-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill hubspot-crm-contact-enrichment-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill hubspot-crm-contact-enrichment-pipeline -a codex
```

### OpenClaw

```bash
clawhub install hubspot-crm-contact-enrichment-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/hubspot-crm-contact-enrichment-pipeline/
