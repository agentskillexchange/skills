---
name: "Plunk Open Source Transactional Email Platform on AWS SES"
description: "Plunk is an open-source email platform built on AWS SES for sending transactional emails, creating event-driven automations, and broadcasting newsletters. It serves as a self-hosted alternative to SendGrid, Resend, and Mailgun."
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/useplunk/plunk"
tool_ecosystem:
  github_repo: useplunk/plunk
  github_stars: 4948
---
# Plunk Open Source Transactional Email Platform on AWS SES

Plunk is an open-source email platform built on AWS SES for sending transactional emails, creating event-driven automations, and broadcasting newsletters. It serves as a self-hosted alternative to SendGrid, Resend, and Mailgun.

## Overview

Plunk is an open-source email platform built on top of Amazon SES that provides transactional email sending, event-driven automations, and broadcast capabilities. Licensed under AGPL-3.0 with nearly 5,000 GitHub stars, it offers a self-hosted alternative to commercial email services like SendGrid, Resend, and Mailgun.

Transactional Email API

Plunk provides a REST API for sending transactional emails directly from applications. The API accepts HTML content or template references, recipient details, and metadata. Each sent email is tracked with delivery status, open rates, and click tracking. The API supports both single sends and batch operations for high-volume use cases.

Event-Driven Automations

The automation system lets teams define email sequences triggered by custom events. When your application fires an event (e.g., user.signup, order.completed, subscription.cancelled), Plunk matches it against configured automation rules and sends the appropriate email or sequence. Automations support delays, conditions, and branching logic to create sophisticated email workflows without code changes.

Broadcast Campaigns

Plunk includes a broadcast feature for sending newsletters, product updates, and announcements to large audiences. The broadcast editor supports HTML templates with merge tags for personalization. Campaigns can be segmented by user attributes and events, ensuring relevant content reaches the right audience.

Contact Management

The platform maintains a contact database that tracks user attributes, event history, and email engagement metrics. Contacts are automatically created when events are triggered, and their profiles accumulate interaction data over time. This data powers segmentation rules for both automations and broadcasts.

Self-Hosting with Docker

Plunk is distributed as a Docker image (`driaug/plunk`) available on Docker Hub. The self-hosting setup requires an AWS SES account for email delivery, a PostgreSQL database for data storage, and Redis for queue management. Configuration is done through environment variables for SES credentials, database connection, and application settings. The Docker image includes the API server, web dashboard, and background worker processes.

AWS SES Integration

By building directly on AWS SES, Plunk inherits its deliverability infrastructure, compliance capabilities, and cost model. SES handles DKIM signing, bounce processing, and complaint handling. Teams benefit from AWS’s email sending reputation while maintaining full control over their email platform logic and data.

Agent Integration Potential

AI agents can leverage the Plunk API to send transactional notifications as part of automated workflows, trigger event-based email sequences when specific conditions are met, and manage broadcast campaigns programmatically. The event-driven architecture aligns well with agent-based systems where actions in one system should trigger email communications in another.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill plunk-open-source-email-platform-aws-ses
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill plunk-open-source-email-platform-aws-ses -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill plunk-open-source-email-platform-aws-ses -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill plunk-open-source-email-platform-aws-ses -a codex
```

### OpenClaw

```bash
clawhub install plunk-open-source-email-platform-aws-ses
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plunk-open-source-email-platform-aws-ses/)
