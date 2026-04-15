---
title: "HubSpot CRM Contact Enrichment Pipeline"
description: "Enriches HubSpot CRM contacts using the v3 Contacts API with batch read/update operations. Cross-references company associations via crm.associations.batchRead(), and syncs lifecycle stage transitions with custom property updates."
verification: security_reviewed
source: "https://github.com/HubSpot/hubspot-api-nodejs"
category:
  - "Integrations & Connectors"
framework:
  - "Claude Code"
---

# HubSpot CRM Contact Enrichment Pipeline

The HubSpot CRM Contact Enrichment Pipeline automates contact data enhancement using the HubSpot CRM v3 API. It performs batch operations via crm.contacts.batchApi.read() and batchApi.update() to efficiently process thousands of contacts with minimal API calls.

The skill manages company-to-contact associations using crm.associations.batchApi.read() with HUBSPOT_DEFINED association types, enabling cross-referencing of company data (industry, revenue, employee count) to enrich contact records. It tracks lifecycle stage transitions from subscriber through opportunity to customer.

Advanced features include custom property creation via crm.properties.create() for enrichment fields, deal pipeline stage monitoring through crm.deals.searchApi.doSearch() with filter groups, and engagement tracking via timeline events. The agent handles HubSpot’s 100-request-per-10-seconds rate limit with token bucket throttling and implements OAuth 2.0 token refresh for long-running pipelines. Supports list segmentation via crm.lists.searchApi and workflow enrollment triggers based on enrichment scores.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/hubspot-crm-contact-enrichment-pipeline
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/hubspot-crm-contact-enrichment-pipeline` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hubspot-crm-contact-enrichment-pipeline/)
