---
title: Deepgram Nova Transcriber
description: 'Deepgram Nova Transcriber integrates with Deepgram’s Nova-2 speech recognition
  model for high-accuracy transcription. It uses the /v1/listen REST endpoint for
  batch processing and WebSocket connections at wss://api.deepgram.com/v1/listen for
  real-time streaming transcription. The agent configures transcription parameters
  including diarize=true for speaker identification, punctuate=true for automatic
  punctuation, smart_format=true for intelligent formatting of dates, numbers, and
  currency. Supports language detection with detect_language=true across 30+ languages.
  For batch processing, it submits audio via URL reference or direct upload with Content-Type:
  audio/* , using callback URLs for async completion notification. Handles audio formats
  including WAV, MP3, FLAC, OGG, and WebM. Outputs structured JSON with word-level
  timestamps, confidence scores, paragraphs, and utterances. Includes post-processing
  for SRT/VTT subtitle generation and topic detection via Deepgram’s topics=true feature.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/
category:
- Media &amp; Transcription
framework:
- OpenClaw
---

# Deepgram Nova Transcriber

Deepgram Nova Transcriber integrates with Deepgram’s Nova-2 speech recognition model for high-accuracy transcription. It uses the /v1/listen REST endpoint for batch processing and WebSocket connections at wss://api.deepgram.com/v1/listen for real-time streaming transcription. The agent configures transcription parameters including diarize=true for speaker identification, punctuate=true for automatic punctuation, smart_format=true for intelligent formatting of dates, numbers, and currency. Supports language detection with detect_language=true across 30+ languages. For batch processing, it submits audio via URL reference or direct upload with Content-Type: audio/* , using callback URLs for async completion notification. Handles audio formats including WAV, MP3, FLAC, OGG, and WebM. Outputs structured JSON with word-level timestamps, confidence scores, paragraphs, and utterances. Includes post-processing for SRT/VTT subtitle generation and topic detection via Deepgram’s topics=true feature.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/)
