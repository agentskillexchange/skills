---
title: "Deepgram Nova Transcriber"
description: "Deepgram Nova Transcriber integrates with Deepgram’s Nova-2 speech recognition model for high-accuracy transcription. It uses the /v1/listen REST endpoint for batch processing and WebSocket connections at wss://api.deepgram.com/v1/listen for real-time streaming transcription.\nThe agent configures transcription parameters including diarize=true for speaker identification, punctuate=true for automatic punctuation, smart_format=true for intelligent formatting of dates, numbers, and currency. Supports language detection with detect_language=true across 30+ languages.\nFor batch processing, it submits audio via URL reference or direct upload with Content-Type: audio/*, using callback URLs for async completion notification. Handles audio formats including WAV, MP3, FLAC, OGG, and WebM. Outputs structured JSON with word-level timestamps, confidence scores, paragraphs, and utterances. Includes post-processing for SRT/VTT subtitle generation and topic detection via Deepgram’s topics=true feature."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/"
framework:
  - "OpenClaw"
---

# Deepgram Nova Transcriber

Deepgram Nova Transcriber integrates with Deepgram’s Nova-2 speech recognition model for high-accuracy transcription. It uses the /v1/listen REST endpoint for batch processing and WebSocket connections at wss://api.deepgram.com/v1/listen for real-time streaming transcription.
The agent configures transcription parameters including diarize=true for speaker identification, punctuate=true for automatic punctuation, smart_format=true for intelligent formatting of dates, numbers, and currency. Supports language detection with detect_language=true across 30+ languages.
For batch processing, it submits audio via URL reference or direct upload with Content-Type: audio/*, using callback URLs for async completion notification. Handles audio formats including WAV, MP3, FLAC, OGG, and WebM. Outputs structured JSON with word-level timestamps, confidence scores, paragraphs, and utterances. Includes post-processing for SRT/VTT subtitle generation and topic detection via Deepgram’s topics=true feature.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/deepgram-nova-transcriber-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/deepgram-nova-transcriber-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/)
