---
title: "Resend Developer Email API and Node.js SDK"
description: "Overview Resend is a developer-first email sending platform that replaces legacy email services with a modern, type-safe API. The official Node.js SDK ( resend on npm) provides a clean interface for sending transactional emails, batch emails, and managing domains, API keys, audiences, and contacts programmatically. Core Capabilities The Resend SDK enables agents and automation workflows to send emails with full programmatic control. It supports plain text, HTML, and React component-based email templates through its react property. Emails can include attachments, custom headers, reply-to addresses, and tags for tracking. The SDK also provides endpoints for managing email domains, retrieving send status, and handling bounces. Integration Points Resend integrates natively with the React Email component library for building responsive, dark-mode-compatible email templates using JSX. Framework-specific guides cover Next.js (App Router and Pages Router), Remix, Nuxt, Express, RedwoodJS, Hono, Bun, and Astro. The SDK works in serverless environments including AWS Lambda, Vercel Edge Functions, and Cloudflare Workers. Agent Use Cases AI agents can use the Resend SDK to send automated notifications, reports, alerts, and summaries via email. Common agent workflows include sending daily digest emails with curated content, triggering transactional emails based on webhook events, automating customer onboarding sequences, and delivering formatted reports from data pipelines. The type-safe TypeScript API makes it reliable for unattended automation. Installation and Setup Install via npm: npm install resend . Initialize with an API key from the Resend Dashboard: const resend = new Resend(\"re_xxxx\") . Send emails with resend.emails.send({ from, to, subject, html }) . The SDK requires Node.js 18+ and uses native fetch. Domain verification is required for sending from custom domains. Key Features Type-safe TypeScript SDK with full IntelliSense React component email templates via the react property Batch sending for up to 100 emails per API call Domain management, API key rotation, and audience/contact APIs Webhook support for delivery, bounce, and complaint events MIT licensed Node.js SDK with active maintenance"
source: "https://github.com/resend/resend-node"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "resend/resend-node"
  github_stars: 887
---

# Resend Developer Email API and Node.js SDK

Overview Resend is a developer-first email sending platform that replaces legacy email services with a modern, type-safe API. The official Node.js SDK ( resend on npm) provides a clean interface for sending transactional emails, batch emails, and managing domains, API keys, audiences, and contacts programmatically. Core Capabilities The Resend SDK enables agents and automation workflows to send emails with full programmatic control. It supports plain text, HTML, and React component-based email templates through its react property. Emails can include attachments, custom headers, reply-to addresses, and tags for tracking. The SDK also provides endpoints for managing email domains, retrieving send status, and handling bounces. Integration Points Resend integrates natively with the React Email component library for building responsive, dark-mode-compatible email templates using JSX. Framework-specific guides cover Next.js (App Router and Pages Router), Remix, Nuxt, Express, RedwoodJS, Hono, Bun, and Astro. The SDK works in serverless environments including AWS Lambda, Vercel Edge Functions, and Cloudflare Workers. Agent Use Cases AI agents can use the Resend SDK to send automated notifications, reports, alerts, and summaries via email. Common agent workflows include sending daily digest emails with curated content, triggering transactional emails based on webhook events, automating customer onboarding sequences, and delivering formatted reports from data pipelines. The type-safe TypeScript API makes it reliable for unattended automation. Installation and Setup Install via npm: npm install resend . Initialize with an API key from the Resend Dashboard: const resend = new Resend("re_xxxx") . Send emails with resend.emails.send({ from, to, subject, html }) . The SDK requires Node.js 18+ and uses native fetch. Domain verification is required for sending from custom domains. Key Features Type-safe TypeScript SDK with full IntelliSense React component email templates via the react property Batch sending for up to 100 emails per API call Domain management, API key rotation, and audience/contact APIs Webhook support for delivery, bounce, and complaint events MIT licensed Node.js SDK with active maintenance

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/resend-developer-email-api-nodejs-sdk/)
