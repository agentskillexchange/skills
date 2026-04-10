---
title: "WPGraphQL for ACF WordPress GraphQL Field Mapping"
description: "WPGraphQL for ACF extends WPGraphQL so Advanced Custom Fields data becomes queryable through a typed GraphQL schema. It is useful for headless WordPress builds that need structured access to field groups, repeaters, and custom post type metadata without writing bespoke REST endpoints."
slug: "wpgraphql-for-acf-wordpress-graphql-field-mapping"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/wp-graphql/wpgraphql-acf"
listed: true
---

# WPGraphQL for ACF WordPress GraphQL Field Mapping

WPGraphQL for ACF extends WPGraphQL so Advanced Custom Fields data becomes queryable through a typed GraphQL schema. It is useful for headless WordPress builds that need structured access to field groups, repeaters, and custom post type metadata without writing bespoke REST endpoints.

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
clawhub install wpgraphql-for-acf-wordpress-graphql-field-mapping
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

WPGraphQL for ACF is an extension plugin for the WPGraphQL ecosystem that exposes Advanced Custom Fields data in the WordPress GraphQL schema. The project is maintained by the WPGraphQL community and is designed for teams building headless WordPress frontends, decoupled editorial systems, and custom integrations that need strongly typed access to content fields. Instead of manually mapping ACF data into custom REST routes, the plugin generates GraphQL object types, interfaces, and fields that align with the field groups configured in the WordPress admin or registered in code.
In practice, this makes it much easier to query complex field sets from Next.js, Gatsby, Astro, or custom clients. Developers can model reusable content structures in ACF, mark them for GraphQL exposure, and query them alongside posts, pages, taxonomies, and other WPGraphQL types. The plugin also supports ACF post type and taxonomy registration flows, provides hooks and filters for extending schema behavior, and works with both UI-defined and code-defined field groups. For teams already using WPGraphQL and ACF, this is a direct fit for reducing API glue code while keeping the data contract explicit and inspectable.
The upstream project documents requirements clearly: WordPress 6.1+, PHP 7.4+, WPGraphQL, and Advanced Custom Fields. That makes it a concrete, production-oriented skill candidate for WordPress and CMS automation workflows centered on structured content delivery.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wpgraphql-for-acf-wordpress-graphql-field-mapping/)
