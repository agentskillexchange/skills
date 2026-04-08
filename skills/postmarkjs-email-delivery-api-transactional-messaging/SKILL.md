---
title: Postmark.js Email Delivery API for Transactional Messaging
description: postmark.js is the official Node.js client library for the Postmark API
  . The upstream project is maintained in the ActiveCampaign/postmark.js GitHub repository,
  published as the postmark npm package, and documented through the Postmark developer
  docs. It provides a typed, programmatic way to send transactional email, work with
  templates, manage message streams, and integrate Postmark delivery features into
  application code. As an ASE skill, postmark.js is useful whenever an agent needs
  to wire a product or workflow into reliable transactional messaging instead of generic
  SMTP scripts. A common pattern is to install the package in a Node.js project, initialize
  the Postmark client with a server token, then call the send-email or template APIs
  from automation code, job workers, or web backends. That makes it suitable for password-reset
  messages, verification emails, workflow notifications, receipts, and internal status
  alerts. Integration points include Node.js services, serverless handlers, queue
  workers, onboarding flows, and notification pipelines. Because the library is official,
  versioned, and documented, it gives a cleaner interface than raw HTTP calls for
  teams already using Postmark. In agent-oriented environments, this skill fits productivity
  and notification scenarios where the output is a real transactional email step backed
  by the Postmark platform rather than a generic mail abstraction.
verification: security_reviewed
source: https://github.com/ActiveCampaign/postmark.js
category:
- Calendar, Email &amp; Productivity
framework:
- Multi-Framework
---

# Postmark.js Email Delivery API for Transactional Messaging

postmark.js is the official Node.js client library for the Postmark API . The upstream project is maintained in the ActiveCampaign/postmark.js GitHub repository, published as the postmark npm package, and documented through the Postmark developer docs. It provides a typed, programmatic way to send transactional email, work with templates, manage message streams, and integrate Postmark delivery features into application code. As an ASE skill, postmark.js is useful whenever an agent needs to wire a product or workflow into reliable transactional messaging instead of generic SMTP scripts. A common pattern is to install the package in a Node.js project, initialize the Postmark client with a server token, then call the send-email or template APIs from automation code, job workers, or web backends. That makes it suitable for password-reset messages, verification emails, workflow notifications, receipts, and internal status alerts. Integration points include Node.js services, serverless handlers, queue workers, onboarding flows, and notification pipelines. Because the library is official, versioned, and documented, it gives a cleaner interface than raw HTTP calls for teams already using Postmark. In agent-oriented environments, this skill fits productivity and notification scenarios where the output is a real transactional email step backed by the Postmark platform rather than a generic mail abstraction.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postmarkjs-email-delivery-api-transactional-messaging/)
