---
name: "HubSpot CRM Contact Enrichment Pipeline"
slug: "hubspot-crm-contact-enrichment-pipeline"
description: "Enriches HubSpot CRM contacts using the v3 Contacts API with batch read/update operations. Cross-references company associations via crm.associations.batchRead(), and syncs lifecycle stage transitions with custom property updates."
github_stars: 392
verification: "security_reviewed"
source: "https://github.com/HubSpot/hubspot-api-nodejs"
category: "Integrations & Connectors"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "hubspot/hubspot-api-nodejs"
  github_stars: 392
  npm_package: "@hubspot/api-client"
  npm_weekly_downloads: 986793
---

# HubSpot CRM Contact Enrichment Pipeline

Enriches HubSpot CRM contacts using the v3 Contacts API with batch read/update operations. Cross-references company associations via crm.associations.batchRead(), and syncs lifecycle stage transitions with custom property updates.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install @hubspot/api-client
- npm install
- npm run test
- npm run lint

Requirements and caveats from upstream:
- const hubspot = require('@hubspot/api-client')
- const fs = require('fs')

Basic usage or getting-started notes:
- defaultHeaders: { 'My-header': 'test-example' },
- All methods return a [promise]. The success includes the serialized to JSON body and response objects. Use the API method via:
- javascript

- Source: https://github.com/HubSpot/hubspot-api-nodejs
- Extracted from upstream docs: https://raw.githubusercontent.com/HubSpot/hubspot-api-nodejs/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hubspot-crm-contact-enrichment-pipeline/)
