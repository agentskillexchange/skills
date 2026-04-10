---
title: "Deepgram Nova Transcriber"
description: "Transcribes audio using the Deepgram Nova-2 API with diarization, punctuation, and smart formatting. Supports streaming via WebSocket and batch via REST with pre-recorded endpoint and callback URLs."
slug: "deepgram-nova-transcriber-agent"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/"
listed: true
---

# Deepgram Nova Transcriber

Transcribes audio using the Deepgram Nova-2 API with diarization, punctuation, and smart formatting. Supports streaming via WebSocket and batch via REST with pre-recorded endpoint and callback URLs.

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
clawhub install deepgram-nova-transcriber-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Deepgram Nova Transcriber integrates with Deepgram’s Nova-2 speech recognition model for high-accuracy transcription. It uses the /v1/listen REST endpoint for batch processing and WebSocket connections at wss://api.deepgram.com/v1/listen for real-time streaming transcription.
The agent configures transcription parameters including diarize=true for speaker identification, punctuate=true for automatic punctuation, smart_format=true for intelligent formatting of dates, numbers, and currency. Supports language detection with detect_language=true across 30+ languages.
For batch processing, it submits audio via URL reference or direct upload with Content-Type: audio/*, using callback URLs for async completion notification. Handles audio formats including WAV, MP3, FLAC, OGG, and WebM. Outputs structured JSON with word-level timestamps, confidence scores, paragraphs, and utterances. Includes post-processing for SRT/VTT subtitle generation and topic detection via Deepgram’s topics=true feature.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/)
