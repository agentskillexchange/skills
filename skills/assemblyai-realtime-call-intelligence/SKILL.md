---
name: "AssemblyAI Real-Time Call Intelligence"
description: "Streams audio from Twilio Media Streams over WebSocket to AssemblyAI real-time transcription, extracting speaker-diarized transcripts with word-level timestamps. Triggers entity detection and sentiment analysis via AssemblyAI LeMUR on completed call segments. Results are pushed to HubSpot or Salesforce contact records via their REST APIs."
category: "Integrations & Connectors"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/assemblyai-realtime-call-intelligence/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "twilio"  # from ase_tool_match
  github_stars: 1523  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3810383  # from ase_npm_downloads
  github_repo: "twilio/twilio-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# AssemblyAI Real-Time Call Intelligence

Streams audio from Twilio Media Streams over WebSocket to AssemblyAI real-time transcription, extracting speaker-diarized transcripts with word-level timestamps. Triggers entity detection and sentiment analysis via AssemblyAI LeMUR on completed call segments. Results are pushed to HubSpot or Salesforce contact records via their REST APIs.

## Overview

**AssemblyAI Real-Time Call Intelligence** is built around Twilio communications APIs. The underlying ecosystem is represented by `twilio/twilio-node` (1,523+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SMS, voice, Media Streams, webhooks, recordings, messaging services and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to twilio so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Streams audio from Twilio Media Streams over WebSocket to AssemblyAI real-time transcription, extracting speaker-diarized transcripts with word-level timestamps. Triggers entity detection and sentiment analysis via AssemblyAI LeMUR on completed call segments. Results are pushed to HubSpot or Salesforce contact records via their REST APIs. The implementation typically relies on SMS, voice, Media Streams, webhooks, recordings, messaging services, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses SMS, voice, Media Streams, webhooks, recordings, messaging services instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as notifications, call intelligence, and communication workflows.

Key integration points include notifications, call intelligence, and communication workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill assemblyai-realtime-call-intelligence
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill assemblyai-realtime-call-intelligence -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill assemblyai-realtime-call-intelligence -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill assemblyai-realtime-call-intelligence -a codex
```

### OpenClaw

```bash
clawhub install assemblyai-realtime-call-intelligence
```

## Source

- Marketplace: https://agentskillexchange.com/skills/assemblyai-realtime-call-intelligence/
