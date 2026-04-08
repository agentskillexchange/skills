---
title: Novu Open-Source Notification Infrastructure Platform
description: What is Novu? Novu is an open-source notification infrastructure platform
  designed for developers who need to manage multi-channel notification delivery at
  scale. Rather than building separate integrations for email, SMS, push notifications,
  in-app messages, and chat platforms, Novu provides a single API and workflow engine
  that orchestrates delivery across all channels simultaneously. How It Works Novu
  operates through a workflow-based model where developers define notification templates
  that specify content and delivery rules for each channel. When a notification is
  triggered via the Novu API or SDK, the workflow engine evaluates subscriber preferences,
  applies digest rules (batching multiple events into a single notification), and
  routes the message through the appropriate provider for each channel. The platform
  supports over 60 notification providers out of the box, including SendGrid, Mailgun,
  Twilio, Firebase Cloud Messaging, Slack, Discord, and Microsoft Teams. Adding a
  new provider is a matter of configuration — no code changes required for supported
  integrations. Key Features The embeddable Inbox component is one of Novu’s standout
  features. It provides a drop-in React component that gives applications a fully
  functional in-app notification center with real-time updates, read/unread tracking,
  and subscriber preference management. The Inbox renders notifications with customizable
  templates and supports actions like marking as read, archiving, and custom click
  handlers. The Digest Engine intelligently batches notifications — for example, instead
  of sending 50 individual “new comment” emails, it combines them into a single digest
  delivered on a configurable schedule. The workflow engine supports conditional logic,
  delays, and multi-step sequences. Architecture and Deployment Novu is built with
  TypeScript and Node.js, using MongoDB for persistence and Redis for queuing and
  caching. The platform can be self-hosted via Docker Compose or deployed on Kubernetes.
  Novu also offers a managed cloud service for teams that prefer not to operate the
  infrastructure themselves. Official SDKs are available for Node.js, Python, Go,
  Ruby, Java, Kotlin, PHP, and .NET. The REST API is fully documented with OpenAPI
  specifications, making integration straightforward from any language. Integration
  Points for Agents For AI agent workflows, Novu serves as the notification layer
  that handles the complexity of multi-channel delivery. An agent can trigger a Novu
  workflow with a single API call, and Novu handles subscriber preferences, channel
  routing, content rendering, and delivery tracking. This is particularly useful for
  alerting systems, user engagement flows, and any automation that needs to reliably
  reach humans across their preferred channels.
verification: security_reviewed
source: https://github.com/novuhq/novu
category:
- Integrations &amp; Connectors
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: novuhq/novu
  github_stars: 38747
  npm_package: novu
  npm_weekly_downloads: 6201
---

# Novu Open-Source Notification Infrastructure Platform

What is Novu? Novu is an open-source notification infrastructure platform designed for developers who need to manage multi-channel notification delivery at scale. Rather than building separate integrations for email, SMS, push notifications, in-app messages, and chat platforms, Novu provides a single API and workflow engine that orchestrates delivery across all channels simultaneously. How It Works Novu operates through a workflow-based model where developers define notification templates that specify content and delivery rules for each channel. When a notification is triggered via the Novu API or SDK, the workflow engine evaluates subscriber preferences, applies digest rules (batching multiple events into a single notification), and routes the message through the appropriate provider for each channel. The platform supports over 60 notification providers out of the box, including SendGrid, Mailgun, Twilio, Firebase Cloud Messaging, Slack, Discord, and Microsoft Teams. Adding a new provider is a matter of configuration — no code changes required for supported integrations. Key Features The embeddable Inbox component is one of Novu’s standout features. It provides a drop-in React component that gives applications a fully functional in-app notification center with real-time updates, read/unread tracking, and subscriber preference management. The Inbox renders notifications with customizable templates and supports actions like marking as read, archiving, and custom click handlers. The Digest Engine intelligently batches notifications — for example, instead of sending 50 individual “new comment” emails, it combines them into a single digest delivered on a configurable schedule. The workflow engine supports conditional logic, delays, and multi-step sequences. Architecture and Deployment Novu is built with TypeScript and Node.js, using MongoDB for persistence and Redis for queuing and caching. The platform can be self-hosted via Docker Compose or deployed on Kubernetes. Novu also offers a managed cloud service for teams that prefer not to operate the infrastructure themselves. Official SDKs are available for Node.js, Python, Go, Ruby, Java, Kotlin, PHP, and .NET. The REST API is fully documented with OpenAPI specifications, making integration straightforward from any language. Integration Points for Agents For AI agent workflows, Novu serves as the notification layer that handles the complexity of multi-channel delivery. An agent can trigger a Novu workflow with a single API call, and Novu handles subscriber preferences, channel routing, content rendering, and delivery tracking. This is particularly useful for alerting systems, user engagement flows, and any automation that needs to reliably reach humans across their preferred channels.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/novu-open-source-notification-infrastructure-platform/)
