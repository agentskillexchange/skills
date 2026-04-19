---
title: "Payload CMS Next.js-Native Headless CMS and Application Framework"
description: "Payload CMS is an open-source headless content management system and application framework built on Next.js and TypeScript. With over 30,000 GitHub stars, it distinguishes itself as the first CMS that installs directly into an existing Next.js /app folder, sharing the same server process, database connection, and deployment pipeline as the frontend application. Payload auto-generates REST and GraphQL APIs, a full admin panel with live preview, and TypeScript types from collection and global configuration files. Collections define repeatable content types (blog posts, products, users), while Globals define singleton data (site settings, navigation). Each collection receives full CRUD endpoints with filtering, sorting, pagination, and depth-based population of relationships. A skill built around Payload enables agents to scaffold new CMS-backed applications, define content schemas programmatically, manage content entries and media, configure access control policies, and deploy fullstack applications. The create-payload-app CLI bootstraps projects with database adapter selection (MongoDB via Mongoose or PostgreSQL/SQLite via Drizzle ORM). Key features include: field-level access control with row and cell-level conditions, lexical rich text editor with custom blocks and inline elements, version history and draft/publish workflow, file uploads with image resizing and focal point cropping, authentication with email verification and password reset, and hooks (beforeChange, afterRead, etc.) for custom business logic at every lifecycle point. Integration points for agent workflows include: automating content model definition and migration, synchronizing content between environments, managing media libraries, implementing custom API endpoints via Next.js route handlers, configuring webhooks for content events, and deploying Payload applications to Vercel, AWS, or self-hosted infrastructure. The Local API provides direct server-side access without HTTP overhead for background jobs and data processing tasks."
source: "https://github.com/payloadcms/payload"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "payloadcms/payload"
  github_stars: 41552
  npm_package: "payload"
  npm_weekly_downloads: 306473
---

# Payload CMS Next.js-Native Headless CMS and Application Framework

Payload CMS is an open-source headless content management system and application framework built on Next.js and TypeScript. With over 30,000 GitHub stars, it distinguishes itself as the first CMS that installs directly into an existing Next.js /app folder, sharing the same server process, database connection, and deployment pipeline as the frontend application. Payload auto-generates REST and GraphQL APIs, a full admin panel with live preview, and TypeScript types from collection and global configuration files. Collections define repeatable content types (blog posts, products, users), while Globals define singleton data (site settings, navigation). Each collection receives full CRUD endpoints with filtering, sorting, pagination, and depth-based population of relationships. A skill built around Payload enables agents to scaffold new CMS-backed applications, define content schemas programmatically, manage content entries and media, configure access control policies, and deploy fullstack applications. The create-payload-app CLI bootstraps projects with database adapter selection (MongoDB via Mongoose or PostgreSQL/SQLite via Drizzle ORM). Key features include: field-level access control with row and cell-level conditions, lexical rich text editor with custom blocks and inline elements, version history and draft/publish workflow, file uploads with image resizing and focal point cropping, authentication with email verification and password reset, and hooks (beforeChange, afterRead, etc.) for custom business logic at every lifecycle point. Integration points for agent workflows include: automating content model definition and migration, synchronizing content between environments, managing media libraries, implementing custom API endpoints via Next.js route handlers, configuring webhooks for content events, and deploying Payload applications to Vercel, AWS, or self-hosted infrastructure. The Local API provides direct server-side access without HTTP overhead for background jobs and data processing tasks.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/payload-cms-nextjs-headless-framework/)
