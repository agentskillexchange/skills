---
name: "Papermark Open Source Document Sharing Platform with Analytics"
description: "Papermark is an open-source alternative to DocSend for secure document sharing with built-in page-by-page analytics, custom branding, custom domains, and self-hosting support. Built with Next.js and PostgreSQL."
category: "Integrations & Connectors"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/mfts/papermark"
tool_ecosystem:
  github_repo: "mfts/papermark"
  github_stars: 8148
---
# Papermark Open Source Document Sharing Platform with Analytics

Papermark is an open-source alternative to DocSend for secure document sharing with built-in page-by-page analytics, custom branding, custom domains, and self-hosting support. Built with Next.js and PostgreSQL.

Papermark is an open-source document-sharing platform that provides a self-hostable alternative to DocSend. It enables secure sharing of documents through custom links with built-in analytics tracking, custom domains, and branding capabilities.



Core Capabilities

The platform allows users to share documents securely by generating custom links with viewer tracking. It provides page-by-page analytics showing how recipients interact with shared documents, including time spent on each page and completion rates. Custom branding support lets organizations apply their own domain and visual identity to shared documents.



Technical Stack

Papermark is built on a modern TypeScript stack using Next.js as the framework, Prisma as the ORM with PostgreSQL for data storage, NextAuth.js for authentication, Tailwind CSS with shadcn/ui for the interface, Tinybird for analytics data processing, Resend for transactional emails, and Stripe for payment handling. It requires Node.js 18.17+ and blob storage via AWS S3 or Vercel Blob.



Data Room Features

Beyond simple document sharing, Papermark supports full data room functionality for use cases like fundraising, sales, and due diligence. Data rooms allow organizing multiple documents with granular access controls and comprehensive viewer analytics across the entire collection.



Deployment Options

Papermark can be self-hosted by cloning the repository, configuring environment variables, running Prisma migrations, and starting the development server. A hosted version is also available at papermark.com for users who prefer not to self-host. The project uses a standard npm development workflow with Prisma for database management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill papermark-document-sharing-analytics
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill papermark-document-sharing-analytics -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill papermark-document-sharing-analytics -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill papermark-document-sharing-analytics -a codex
```

### OpenClaw

```bash
clawhub install papermark-document-sharing-analytics
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/papermark-document-sharing-analytics/)
