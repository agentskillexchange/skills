---
title: "SendGrid Transactional Email Router"
description: "Manages transactional email delivery via SendGrid v3 Mail Send API with dynamic template rendering. Handles bounce processing, suppression group management, and event webhook parsing."
verification: security_reviewed
source: "https://github.com/sendgrid/sendgrid-nodejs"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "sendgrid/sendgrid-nodejs"
  github_stars: 3049
  npm_package: "@sendgrid/mail"
  npm_weekly_downloads: 3588681
---

# SendGrid Transactional Email Router

Manages transactional email delivery via SendGrid v3 Mail Send API with dynamic template rendering. Handles bounce processing, suppression group management, and event webhook parsing.

This skill automates sendgrid transactional email router operations for agent-driven workflows. It wraps the underlying API client libraries with sensible defaults for authentication, error handling, and pagination. Configuration is managed through environment variables and a local settings file, keeping credentials out of your codebase. The agent validates inputs against the provider’s API schema before making requests, catching configuration errors early. Includes retry logic with exponential backoff for transient failures and structured logging for audit trails. Works in both synchronous command mode and event-driven webhook mode for real-time integrations.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sendgrid-transactional-email-router/)
