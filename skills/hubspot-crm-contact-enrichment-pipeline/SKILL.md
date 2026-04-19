---
title: "HubSpot CRM Contact Enrichment Pipeline"
description: "The HubSpot CRM Contact Enrichment Pipeline automates contact data enhancement using the HubSpot CRM v3 API. It performs batch operations via crm.contacts.batchApi.read() and batchApi.update() to efficiently process thousands of contacts with minimal API calls. The skill manages company-to-contact associations using crm.associations.batchApi.read() with HUBSPOT_DEFINED association types, enabling cross-referencing of company data (industry, revenue, employee count) to enrich contact records. It tracks lifecycle stage transitions from subscriber through opportunity to customer. Advanced features include custom property creation via crm.properties.create() for enrichment fields, deal pipeline stage monitoring through crm.deals.searchApi.doSearch() with filter groups, and engagement tracking via timeline events. The agent handles HubSpot&#8217;s 100-request-per-10-seconds rate limit with token bucket throttling and implements OAuth 2.0 token refresh for long-running pipelines. Supports list segmentation via crm.lists.searchApi and workflow enrollment triggers based on enrichment scores."
source: "https://github.com/HubSpot/hubspot-api-nodejs"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Claude Code"
tool_ecosystem:
  npm_package: "@hubspot/api-client"
---

# HubSpot CRM Contact Enrichment Pipeline

The HubSpot CRM Contact Enrichment Pipeline automates contact data enhancement using the HubSpot CRM v3 API. It performs batch operations via crm.contacts.batchApi.read() and batchApi.update() to efficiently process thousands of contacts with minimal API calls. The skill manages company-to-contact associations using crm.associations.batchApi.read() with HUBSPOT_DEFINED association types, enabling cross-referencing of company data (industry, revenue, employee count) to enrich contact records. It tracks lifecycle stage transitions from subscriber through opportunity to customer. Advanced features include custom property creation via crm.properties.create() for enrichment fields, deal pipeline stage monitoring through crm.deals.searchApi.doSearch() with filter groups, and engagement tracking via timeline events. The agent handles HubSpot&#8217;s 100-request-per-10-seconds rate limit with token bucket throttling and implements OAuth 2.0 token refresh for long-running pipelines. Supports list segmentation via crm.lists.searchApi and workflow enrollment triggers based on enrichment scores.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hubspot-crm-contact-enrichment-pipeline/)
