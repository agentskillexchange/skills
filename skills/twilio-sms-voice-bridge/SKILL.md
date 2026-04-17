---
title: "Twilio SMS & Voice Bridge"
description: "Connects to Twilio REST API via the twilio-node SDK for programmable messaging and voice. Sends SMS with client.messages.create(), builds IVR flows using TwiML VoiceResponse, and processes delivery webhooks for message status tracking and conversation threading."
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
  license: "MIT"
---

# Twilio SMS & Voice Bridge

The Twilio SMS & Voice Bridge enables programmatic communication through Twilio’s messaging and voice APIs using the official twilio-node helper library. It provides both outbound messaging capabilities and inbound webhook processing for two-way communication.

SMS operations use client.messages.create() with support for standard SMS, MMS with media attachments, and WhatsApp messaging via the Twilio WhatsApp Business API. The skill handles message segmentation for long texts, tracks delivery status through StatusCallback webhooks (queued, sent, delivered, failed), and supports conversation threading with Twilio Conversations API.

Voice capabilities are built using TwiML (Twilio Markup Language). The agent constructs VoiceResponse objects to build interactive IVR menus with Gather for DTMF input, Say for text-to-speech using Amazon Polly voices, Record for voicemail capture, and Dial for call forwarding. Conference calling and call queuing are supported through respective TwiML verbs.

Advanced features include programmable voice with SIP trunking, phone number management via client.incomingPhoneNumbers, Twilio Verify for OTP/2FA flows, and Twilio Studio integration for visual flow orchestration. The skill also supports bulk messaging with Messaging Services for throughput optimization and sender pool management.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/twilio-sms-voice-bridge
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/twilio-sms-voice-bridge` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-sms-voice-bridge/)
