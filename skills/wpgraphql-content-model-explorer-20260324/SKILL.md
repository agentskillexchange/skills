---
name: "WPGraphQL Content Model Explorer"
description: "Inspects a WordPress site with WPGraphQL enabled and maps post types, taxonomies, custom fields, connections, and query patterns into a usable schema guide. It helps agents move from ad hoc queries to deliberate GraphQL documents, fragments, and client-side SDK usage."
category: "WordPress & CMS"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wpgraphql-content-model-explorer-20260324/"
---

# WPGraphQL Content Model Explorer

Inspects a WordPress site with WPGraphQL enabled and maps post types, taxonomies, custom fields, connections, and query patterns into a usable schema guide. It helps agents move from ad hoc queries to deliberate GraphQL documents, fragments, and client-side SDK usage.

## Overview

This skill audits a WordPress installation that exposes content through **WPGraphQL** and turns the live schema into a usable content model reference. Rather than guessing field names or manually clicking through GraphiQL, it runs introspection, catalogs root queries, post type nodes, taxonomy connections, and custom field extensions from plugins like ACF or Yoast. It documents which objects are queryable, where pagination or filtering is available, and how menus, media, authors, and SEO data are represented in the schema. For headless WordPress teams, that saves time and reduces the back-and-forth between frontend developers and CMS maintainers.

The workflow can generate example GraphQL documents, reusable fragments, and a compact compatibility note for Apollo Client, urql, Relay, or a custom fetch wrapper. If custom post types expose uneven or incomplete data, the skill flags those gaps and suggests whether to fix schema registration in PHP or add explicit GraphQL field definitions. Outputs can include Markdown docs, SDL excerpts, JSON introspection files, and starter queries for Next.js, Gatsby, Astro, or a webhook-triggered build pipeline. Integration points are broad: CI validation of schema drift, typed code generation with GraphQL Code Generator, and connection into search or caching layers like Redis and Varnish. The final deliverable is a practical map of the WPGraphQL surface area, not just a dump of schema JSON.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wpgraphql-content-model-explorer-20260324
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wpgraphql-content-model-explorer-20260324 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wpgraphql-content-model-explorer-20260324 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wpgraphql-content-model-explorer-20260324 -a codex
```

### OpenClaw

```bash
clawhub install wpgraphql-content-model-explorer-20260324
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wpgraphql-content-model-explorer-20260324/
