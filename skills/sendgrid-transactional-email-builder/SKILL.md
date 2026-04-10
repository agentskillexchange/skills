---
name: "SendGrid Transactional Email Builder"
description: "Constructs and sends transactional emails using the SendGrid v3 Mail Send API. Builds dynamic templates with Handlebars substitutions, manages suppression groups, and tracks delivery via Event Webhook parsing."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sendgrid-transactional-email-builder/"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
---

# SendGrid Transactional Email Builder

The SendGrid Transactional Email Builder creates and manages transactional email workflows using SendGrid's v3 Mail Send API. It constructs emails with dynamic template data using Handlebars syntax for personalization, handles recipient management, and provides delivery tracking.
The skill uses @sendgrid/mail to send single and batch emails via sgMail.send() and sgMail.sendMultiple(). It supports dynamic templates created in SendGrid with template_id and dynamic_template_data for variable substitution. Advanced personalization includes conditional sections and iteration blocks in templates.
Delivery management features include suppression group integration with asm.group_id, category tagging for analytics segmentation, and send-at scheduling with Unix timestamps. The agent parses Event Webhook payloads for delivery, open, click, bounce, and spam report events. It handles bounce management by updating suppression lists and implements exponential backoff for rate limit (429) responses. Supports sender identity verification and domain authentication status checks via the Sender Authentication API.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sendgrid-transactional-email-builder/)
