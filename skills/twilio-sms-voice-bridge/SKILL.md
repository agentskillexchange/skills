---
name: Twilio SMS &#038; Voice Bridge
description: Connects to Twilio REST API via the twilio-node SDK for programmable
  messaging and voice. Sends SMS with client.messages.create(), builds IVR flows using
  TwiML VoiceResponse, and processes delivery webhooks for message status tracking
  and conversation threading.
verification: security_reviewed
source: https://agentskillexchange.com/skills/twilio-sms-voice-bridge/
category:
- Integrations &amp; Connectors
framework:
- OpenClaw
---
# Twilio SMS & Voice Bridge

The Twilio SMS & Voice Bridge enables programmatic communication through Twilio's messaging and voice APIs using the official twilio-node helper library. It provides both outbound messaging capabilities and inbound webhook processing for two-way communication.
SMS operations use client.messages.create() with support for standard SMS, MMS with media attachments, and WhatsApp messaging via the Twilio WhatsApp Business API. The skill handles message segmentation for long texts, tracks delivery status through StatusCallback webhooks (queued, sent, delivered, failed), and supports conversation threading with Twilio Conversations API.
Voice capabilities are built using TwiML (Twilio Markup Language). The agent constructs VoiceResponse objects to build interactive IVR menus with Gather for DTMF input, Say for text-to-speech using Amazon Polly voices, Record for voicemail capture, and Dial for call forwarding. Conference calling and call queuing are supported through respective TwiML verbs.
Advanced features include programmable voice with SIP trunking, phone number management via client.incomingPhoneNumbers, Twilio Verify for OTP/2FA flows, and Twilio Studio integration for visual flow orchestration. The skill also supports bulk messaging with Messaging Services for throughput optimization and sender pool management.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-sms-voice-bridge/)
