---
name: "WPGraphQL GraphQL API for WordPress"
description: "Builds headless WordPress workflows around WPGraphQL, the open-source GraphQL API plugin for WordPress. Useful for querying posts, custom post types, menus, taxonomies, and custom fields through typed GraphQL operations instead of ad hoc REST fetches."
category: "WordPress &amp; CMS"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/wp-graphql/wp-graphql"
---
# WPGraphQL GraphQL API for WordPress

Builds headless WordPress workflows around WPGraphQL, the open-source GraphQL API plugin for WordPress. Useful for querying posts, custom post types, menus, taxonomies, and custom fields through typed GraphQL operations instead of ad hoc REST fetches.

## Overview

WPGraphQL GraphQL API for WordPress is for headless and composable WordPress projects that want a typed query layer instead of a loose collection of REST endpoints. The skill is grounded in the real WPGraphQL plugin and its documented APIs, including schema objects, connections, resolvers, custom post type exposure, menu queries, and extension hooks such as register_graphql_field and register_graphql_object_type. It is especially useful when a frontend built in Next.js, Remix, Astro, or another JavaScript framework needs stable field selection and predictable relationships.

The workflow usually starts by identifying the WordPress entities that must be exposed, such as posts, pages, products, taxonomies, or Advanced Custom Fields data. From there, the skill can shape GraphQL queries, explain pagination through connections and edges, define naming conventions for schema additions, and help reason about nullability, authorization, and field resolution. That makes it valuable both for using WPGraphQL as a consumer and for extending it safely as a plugin author.

Outputs include GraphQL queries and mutations, schema extension snippets, documentation for query contracts, and debugging guidance for resolver issues, field registration mistakes, or mismatches between WordPress data models and API output. Integration points include Apollo Client, Relay-style query patterns, headless frontends, build-time data fetching, and custom WordPress plugins that expose business logic through GraphQL. Use this skill when the job is to make WordPress queryable as a real GraphQL application rather than just treat it as a generic CMS backend.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wpgraphql-graphql-api-wordpress
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wpgraphql-graphql-api-wordpress -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wpgraphql-graphql-api-wordpress -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wpgraphql-graphql-api-wordpress -a codex
```

### OpenClaw

```bash
clawhub install wpgraphql-graphql-api-wordpress
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wpgraphql-graphql-api-wordpress/)
