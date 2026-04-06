---
name: Twilio Programmable SMS Gateway
description: Sends and receives SMS/MMS messages via Twilio REST API with webhook
  handler generation. Supports message scheduling, delivery status callbacks, and
  Twilio Verify for OTP flows.
category: "Integrations &amp; Connectors"
framework: OpenClaw
verification: security_reviewed
source: "https://agentskillexchange.com/skills/twilio-programmable-sms-gateway/"
---
# Twilio Programmable SMS Gateway

Sends and receives SMS/MMS messages via Twilio REST API with webhook handler generation. Supports message scheduling, delivery status callbacks, and Twilio Verify for OTP flows.

This skill automates twilio programmable sms gateway operations for agent-driven workflows. It wraps the underlying API client libraries with sensible defaults for authentication, error handling, and pagination. Configuration is managed through environment variables and a local settings file, keeping credentials out of your codebase. The agent validates inputs against the provider’s API schema before making requests, catching configuration errors early. Includes retry logic with exponential backoff for transient failures and structured logging for audit trails. Works in both synchronous command mode and event-driven webhook mode for real-time integrations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill twilio-programmable-sms-gateway
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill twilio-programmable-sms-gateway -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill twilio-programmable-sms-gateway -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill twilio-programmable-sms-gateway -a codex
```

### OpenClaw

```bash
clawhub install twilio-programmable-sms-gateway
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-programmable-sms-gateway/)
