---
title: "HubSpot CRM Contact Enrichment Pipeline"
description: "Enriches HubSpot CRM contacts using the v3 Contacts API with batch read/update operations. Cross-references company associations via crm.associations.batchRead(), and syncs lifecycle stage transitions with custom property updates."
slug: "hubspot-crm-contact-enrichment-pipeline"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/hubspot-crm-contact-enrichment-pipeline/"
---

# HubSpot CRM Contact Enrichment Pipeline

Enriches HubSpot CRM contacts using the v3 Contacts API with batch read/update operations. Cross-references company associations via crm.associations.batchRead(), and syncs lifecycle stage transitions with custom property updates.

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
clawhub install hubspot-crm-contact-enrichment-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The HubSpot CRM Contact Enrichment Pipeline automates contact data enhancement using the HubSpot CRM v3 API. It performs batch operations via crm.contacts.batchApi.read() and batchApi.update() to efficiently process thousands of contacts with minimal API calls.
The skill manages company-to-contact associations using crm.associations.batchApi.read() with HUBSPOT_DEFINED association types, enabling cross-referencing of company data (industry, revenue, employee count) to enrich contact records. It tracks lifecycle stage transitions from subscriber through opportunity to customer.
Advanced features include custom property creation via crm.properties.create() for enrichment fields, deal pipeline stage monitoring through crm.deals.searchApi.doSearch() with filter groups, and engagement tracking via timeline events. The agent handles HubSpot’s 100-request-per-10-seconds rate limit with token bucket throttling and implements OAuth 2.0 token refresh for long-running pipelines. Supports list segmentation via crm.lists.searchApi and workflow enrollment triggers based on enrichment scores.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hubspot-crm-contact-enrichment-pipeline/)
