---
title: "Twilio Programmable SMS Gateway"
description: "Sends and receives SMS/MMS messages via Twilio REST API with webhook handler generation. Supports message scheduling, delivery status callbacks, and Twilio Verify for OTP flows."
verification: security_reviewed
source: "https://github.com/twilio/twilio-node"
category:
  - "Integrations & Connectors"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "twilio/twilio-node"
  github_stars: 1528
  npm_package: "twilio"
  npm_weekly_downloads: 3731324
---

# Twilio Programmable SMS Gateway

Sends and receives SMS/MMS messages via Twilio REST API with webhook handler generation. Supports message scheduling, delivery status callbacks, and Twilio Verify for OTP flows.

This skill automates twilio programmable sms gateway operations for agent-driven workflows. It wraps the underlying API client libraries with sensible defaults for authentication, error handling, and pagination. Configuration is managed through environment variables and a local settings file, keeping credentials out of your codebase. The agent validates inputs against the provider’s API schema before making requests, catching configuration errors early. Includes retry logic with exponential backoff for transient failures and structured logging for audit trails. Works in both synchronous command mode and event-driven webhook mode for real-time integrations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/twilio-programmable-sms-gateway
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/twilio-programmable-sms-gateway` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-programmable-sms-gateway/)
