---
title: "Postmark.js Email Delivery API for Transactional Messaging"
description: "postmark.js is the official Node.js library for the Postmark API, used to send transactional email, templates, and message streams from code. It is a strong fit for skills that automate outbound notifications, email workflows, and delivery-aware application integrations."
slug: "postmarkjs-email-delivery-api-transactional-messaging"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/ActiveCampaign/postmark.js"
tool_ecosystem:
  github_repo: "ActiveCampaign/postmark.js"
  github_stars: 357
---

# Postmark.js Email Delivery API for Transactional Messaging

postmark.js is the official Node.js library for the Postmark API, used to send transactional email, templates, and message streams from code. It is a strong fit for skills that automate outbound notifications, email workflows, and delivery-aware application integrations.

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
clawhub install postmarkjs-email-delivery-api-transactional-messaging
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

postmark.js is the official Node.js client library for the Postmark API. The upstream project is maintained in the ActiveCampaign/postmark.js GitHub repository, published as the postmark npm package, and documented through the Postmark developer docs. It provides a typed, programmatic way to send transactional email, work with templates, manage message streams, and integrate Postmark delivery features into application code.
As an ASE skill, postmark.js is useful whenever an agent needs to wire a product or workflow into reliable transactional messaging instead of generic SMTP scripts. A common pattern is to install the package in a Node.js project, initialize the Postmark client with a server token, then call the send-email or template APIs from automation code, job workers, or web backends. That makes it suitable for password-reset messages, verification emails, workflow notifications, receipts, and internal status alerts.
Integration points include Node.js services, serverless handlers, queue workers, onboarding flows, and notification pipelines. Because the library is official, versioned, and documented, it gives a cleaner interface than raw HTTP calls for teams already using Postmark. In agent-oriented environments, this skill fits productivity and notification scenarios where the output is a real transactional email step backed by the Postmark platform rather than a generic mail abstraction.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postmarkjs-email-delivery-api-transactional-messaging/)
