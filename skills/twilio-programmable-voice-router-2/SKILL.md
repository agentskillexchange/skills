---
title: "Twilio Programmable Voice Router"
description: "Builds intelligent voice routing flows using the Twilio Programmable Voice API. Generates TwiML responses with , , and verbs, and manages call recordings via the Recordings REST resource."
slug: "twilio-programmable-voice-router-2"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/twilio-programmable-voice-router-2/"
listed: true
---

# Twilio Programmable Voice Router

Builds intelligent voice routing flows using the Twilio Programmable Voice API. Generates TwiML responses with , , and verbs, and manages call recordings via the Recordings REST resource.

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
clawhub install twilio-programmable-voice-router-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Twilio Programmable Voice Router creates sophisticated call handling workflows using Twilio’s Programmable Voice API. It generates dynamic TwiML documents that chain for DTMF/speech input, for call forwarding with SIP and Client endpoints, and for queue-based routing.
The skill manages the full call lifecycle: incoming call webhook handling, real-time call modification via the Calls resource (client.calls(sid).update()), and post-call recording retrieval through the Recordings REST API. It supports conference bridges with verb including mute/hold controls.
Advanced features include StatusCallback URL configuration for call progress events, AMD (Answering Machine Detection) with machineDetection: 'DetectMessageEnd', and fallback URL routing. The agent handles Twilio signature validation using twilio.webhook() middleware for request authentication. Integrates with Twilio Studio for visual IVR flow management.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-programmable-voice-router-2/)
