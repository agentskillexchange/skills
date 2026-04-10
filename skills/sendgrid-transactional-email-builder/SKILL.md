---
title: "SendGrid Transactional Email Builder"
description: "Constructs and sends transactional emails using the SendGrid v3 Mail Send API. Builds dynamic templates with Handlebars substitutions, manages suppression groups, and tracks delivery via Event Webhook parsing."
slug: "sendgrid-transactional-email-builder"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sendgrid-transactional-email-builder/"
---

# SendGrid Transactional Email Builder

Constructs and sends transactional emails using the SendGrid v3 Mail Send API. Builds dynamic templates with Handlebars substitutions, manages suppression groups, and tracks delivery via Event Webhook parsing.

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
clawhub install sendgrid-transactional-email-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SendGrid Transactional Email Builder creates and manages transactional email workflows using SendGrid’s v3 Mail Send API. It constructs emails with dynamic template data using Handlebars syntax for personalization, handles recipient management, and provides delivery tracking.
The skill uses @sendgrid/mail to send single and batch emails via sgMail.send() and sgMail.sendMultiple(). It supports dynamic templates created in SendGrid with template_id and dynamic_template_data for variable substitution. Advanced personalization includes conditional sections and iteration blocks in templates.
Delivery management features include suppression group integration with asm.group_id, category tagging for analytics segmentation, and send-at scheduling with Unix timestamps. The agent parses Event Webhook payloads for delivery, open, click, bounce, and spam report events. It handles bounce management by updating suppression lists and implements exponential backoff for rate limit (429) responses. Supports sender identity verification and domain authentication status checks via the Sender Authentication API.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sendgrid-transactional-email-builder/)
