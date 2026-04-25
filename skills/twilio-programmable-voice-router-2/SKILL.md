---
title: "Twilio Programmable Voice Router"
description: "Builds intelligent voice routing flows using the Twilio Programmable Voice API. Generates TwiML responses with , , and verbs, and manages call recordings via the Recordings REST resource."
verification: "security_reviewed"
source: "https://github.com/twilio/twilio-node"
category:
  - "Integrations & Connectors"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "twilio/twilio-node"
  github_stars: 1528
  npm_package: "twilio"
  npm_weekly_downloads: 3731324
---

# Twilio Programmable Voice Router

The Twilio Programmable Voice Router creates sophisticated call handling workflows using Twilio’s Programmable Voice API. It generates dynamic TwiML documents that chain for DTMF/speech input, for call forwarding with SIP and Client endpoints, and for queue-based routing. The skill manages the full call lifecycle: incoming call webhook handling, real-time call modification via the Calls resource (client.calls(sid).update()), and post-call recording retrieval through the Recordings REST API. It supports conference bridges with verb including mute/hold controls. Advanced features include StatusCallback URL configuration for call progress events, AMD (Answering Machine Detection) with machineDetection: 'DetectMessageEnd', and fallback URL routing. The agent handles Twilio signature validation using twilio.webhook() middleware for request authentication. Integrates with Twilio Studio for visual IVR flow management.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/twilio-programmable-voice-router-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/twilio-programmable-voice-router-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/twilio-programmable-voice-router-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-programmable-voice-router-2/)
