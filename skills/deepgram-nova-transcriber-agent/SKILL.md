---
name: "Deepgram Nova Transcriber"
description: "Transcribes audio using the Deepgram Nova-2 API with diarization, punctuation, and smart formatting. Supports streaming via WebSocket and batch via REST with pre-recorded endpoint and callback URLs."
category: "Media & Transcription"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/"
---

# Deepgram Nova Transcriber

Transcribes audio using the Deepgram Nova-2 API with diarization, punctuation, and smart formatting. Supports streaming via WebSocket and batch via REST with pre-recorded endpoint and callback URLs.

## Overview

Deepgram Nova Transcriber integrates with Deepgram’s Nova-2 speech recognition model for high-accuracy transcription. It uses the `/v1/listen` REST endpoint for batch processing and WebSocket connections at `wss://api.deepgram.com/v1/listen` for real-time streaming transcription.

The agent configures transcription parameters including `diarize=true` for speaker identification, `punctuate=true` for automatic punctuation, `smart_format=true` for intelligent formatting of dates, numbers, and currency. Supports language detection with `detect_language=true` across 30+ languages.

For batch processing, it submits audio via URL reference or direct upload with `Content-Type: audio/*`, using callback URLs for async completion notification. Handles audio formats including WAV, MP3, FLAC, OGG, and WebM. Outputs structured JSON with word-level timestamps, confidence scores, paragraphs, and utterances. Includes post-processing for SRT/VTT subtitle generation and topic detection via Deepgram’s `topics=true` feature.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill deepgram-nova-transcriber-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill deepgram-nova-transcriber-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill deepgram-nova-transcriber-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill deepgram-nova-transcriber-agent -a codex
```

### OpenClaw

```bash
clawhub install deepgram-nova-transcriber-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/
