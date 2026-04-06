---
name: "Chatwoot Open Source Customer Engagement and Omnichannel Support Platform"
description: "Chatwoot is a self-hosted, open-source customer engagement platform that provides live chat, email, social media, and messaging channel support in a unified agent dashboard. It serves as an alternative to Intercom, Zendesk, and Freshdesk with full API access for automation."
category: "Integrations &amp; Connectors"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/chatwoot/chatwoot"
---
# Chatwoot Open Source Customer Engagement and Omnichannel Support Platform

Chatwoot is a self-hosted, open-source customer engagement platform that provides live chat, email, social media, and messaging channel support in a unified agent dashboard. It serves as an alternative to Intercom, Zendesk, and Freshdesk with full API access for automation.

Chatwoot is an open-source customer engagement platform built with Ruby on Rails and Vue.js that unifies conversations from live chat, email, Facebook, Twitter, WhatsApp, Telegram, Line, SMS, and API channels into a single agent dashboard. With over 28,000 GitHub stars and active development, it has become the leading open-source alternative to proprietary helpdesk platforms like Intercom, Zendesk, and Freshdesk.

Core Capabilities

The platform provides a comprehensive REST API and webhook system that enables AI agents to automate customer support workflows. Agents can create and manage conversations, send messages, assign teams, apply labels, and trigger automations programmatically. The API supports both agent-facing and contact-facing operations, making it suitable for building chatbots, automated triage systems, and customer intelligence pipelines.

Integration Architecture

Chatwoot supports channel adapters for website live chat (via an embeddable JavaScript widget), email (IMAP/SMTP), Facebook Messenger, Twitter DMs, WhatsApp Business API, Telegram Bot API, Line, SMS (via Twilio), and custom API channels. Each channel can be configured with its own inbox, team assignments, and automation rules. Webhooks fire on message creation, conversation status changes, and contact events, allowing external systems to react in real time.

Self-Hosted Deployment

Chatwoot can be deployed via Docker, Docker Compose, Helm charts for Kubernetes, or directly on Linux servers. It requires PostgreSQL and Redis as backing services. The platform includes built-in support for object storage (S3-compatible), Sidekiq for background job processing, and ActionCable for real-time WebSocket connections. Environment configuration covers SMTP, storage, Sentry error tracking, and third-party integrations.

Agent Automation Use Cases

AI coding agents can integrate Chatwoot to build automated customer support systems: routing incoming messages to appropriate teams based on content analysis, generating suggested replies using LLMs, creating knowledge base articles from resolved conversations, syncing customer data with CRMs, and monitoring conversation metrics for SLA compliance. The webhook + API combination provides the foundation for event-driven customer support automation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill chatwoot-open-source-customer-engagement-omnichannel-support
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill chatwoot-open-source-customer-engagement-omnichannel-support -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill chatwoot-open-source-customer-engagement-omnichannel-support -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill chatwoot-open-source-customer-engagement-omnichannel-support -a codex
```

### OpenClaw

```bash
clawhub install chatwoot-open-source-customer-engagement-omnichannel-support
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chatwoot-open-source-customer-engagement-omnichannel-support/)
