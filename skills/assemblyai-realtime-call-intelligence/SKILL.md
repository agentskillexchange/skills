---
name: "AssemblyAI Real-Time Call Intelligence"
description: "Streams audio from Twilio Media Streams over WebSocket to AssemblyAI real-time transcription, extracting speaker-diarized transcripts with word-level timestamps. Triggers entity detection and sentiment analysis via AssemblyAI LeMUR on completed call segments. Results are pushed to HubSpot or Salesforce contact records via their REST APIs."
category: "Integrations & Connectors"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
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

Streams audio from Twilio Media Streams over WebSocket to AssemblyAI real-time transcription, extracting speaker-diarized transcripts with word-level timestamps. Triggers entity detection and sentiment analysis via AssemblyAI LeMUR on completed call segments. Results are pushed to HubSpot or Salesforce contact records via their REST APIs.

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
