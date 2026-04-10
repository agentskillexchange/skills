---
name: HubSpot CRM Contact Enrichment Pipeline
description: Enriches HubSpot CRM contacts using the v3 Contacts API with batch read/update
  operations. Cross-references company associations via crm.associations.batchRead(),
  and syncs lifecycle stage transitions with custom property updates.
verification: security_reviewed
source: https://agentskillexchange.com/skills/hubspot-crm-contact-enrichment-pipeline/
category:
- Integrations &amp; Connectors
framework:
- Claude Code
---
# HubSpot CRM Contact Enrichment Pipeline

The HubSpot CRM Contact Enrichment Pipeline automates contact data enhancement using the HubSpot CRM v3 API. It performs batch operations via crm.contacts.batchApi.read() and batchApi.update() to efficiently process thousands of contacts with minimal API calls.
The skill manages company-to-contact associations using crm.associations.batchApi.read() with HUBSPOT_DEFINED association types, enabling cross-referencing of company data (industry, revenue, employee count) to enrich contact records. It tracks lifecycle stage transitions from subscriber through opportunity to customer.
Advanced features include custom property creation via crm.properties.create() for enrichment fields, deal pipeline stage monitoring through crm.deals.searchApi.doSearch() with filter groups, and engagement tracking via timeline events. The agent handles HubSpot's 100-request-per-10-seconds rate limit with token bucket throttling and implements OAuth 2.0 token refresh for long-running pipelines. Supports list segmentation via crm.lists.searchApi and workflow enrollment triggers based on enrichment scores.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hubspot-crm-contact-enrichment-pipeline/)
