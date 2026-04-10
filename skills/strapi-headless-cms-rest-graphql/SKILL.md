---
name: "Strapi Open Source Headless CMS with REST and GraphQL APIs"
description: "Strapi is the leading open-source headless CMS built with Node.js and TypeScript. It auto-generates REST and GraphQL APIs from content types, provides a customizable admin panel, and supports roles, i18n, and plugin extensions."
verification: security_reviewed
source: "https://github.com/strapi/strapi"
category:
  - "WordPress &amp; CMS"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "strapi/strapi"
  github_stars: 71740
  ase_npm_package: "@strapi/strapi"
  npm_weekly_downloads: 147371
---

# Strapi Open Source Headless CMS with REST and GraphQL APIs

Strapi is an open-source, self-hosted headless content management system written in JavaScript and TypeScript. With nearly 70,000 GitHub stars and over 20 million npm downloads, it is the most widely adopted open-source headless CMS. Strapi auto-generates both REST and GraphQL APIs from user-defined content types, eliminating the need for manual endpoint coding.
The Content Type Builder allows defining structured content schemas through either the admin UI or programmatic configuration files. Each content type automatically receives full CRUD endpoints with filtering, sorting, pagination, population of relations, and field selection. The built-in role-based access control (RBAC) system supports granular permissions for both admin users and API consumers.
A skill leveraging Strapi enables agents to manage content lifecycles across headless architectures: creating and updating content entries, managing media assets, configuring webhooks for content events, querying content via the REST or GraphQL APIs, and managing user roles and permissions. The CLI tool (npx create-strapi-app) scaffolds new projects with database configuration for SQLite, PostgreSQL, MySQL, or MariaDB.
Key features include: internationalization (i18n) for multi-locale content, draft and publish workflow, media library with image optimization, webhook system for event-driven architectures, customizable admin panel with field-level configuration, and a plugin ecosystem for extending functionality. The Entity Service API and Query Engine API provide programmatic access for custom controllers and services.
Integration points for agent workflows include: automating content migration between environments, synchronizing content from external sources (APIs, spreadsheets, databases), generating content entries from structured data, managing SEO metadata across content types, and orchestrating multi-locale content publishing. Strapi v5 introduces the Document Service API with improved TypeScript support and a refined plugin architecture.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/strapi-headless-cms-rest-graphql/)
