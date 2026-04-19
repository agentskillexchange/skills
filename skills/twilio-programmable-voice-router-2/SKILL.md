---
title: "Twilio Programmable Voice Router"
description: "The Twilio Programmable Voice Router creates sophisticated call handling workflows using Twilio&#8217;s Programmable Voice API. It generates dynamic TwiML documents that chain for DTMF/speech input, for call forwarding with SIP and Client endpoints, and for queue-based routing. The skill manages the full call lifecycle: incoming call webhook handling, real-time call modification via the Calls resource ( client.calls(sid).update() ), and post-call recording retrieval through the Recordings REST API. It supports conference bridges with verb including mute/hold controls. Advanced features include StatusCallback URL configuration for call progress events, AMD (Answering Machine Detection) with machineDetection: 'DetectMessageEnd' , and fallback URL routing. The agent handles Twilio signature validation using twilio.webhook() middleware for request authentication. Integrates with Twilio Studio for visual IVR flow management."
source: "https://github.com/twilio/twilio-node"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "twilio/twilio-node"
  github_stars: 1528
  npm_package: "twilio"
  npm_weekly_downloads: 3731324
---

# Twilio Programmable Voice Router

The Twilio Programmable Voice Router creates sophisticated call handling workflows using Twilio&#8217;s Programmable Voice API. It generates dynamic TwiML documents that chain for DTMF/speech input, for call forwarding with SIP and Client endpoints, and for queue-based routing. The skill manages the full call lifecycle: incoming call webhook handling, real-time call modification via the Calls resource ( client.calls(sid).update() ), and post-call recording retrieval through the Recordings REST API. It supports conference bridges with verb including mute/hold controls. Advanced features include StatusCallback URL configuration for call progress events, AMD (Answering Machine Detection) with machineDetection: 'DetectMessageEnd' , and fallback URL routing. The agent handles Twilio signature validation using twilio.webhook() middleware for request authentication. Integrates with Twilio Studio for visual IVR flow management.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-programmable-voice-router-2/)
