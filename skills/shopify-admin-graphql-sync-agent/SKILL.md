---
title: "Shopify Admin GraphQL Sync Agent"
description: "Coordinates Shopify data syncs with the Admin GraphQL API, including `bulkOperationRunQuery`, node connections, and webhook-assisted delta updates. Useful for product, inventory, and order pipelines that need higher throughput than ad hoc REST polling."
verification: security_reviewed
source: "https://github.com/Shopify/shopify-api-js"
category:
  - "Integrations &amp; Connectors"
tool_ecosystem:
  github_repo: "Shopify/shopify-api-js"
  github_stars: 959
  npm_package: "@shopify/shopify-api"
  npm_weekly_downloads: 318463
---

# Shopify Admin GraphQL Sync Agent

Coordinates Shopify data syncs with the Admin GraphQL API, including `bulkOperationRunQuery`, node connections, and webhook-assisted delta updates. Useful for product, inventory, and order pipelines that need higher throughput than ad hoc REST polling.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shopify-admin-graphql-sync-agent/)
