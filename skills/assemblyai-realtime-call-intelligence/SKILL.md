---
title: "AssemblyAI Real-Time Call Intelligence"
description: "Streams audio from Twilio Media Streams over WebSocket to AssemblyAI real-time transcription, extracting speaker-diarized transcripts with word-level timestamps. Triggers entity detection and sentiment analysis via AssemblyAI LeMUR on completed call segments. Results are pushed to HubSpot or Salesforce contact records via their REST APIs."
slug: "assemblyai-realtime-call-intelligence"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/assemblyai-realtime-call-intelligence/"
listed: true
---

# AssemblyAI Real-Time Call Intelligence

Streams audio from Twilio Media Streams over WebSocket to AssemblyAI real-time transcription, extracting speaker-diarized transcripts with word-level timestamps. Triggers entity detection and sentiment analysis via AssemblyAI LeMUR on completed call segments. Results are pushed to HubSpot or Salesforce contact records via their REST APIs.

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
clawhub install assemblyai-realtime-call-intelligence
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

AssemblyAI Real-Time Call Intelligence is built around Twilio communications APIs. The underlying ecosystem is represented by twilio/twilio-node (1,523+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SMS, voice, Media Streams, webhooks, recordings, messaging services and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to twilio so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Streams audio from Twilio Media Streams over WebSocket to AssemblyAI real-time transcription, extracting speaker-diarized transcripts with word-level timestamps. Triggers entity detection and sentiment analysis via AssemblyAI LeMUR on completed call segments. Results are pushed to HubSpot or Salesforce contact records via their REST APIs. The implementation typically relies on SMS, voice, Media Streams, webhooks, recordings, messaging services, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses SMS, voice, Media Streams, webhooks, recordings, messaging services instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as notifications, call intelligence, and communication workflows.
Key integration points include notifications, call intelligence, and communication workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemblyai-realtime-call-intelligence/)
