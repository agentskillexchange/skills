---
title: "Deepgram Real-Time Transcription Connector"
description: "Streams live audio to Deepgram's WebSocket API at wss://api.deepgram.com/v1/listen for real-time speech-to-text. Handles interim results, utterance detection, and speaker diarization via the Deepgram Node SDK."
verification: "security_reviewed"
source: "https://github.com/deepgram/deepgram-js-sdk"
author: "Deepgram"
category:
  - "Media & Transcription"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "deepgram/deepgram-js-sdk"
  github_stars: 260
  npm_package: "@deepgram/sdk"
  npm_weekly_downloads: 1571012
---

# Deepgram Real-Time Transcription Connector

Streams live audio to Deepgram's WebSocket API at wss://api.deepgram.com/v1/listen for real-time speech-to-text. Handles interim results, utterance detection, and speaker diarization via the Deepgram Node SDK.

## Prerequisites

Node.js

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
npm install @deepgram/sdk
```

## Documentation

- https://developers.deepgram.com/docs/node-sdk

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-realtime-transcription-connector/)
