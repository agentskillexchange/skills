---
title: "SendGrid Transactional Email Builder"
description: "The SendGrid Transactional Email Builder creates and manages transactional email workflows using SendGrid&#8217;s v3 Mail Send API. It constructs emails with dynamic template data using Handlebars syntax for personalization, handles recipient management, and provides delivery tracking. The skill uses @sendgrid/mail to send single and batch emails via sgMail.send() and sgMail.sendMultiple() . It supports dynamic templates created in SendGrid with template_id and dynamic_template_data for variable substitution. Advanced personalization includes conditional sections and iteration blocks in templates. Delivery management features include suppression group integration with asm.group_id , category tagging for analytics segmentation, and send-at scheduling with Unix timestamps. The agent parses Event Webhook payloads for delivery, open, click, bounce, and spam report events. It handles bounce management by updating suppression lists and implements exponential backoff for rate limit (429) responses. Supports sender identity verification and domain authentication status checks via the Sender Authentication API."
source: "https://github.com/sendgrid/sendgrid-nodejs"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "sendgrid/sendgrid-nodejs"
  github_stars: 3049
  npm_package: "@sendgrid/mail"
  npm_weekly_downloads: 3588681
---

# SendGrid Transactional Email Builder

The SendGrid Transactional Email Builder creates and manages transactional email workflows using SendGrid&#8217;s v3 Mail Send API. It constructs emails with dynamic template data using Handlebars syntax for personalization, handles recipient management, and provides delivery tracking. The skill uses @sendgrid/mail to send single and batch emails via sgMail.send() and sgMail.sendMultiple() . It supports dynamic templates created in SendGrid with template_id and dynamic_template_data for variable substitution. Advanced personalization includes conditional sections and iteration blocks in templates. Delivery management features include suppression group integration with asm.group_id , category tagging for analytics segmentation, and send-at scheduling with Unix timestamps. The agent parses Event Webhook payloads for delivery, open, click, bounce, and spam report events. It handles bounce management by updating suppression lists and implements exponential backoff for rate limit (429) responses. Supports sender identity verification and domain authentication status checks via the Sender Authentication API.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sendgrid-transactional-email-builder/)
