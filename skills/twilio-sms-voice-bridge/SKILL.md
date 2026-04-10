---
title: "Twilio SMS & Voice Bridge"
description: "Connects to Twilio REST API via the twilio-node SDK for programmable messaging and voice. Sends SMS with client.messages.create(), builds IVR flows using TwiML VoiceResponse, and processes delivery webhooks for message status tracking and conversation threading."
slug: "twilio-sms-voice-bridge"
category:
  - "Integrations &amp; Connectors"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/twilio-sms-voice-bridge/"
---

# Twilio SMS & Voice Bridge

Connects to Twilio REST API via the twilio-node SDK for programmable messaging and voice. Sends SMS with client.messages.create(), builds IVR flows using TwiML VoiceResponse, and processes delivery webhooks for message status tracking and conversation threading.

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
clawhub install twilio-sms-voice-bridge
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Twilio SMS & Voice Bridge enables programmatic communication through Twilio’s messaging and voice APIs using the official twilio-node helper library. It provides both outbound messaging capabilities and inbound webhook processing for two-way communication.
SMS operations use client.messages.create() with support for standard SMS, MMS with media attachments, and WhatsApp messaging via the Twilio WhatsApp Business API. The skill handles message segmentation for long texts, tracks delivery status through StatusCallback webhooks (queued, sent, delivered, failed), and supports conversation threading with Twilio Conversations API.
Voice capabilities are built using TwiML (Twilio Markup Language). The agent constructs VoiceResponse objects to build interactive IVR menus with Gather for DTMF input, Say for text-to-speech using Amazon Polly voices, Record for voicemail capture, and Dial for call forwarding. Conference calling and call queuing are supported through respective TwiML verbs.
Advanced features include programmable voice with SIP trunking, phone number management via client.incomingPhoneNumbers, Twilio Verify for OTP/2FA flows, and Twilio Studio integration for visual flow orchestration. The skill also supports bulk messaging with Messaging Services for throughput optimization and sender pool management.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-sms-voice-bridge/)
