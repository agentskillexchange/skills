---
title: "HubSpot CRM Contact Enrichment Pipeline"
description: "Enriches HubSpot CRM contacts using the v3 Contacts API with batch read/update operations. Cross-references company associations via crm.associations.batchRead(), and syncs lifecycle stage transitions with custom property updates."
verification: security_reviewed
source: "https://github.com/HubSpot/hubspot-api-nodejs"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "hubspot/hubspot-api-nodejs"
  github_stars: 392
  npm_package: "@hubspot/api-client"
  npm_weekly_downloads: 986793
---

# HubSpot CRM Contact Enrichment Pipeline

The HubSpot CRM Contact Enrichment Pipeline automates contact data enhancement using the HubSpot CRM v3 API. It performs batch operations via crm.contacts.batchApi.read() and batchApi.update() to efficiently process thousands of contacts with minimal API calls.

The skill manages company-to-contact associations using crm.associations.batchApi.read() with HUBSPOT_DEFINED association types, enabling cross-referencing of company data (industry, revenue, employee count) to enrich contact records. It tracks lifecycle stage transitions from subscriber through opportunity to customer.

Advanced features include custom property creation via crm.properties.create() for enrichment fields, deal pipeline stage monitoring through crm.deals.searchApi.doSearch() with filter groups, and engagement tracking via timeline events. The agent handles HubSpot’s 100-request-per-10-seconds rate limit with token bucket throttling and implements OAuth 2.0 token refresh for long-running pipelines. Supports list segmentation via crm.lists.searchApi and workflow enrollment triggers based on enrichment scores.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hubspot-crm-contact-enrichment-pipeline/)
