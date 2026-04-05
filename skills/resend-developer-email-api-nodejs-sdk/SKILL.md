---
name: "Resend Developer Email API and Node.js SDK"
description: "Resend is a modern email API designed for developers, providing a clean SDK for sending transactional and marketing emails from Node.js applications. It supports React-based email templates, domain verification, and integrates with popular frameworks like Next.js, Remix, Hono, and Astro."
category: "Calendar, Email &amp; Productivity"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/resend/resend-node"
---
# Resend Developer Email API and Node.js SDK

Resend is a modern email API designed for developers, providing a clean SDK for sending transactional and marketing emails from Node.js applications. It supports React-based email templates, domain verification, and integrates with popular frameworks like Next.js, Remix, Hono, and Astro.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill resend-developer-email-api-nodejs-sdk
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill resend-developer-email-api-nodejs-sdk -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill resend-developer-email-api-nodejs-sdk -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill resend-developer-email-api-nodejs-sdk -a codex
```

### OpenClaw

```bash
clawhub install resend-developer-email-api-nodejs-sdk
```

## Details

Overview
Resend is a developer-first email sending platform that replaces legacy email services with a modern, type-safe API. The official Node.js SDK (resend on npm) provides a clean interface for sending transactional emails, batch emails, and managing domains, API keys, audiences, and contacts programmatically.

Core Capabilities
The Resend SDK enables agents and automation workflows to send emails with full programmatic control. It supports plain text, HTML, and React component-based email templates through its react property. Emails can include attachments, custom headers, reply-to addresses, and tags for tracking. The SDK also provides endpoints for managing email domains, retrieving send status, and handling bounces.

Integration Points
Resend integrates natively with the React Email component library for building responsive, dark-mode-compatible email templates using JSX. Framework-specific guides cover Next.js (App Router and Pages Router), Remix, Nuxt, Express, RedwoodJS, Hono, Bun, and Astro. The SDK works in serverless environments including AWS Lambda, Vercel Edge Functions, and Cloudflare Workers.

Agent Use Cases
AI agents can use the Resend SDK to send automated notifications, reports, alerts, and summaries via email. Common agent workflows include sending daily digest emails with curated content, triggering transactional emails based on webhook events, automating customer onboarding sequences, and delivering formatted reports from data pipelines. The type-safe TypeScript API makes it reliable for unattended automation.

Installation and Setup
Install via npm: npm install resend. Initialize with an API key from the Resend Dashboard: const resend = new Resend("re_xxxx"). Send emails with resend.emails.send({ from, to, subject, html }). The SDK requires Node.js 18+ and uses native fetch. Domain verification is required for sending from custom domains.

Key Features

Type-safe TypeScript SDK with full IntelliSense
React component email templates via the react property
Batch sending for up to 100 emails per API call
Domain management, API key rotation, and audience/contact APIs
Webhook support for delivery, bounce, and complaint events
MIT licensed Node.js SDK with active maintenance

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/resend-developer-email-api-nodejs-sdk/)
