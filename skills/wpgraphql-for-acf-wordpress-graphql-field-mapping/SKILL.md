---
title: "WPGraphQL for ACF WordPress GraphQL Field Mapping"
description: "WPGraphQL for ACF extends WPGraphQL so Advanced Custom Fields data becomes queryable through a typed GraphQL schema. It is useful for headless WordPress builds that need structured access to field groups, repeaters, and custom post type metadata without writing bespoke REST endpoints."
verification: security_reviewed
source: "https://github.com/wp-graphql/wpgraphql-acf"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "wp-graphql/wpgraphql-acf"
  github_stars: 108
---

# WPGraphQL for ACF WordPress GraphQL Field Mapping

WPGraphQL for ACF is an extension plugin for the WPGraphQL ecosystem that exposes Advanced Custom Fields data in the WordPress GraphQL schema. The project is maintained by the WPGraphQL community and is designed for teams building headless WordPress frontends, decoupled editorial systems, and custom integrations that need strongly typed access to content fields. Instead of manually mapping ACF data into custom REST routes, the plugin generates GraphQL object types, interfaces, and fields that align with the field groups configured in the WordPress admin or registered in code.

In practice, this makes it much easier to query complex field sets from Next.js, Gatsby, Astro, or custom clients. Developers can model reusable content structures in ACF, mark them for GraphQL exposure, and query them alongside posts, pages, taxonomies, and other WPGraphQL types. The plugin also supports ACF post type and taxonomy registration flows, provides hooks and filters for extending schema behavior, and works with both UI-defined and code-defined field groups. For teams already using WPGraphQL and ACF, this is a direct fit for reducing API glue code while keeping the data contract explicit and inspectable.

The upstream project documents requirements clearly: WordPress 6.1+, PHP 7.4+, WPGraphQL, and Advanced Custom Fields. That makes it a concrete, production-oriented skill candidate for WordPress and CMS automation workflows centered on structured content delivery.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wpgraphql-for-acf-wordpress-graphql-field-mapping/)
