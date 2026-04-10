---
title: "Resend Developer Email API and Node.js SDK"
description: "Resend is a modern email API designed for developers, providing a clean SDK for sending transactional and marketing emails from Node.js applications. It supports React-based email templates, domain verification, and integrates with popular frameworks like Next.js, Remix, Hono, and Astro."
slug: "resend-developer-email-api-nodejs-sdk"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/resend/resend-node"
---

# Resend Developer Email API and Node.js SDK

Resend is a modern email API designed for developers, providing a clean SDK for sending transactional and marketing emails from Node.js applications. It supports React-based email templates, domain verification, and integrates with popular frameworks like Next.js, Remix, Hono, and Astro.

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
clawhub install resend-developer-email-api-nodejs-sdk
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

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
- Type-safe TypeScript SDK with full IntelliSense
- React component email templates via the react property
- Batch sending for up to 100 emails per API call
- Domain management, API key rotation, and audience/contact APIs
- Webhook support for delivery, bounce, and complaint events
- MIT licensed Node.js SDK with active maintenance

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/resend-developer-email-api-nodejs-sdk/)
