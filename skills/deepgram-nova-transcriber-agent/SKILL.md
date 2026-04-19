---
title: "Deepgram Nova Transcriber"
description: "Deepgram Nova Transcriber integrates with Deepgram&#8217;s Nova-2 speech recognition model for high-accuracy transcription. It uses the /v1/listen REST endpoint for batch processing and WebSocket connections at wss://api.deepgram.com/v1/listen for real-time streaming transcription. The agent configures transcription parameters including diarize=true for speaker identification, punctuate=true for automatic punctuation, smart_format=true for intelligent formatting of dates, numbers, and currency. Supports language detection with detect_language=true across 30+ languages. For batch processing, it submits audio via URL reference or direct upload with Content-Type: audio/* , using callback URLs for async completion notification. Handles audio formats including WAV, MP3, FLAC, OGG, and WebM. Outputs structured JSON with word-level timestamps, confidence scores, paragraphs, and utterances. Includes post-processing for SRT/VTT subtitle generation and topic detection via Deepgram&#8217;s topics=true feature."
source: "https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
---

# Deepgram Nova Transcriber

Deepgram Nova Transcriber integrates with Deepgram&#8217;s Nova-2 speech recognition model for high-accuracy transcription. It uses the /v1/listen REST endpoint for batch processing and WebSocket connections at wss://api.deepgram.com/v1/listen for real-time streaming transcription. The agent configures transcription parameters including diarize=true for speaker identification, punctuate=true for automatic punctuation, smart_format=true for intelligent formatting of dates, numbers, and currency. Supports language detection with detect_language=true across 30+ languages. For batch processing, it submits audio via URL reference or direct upload with Content-Type: audio/* , using callback URLs for async completion notification. Handles audio formats including WAV, MP3, FLAC, OGG, and WebM. Outputs structured JSON with word-level timestamps, confidence scores, paragraphs, and utterances. Includes post-processing for SRT/VTT subtitle generation and topic detection via Deepgram&#8217;s topics=true feature.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/)
