---
name: "Deepgram Real-Time Transcription Connector"
slug: "deepgram-realtime-transcription-connector"
description: "Streams live audio to Deepgram's WebSocket API at wss://api.deepgram.com/v1/listen for real-time speech-to-text. Handles interim results, utterance detection, and speaker diarization via the Deepgram Node SDK."
github_stars: 260
verification: "listed"
source: "https://github.com/deepgram/deepgram-js-sdk"
author: "Deepgram"
category: "Media & Transcription"
framework: "MCP"
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

Use the upstream install or setup path that matches your environment:
- npm install @deepgram/sdk
- pnpm install
- make build
- make test

Requirements and caveats from upstream:
- [![Node.js 18+](https://img.shields.io/badge/node-18+-blue.svg)](https://nodejs.org/)
- Your proxy must set the Authorization: token DEEPGRAM_API_KEY header and forward requests to Deepgram's API. See our example [Deepgram Node Proxy](https://github.com/deepgram-devs/deepgram-node-proxy).
- Node.js 18+

Basic usage or getting-started notes:
- bash
- ## Reference
- **[API Reference](./reference.md)** - Complete reference for all SDK methods and parameters

- Source: https://github.com/deepgram/deepgram-js-sdk
- Extracted from upstream docs: https://raw.githubusercontent.com/deepgram/deepgram-js-sdk/HEAD/README.md

## Documentation

- https://developers.deepgram.com/docs/node-sdk

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-realtime-transcription-connector/)
