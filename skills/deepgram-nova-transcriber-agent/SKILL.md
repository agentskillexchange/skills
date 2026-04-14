---
title: "Deepgram Nova Transcriber"
description: "Transcribes audio using the Deepgram Nova-2 API with diarization, punctuation, and smart formatting. Supports streaming via WebSocket and batch via REST with pre-recorded endpoint and callback URLs."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
---

# Deepgram Nova Transcriber

Deepgram Nova Transcriber integrates with Deepgram’s Nova-2 speech recognition model for high-accuracy transcription. It uses the /v1/listen REST endpoint for batch processing and WebSocket connections at wss://api.deepgram.com/v1/listen for real-time streaming transcription.

The agent configures transcription parameters including diarize=true for speaker identification, punctuate=true for automatic punctuation, smart_format=true for intelligent formatting of dates, numbers, and currency. Supports language detection with detect_language=true across 30+ languages.

For batch processing, it submits audio via URL reference or direct upload with Content-Type: audio/*, using callback URLs for async completion notification. Handles audio formats including WAV, MP3, FLAC, OGG, and WebM. Outputs structured JSON with word-level timestamps, confidence scores, paragraphs, and utterances. Includes post-processing for SRT/VTT subtitle generation and topic detection via Deepgram’s topics=true feature.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/)
