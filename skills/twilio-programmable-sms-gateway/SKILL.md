---
title: "Twilio Programmable SMS Gateway"
description: "Sends and receives SMS/MMS messages via Twilio REST API with webhook handler generation. Supports message scheduling, delivery status callbacks, and Twilio Verify for OTP flows."
verification: "security_reviewed"
source: "https://github.com/twilio/twilio-node"
category:
  - "Integrations & Connectors"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "twilio/twilio-node"
  github_stars: 1528
  ase_npm_package: "twilio"
  npm_weekly_downloads: 3731324
  license: "MIT"
---

# Twilio Programmable SMS Gateway

Sends and receives SMS/MMS messages via Twilio REST API with webhook handler generation. Supports message scheduling, delivery status callbacks, and Twilio Verify for OTP flows.


This skill automates twilio programmable sms gateway operations for agent-driven workflows. It wraps the underlying API client libraries with sensible defaults for authentication, error handling, and pagination. Configuration is managed through environment variables and a local settings file, keeping credentials out of your codebase. The agent validates inputs against the provider’s API schema before making requests, catching configuration errors early. Includes retry logic with exponential backoff for transient failures and structured logging for audit trails. Works in both synchronous command mode and event-driven webhook mode for real-time integrations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-programmable-sms-gateway/)
