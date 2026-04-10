---
title: "SendGrid Transactional Email Router"
description: "Manages transactional email delivery via SendGrid v3 Mail Send API with dynamic template rendering. Handles bounce processing, suppression group management, and event webhook parsing."
slug: "sendgrid-transactional-email-router"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sendgrid-transactional-email-router/"
---

# SendGrid Transactional Email Router

Manages transactional email delivery via SendGrid v3 Mail Send API with dynamic template rendering. Handles bounce processing, suppression group management, and event webhook parsing.

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
clawhub install sendgrid-transactional-email-router
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill automates sendgrid transactional email router operations for agent-driven workflows. It wraps the underlying API client libraries with sensible defaults for authentication, error handling, and pagination. Configuration is managed through environment variables and a local settings file, keeping credentials out of your codebase. The agent validates inputs against the provider’s API schema before making requests, catching configuration errors early. Includes retry logic with exponential backoff for transient failures and structured logging for audit trails. Works in both synchronous command mode and event-driven webhook mode for real-time integrations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sendgrid-transactional-email-router/)
