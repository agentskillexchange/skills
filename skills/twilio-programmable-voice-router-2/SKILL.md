---
title: "Twilio Programmable Voice Router"
description: "Builds intelligent voice routing flows using the Twilio Programmable Voice API. Generates TwiML responses with , , and  verbs, and manages call recordings via the Recordings REST resource."
verification: "security_reviewed"
source: "https://github.com/twilio/twilio-node"
category:
  - "Integrations & Connectors"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "twilio/twilio-node"
  github_stars: 1528
  ase_npm_package: "twilio"
  npm_weekly_downloads: 3731324
  license: "MIT"
---

# Twilio Programmable Voice Router

The Twilio Programmable Voice Router creates sophisticated call handling workflows using Twilio’s Programmable Voice API. It generates dynamic TwiML documents that chain  for DTMF/speech input,  for call forwarding with SIP and Client endpoints, and  for queue-based routing.


The skill manages the full call lifecycle: incoming call webhook handling, real-time call modification via the Calls resource (client.calls(sid).update()), and post-call recording retrieval through the Recordings REST API. It supports conference bridges with  verb including mute/hold controls.


Advanced features include StatusCallback URL configuration for call progress events, AMD (Answering Machine Detection) with machineDetection: 'DetectMessageEnd', and fallback URL routing. The agent handles Twilio signature validation using twilio.webhook() middleware for request authentication. Integrates with Twilio Studio for visual IVR flow management.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twilio-programmable-voice-router-2/)
