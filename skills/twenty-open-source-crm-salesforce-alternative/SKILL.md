---
name: "Twenty Open Source CRM Platform and Salesforce Alternative"
description: "Twenty is a modern open-source CRM built to replace Salesforce, with customizable objects, workflow automation, email and calendar integration, and a GraphQL API. It offers kanban, table, and calendar views with fine-grained permission controls and self-hosting support."
category: "Calendar, Email &amp; Productivity"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/twentyhq/twenty"
tool_ecosystem:
  github_repo: "https://github.com/twentyhq/twenty"
  github_stars: 43525
---
# Twenty Open Source CRM Platform and Salesforce Alternative

Twenty is a modern open-source CRM built to replace Salesforce, with customizable objects, workflow automation, email and calendar integration, and a GraphQL API. It offers kanban, table, and calendar views with fine-grained permission controls and self-hosting support.

Overview

Twenty is an open-source CRM platform designed as a modern alternative to Salesforce. With over 43,000 GitHub stars and backing from Y Combinator, it brings the UX patterns of tools like Notion, Airtable, and Linear to customer relationship management. The entire platform is available under the AGPLv3 license and can be self-hosted or used via their cloud offering.

How It Works

Twenty provides a flexible data model where users can create custom objects and fields to match their specific business needs. The platform supports multiple layout options including table views with filters, sorting, and grouping; kanban boards for pipeline management; and calendar views for time-based data. All data is stored in PostgreSQL and accessible through a GraphQL API.

Key Capabilities

The CRM includes contact and company management, deal pipeline tracking, email integration for syncing conversations, calendar event tracking, file attachments, and activity timelines. Workflow automation allows defining triggers and actions to streamline repetitive tasks. Custom roles and granular permissions control who can see and edit what.

Agent Integration

Twenty exposes a full GraphQL API that AI agents and coding assistants can use to query contacts, update deals, create records, and trigger workflows programmatically. The API supports standard authentication and follows GraphQL best practices with introspectable schemas, making it straightforward to generate typed clients or integrate with agent tool frameworks.

Deployment

Self-hosting is supported via Docker Compose with PostgreSQL and Redis. The project provides detailed documentation for local development setup and production deployment. The tech stack includes TypeScript, NestJS, React, BullMQ, and Nx for monorepo management.

Community and Ecosystem

Hundreds of developers contribute to Twenty actively. The project maintains a public roadmap on GitHub Projects, an active Discord community, and Figma design files for contributors. Integration with tools like Sentry for error tracking and Chromatic for UI testing demonstrates production-grade engineering practices.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill twenty-open-source-crm-salesforce-alternative
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill twenty-open-source-crm-salesforce-alternative -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill twenty-open-source-crm-salesforce-alternative -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill twenty-open-source-crm-salesforce-alternative -a codex
```

### OpenClaw

```bash
clawhub install twenty-open-source-crm-salesforce-alternative
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twenty-open-source-crm-salesforce-alternative/)
