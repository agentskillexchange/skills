---
title: "KeystoneJS Headless CMS with GraphQL API and React Admin UI"
description: "KeystoneJS is a powerful open-source headless CMS for Node.js that auto-generates a GraphQL API and React-based Admin UI from your schema definition. Built by Thinkmill, it supports PostgreSQL and SQLite, custom access control, hooks, virtual fields, and document-based rich text editing."
slug: "keystonejs-headless-cms-graphql-react-admin"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/keystonejs/keystone"
listed: true
---

# KeystoneJS Headless CMS with GraphQL API and React Admin UI

KeystoneJS is a powerful open-source headless CMS for Node.js that auto-generates a GraphQL API and React-based Admin UI from your schema definition. Built by Thinkmill, it supports PostgreSQL and SQLite, custom access control, hooks, virtual fields, and document-based rich text editing.

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
clawhub install keystonejs-headless-cms-graphql-react-admin
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

KeystoneJS is a programmable headless CMS and application framework for Node.js. You define your data schema in code, and Keystone generates a complete GraphQL API and a polished React-based Admin UI automatically. Published under the @keystone-6/* namespace on npm, it is maintained by Thinkmill and has over 9,000 GitHub stars.
Schema-First Development
Keystone uses a declarative schema definition to model your content. You define lists (content types) with typed fields — text, integer, float, decimal, timestamp, select, relationship, image, file, and more. Each list automatically gets CRUD operations in the GraphQL API and a corresponding editor in the Admin UI. Virtual fields let you compute derived data at query time.
GraphQL API
The auto-generated GraphQL API supports querying, filtering, sorting, pagination, and mutations for all lists. Nested relationship queries work out of the box. The API includes built-in support for authentication and session management, with configurable access control at the list, field, and operation level.
Admin UI
The React-based Admin UI is generated from your schema and provides list views with filtering, sorting, and search; item detail views with inline editing; relationship pickers; and a document field editor for rich text. The UI is customizable through custom field views and page extensions.
Document Field
Keystone’s document field provides a structured rich text editor that stores content as a portable JSON structure rather than raw HTML. It supports inline relationships (embedding references to other Keystone items), custom component blocks, and configurable formatting options. This makes content reusable across different rendering targets.
Access Control and Hooks
Keystone provides granular access control through filter, item, and operation-level access functions. Hooks run before and after create, update, and delete operations, enabling validation, side effects, and workflow logic. Session management supports password-based auth, with extensibility for OAuth and other strategies.
Database Support
Keystone uses Prisma as its database layer, supporting PostgreSQL and SQLite. Database migrations are managed through Prisma Migrate, providing schema versioning and safe deployments.
Getting Started
Create a new project with npx create-keystone-app@latest. The CLI scaffolds a project with a working schema, Admin UI, and GraphQL playground. Documentation, examples, and API reference are available at keystonejs.com/docs. The source code is MIT-licensed at github.com/keystonejs/keystone.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keystonejs-headless-cms-graphql-react-admin/)
