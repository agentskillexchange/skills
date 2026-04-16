---
title: "AssemblyAI Real-Time Call Intelligence"
description: "Streams audio from Twilio Media Streams over WebSocket to AssemblyAI real-time transcription, extracting speaker-diarized transcripts with word-level timestamps. Triggers entity detection and sentiment analysis via AssemblyAI LeMUR on completed call segments. Results are pushed to HubSpot or Salesforce contact records via their REST APIs."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/assemblyai-realtime-call-intelligence/"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Custom Agents"
---

# AssemblyAI Real-Time Call Intelligence

AssemblyAI Real-Time Call Intelligence is built around Twilio communications APIs. The underlying ecosystem is represented by twilio/twilio-node (1,523+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SMS, voice, Media Streams, webhooks, recordings, messaging services and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to twilio so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Streams audio from Twilio Media Streams over WebSocket to AssemblyAI real-time transcription, extracting speaker-diarized transcripts with word-level timestamps. Triggers entity detection and sentiment analysis via AssemblyAI LeMUR on completed call segments. Results are pushed to HubSpot or Salesforce contact records via their REST APIs. The implementation typically relies on SMS, voice, Media Streams, webhooks, recordings, messaging services, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses SMS, voice, Media Streams, webhooks, recordings, messaging services instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as notifications, call intelligence, and communication workflows.

Key integration points include notifications, call intelligence, and communication workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemblyai-realtime-call-intelligence/)
