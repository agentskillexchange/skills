---
title: "Twilio SMS & Voice Bridge"
description: "Connects to Twilio REST API via the twilio-node SDK for programmable messaging and voice. Sends SMS with client.messages.create(), builds IVR flows using TwiML VoiceResponse, and processes delivery webhooks for message status tracking and conversation threading."
verification: "security_reviewed"
source: "https://github.com/twilio/twilio-node"
category:
  - "Integrations &amp; Connectors"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "twilio/twilio-node"
  github_stars: 1528
  ase_npm_package: "twilio"
  npm_weekly_downloads: 3731324
  license: "MIT"
---

# Twilio SMS & Voice Bridge

The Twilio SMS & Voice Bridge enables programmatic communication through Twilio’s messaging and voice APIs using the official twilio-node helper library. It provides both outbound messaging capabilities and inbound webhook processing for two-way communication.

SMS operations use client.messages.create() with support for standard SMS, MMS with media attachments, and WhatsApp messaging via the Twilio WhatsApp Business API. The skill handles message segmentation for long texts, tracks delivery status through StatusCallback webhooks (queued, sent, delivered, failed), and supports conversation threading with Twilio Conversations API.

Voice capabilities are built using TwiML (Twilio Markup Language). The agent constructs VoiceResponse objects to build interactive IVR menus with Gather for DTMF input, Say for text-to-speech using Amazon Polly voices, Record for voicemail capture, and Dial for call forwarding. Conference calling and call queuing are supported through respective TwiML verbs.

Advanced features include programmable voice with SIP trunking, phone number management via client.incomingPhoneNumbers, Twilio Verify for OTP/2FA flows, and Twilio Studio integration for visual flow orchestration. The skill also supports bulk messaging with Messaging Services for throughput optimization and sender pool management.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-sms-voice-bridge/)
