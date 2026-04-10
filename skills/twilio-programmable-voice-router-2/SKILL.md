---
name: Twilio Programmable Voice Router
description: Builds intelligent voice routing flows using the Twilio Programmable
  Voice API. Generates TwiML responses with , , and verbs, and manages call recordings
  via the Recordings REST resource.
verification: security_reviewed
source: https://agentskillexchange.com/skills/twilio-programmable-voice-router-2/
category:
- Integrations &amp; Connectors
framework:
- Claude Agents
---
# Twilio Programmable Voice Router

The Twilio Programmable Voice Router creates sophisticated call handling workflows using Twilio's Programmable Voice API. It generates dynamic TwiML documents that chain  for DTMF/speech input,  for call forwarding with SIP and Client endpoints, and  for queue-based routing.
The skill manages the full call lifecycle: incoming call webhook handling, real-time call modification via the Calls resource (client.calls(sid).update()), and post-call recording retrieval through the Recordings REST API. It supports conference bridges with  verb including mute/hold controls.
Advanced features include StatusCallback URL configuration for call progress events, AMD (Answering Machine Detection) with machineDetection: 'DetectMessageEnd', and fallback URL routing. The agent handles Twilio signature validation using twilio.webhook() middleware for request authentication. Integrates with Twilio Studio for visual IVR flow management.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-programmable-voice-router-2/)
