---
name: "Payload CMS Next.js-Native Headless CMS and Application Framework"
description: "Payload is an open-source, TypeScript-first headless CMS that installs directly into a Next.js application. It provides a full admin panel, REST and GraphQL APIs, access control, file uploads, and rich text editing with zero separate backend required."
category: "WordPress &amp; CMS"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/payloadcms/payload"
tool_ecosystem:
  github_repo: "payloadcms/payload"
  github_stars: 41552
  npm_package: "payload"
  npm_weekly_downloads: 316489
  license: "MIT"
---
# Payload CMS Next.js-Native Headless CMS and Application Framework

Payload is an open-source, TypeScript-first headless CMS that installs directly into a Next.js application. It provides a full admin panel, REST and GraphQL APIs, access control, file uploads, and rich text editing with zero separate backend required.

Payload CMS is an open-source headless content management system and application framework built on Next.js and TypeScript. With over 30,000 GitHub stars, it distinguishes itself as the first CMS that installs directly into an existing Next.js /app folder, sharing the same server process, database connection, and deployment pipeline as the frontend application.

Payload auto-generates REST and GraphQL APIs, a full admin panel with live preview, and TypeScript types from collection and global configuration files. Collections define repeatable content types (blog posts, products, users), while Globals define singleton data (site settings, navigation). Each collection receives full CRUD endpoints with filtering, sorting, pagination, and depth-based population of relationships.

A skill built around Payload enables agents to scaffold new CMS-backed applications, define content schemas programmatically, manage content entries and media, configure access control policies, and deploy fullstack applications. The create-payload-app CLI bootstraps projects with database adapter selection (MongoDB via Mongoose or PostgreSQL/SQLite via Drizzle ORM).

Key features include: field-level access control with row and cell-level conditions, lexical rich text editor with custom blocks and inline elements, version history and draft/publish workflow, file uploads with image resizing and focal point cropping, authentication with email verification and password reset, and hooks (beforeChange, afterRead, etc.) for custom business logic at every lifecycle point.

Integration points for agent workflows include: automating content model definition and migration, synchronizing content between environments, managing media libraries, implementing custom API endpoints via Next.js route handlers, configuring webhooks for content events, and deploying Payload applications to Vercel, AWS, or self-hosted infrastructure. The Local API provides direct server-side access without HTTP overhead for background jobs and data processing tasks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill payload-cms-nextjs-headless-framework
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill payload-cms-nextjs-headless-framework -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill payload-cms-nextjs-headless-framework -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill payload-cms-nextjs-headless-framework -a codex
```

### OpenClaw

```bash
clawhub install payload-cms-nextjs-headless-framework
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/payload-cms-nextjs-headless-framework/)
