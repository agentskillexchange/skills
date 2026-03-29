---
name: "Twilio SMS & Voice Bridge"
description: "Connects to Twilio REST API via the twilio-node SDK for programmable messaging and voice. Sends SMS with client.messages.create(), builds IVR flows using TwiML VoiceResponse, and processes delivery webhooks for message status tracking and conversation threading."
category: "Integrations & Connectors"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/twilio/twilio-node"
tool_ecosystem:
  tool: twilio
  github_stars: 1523
  npm_weekly_downloads: 3810383
  github_repo: twilio/twilio-node
  license: MIT
  maintained: true
---
# Twilio SMS & Voice Bridge

Connects to Twilio REST API via the twilio-node SDK for programmable messaging and voice. Sends SMS with client.messages.create(), builds IVR flows using TwiML VoiceResponse, and processes delivery webhooks for message status tracking and conversation threading.

## Overview

The Twilio SMS & Voice Bridge enables programmatic communication through Twilio’s messaging and voice APIs using the official twilio-node helper library. It provides both outbound messaging capabilities and inbound webhook processing for two-way communication.

SMS operations use client.messages.create() with support for standard SMS, MMS with media attachments, and WhatsApp messaging via the Twilio WhatsApp Business API. The skill handles message segmentation for long texts, tracks delivery status through StatusCallback webhooks (queued, sent, delivered, failed), and supports conversation threading with Twilio Conversations API.

Voice capabilities are built using TwiML (Twilio Markup Language). The agent constructs VoiceResponse objects to build interactive IVR menus with Gather for DTMF input, Say for text-to-speech using Amazon Polly voices, Record for voicemail capture, and Dial for call forwarding. Conference calling and call queuing are supported through respective TwiML verbs.

Advanced features include programmable voice with SIP trunking, phone number management via client.incomingPhoneNumbers, Twilio Verify for OTP/2FA flows, and Twilio Studio integration for visual flow orchestration. The skill also supports bulk messaging with Messaging Services for throughput optimization and sender pool management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill twilio-sms-voice-bridge
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill twilio-sms-voice-bridge -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill twilio-sms-voice-bridge -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill twilio-sms-voice-bridge -a codex
```

### OpenClaw

```bash
clawhub install twilio-sms-voice-bridge
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-sms-voice-bridge/)
