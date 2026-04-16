---
title: "Deepgram Nova Transcriber"
description: "Transcribes audio using the Deepgram Nova-2 API with diarization, punctuation, and smart formatting. Supports streaming via WebSocket and batch via REST with pre-recorded endpoint and callback URLs."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/"
category:
  - "Media & Transcription"
framework:
  - "OpenClaw"
---

# Deepgram Nova Transcriber

Deepgram Nova Transcriber integrates with Deepgram’s Nova-2 speech recognition model for high-accuracy transcription. It uses the /v1/listen REST endpoint for batch processing and WebSocket connections at wss://api.deepgram.com/v1/listen for real-time streaming transcription.


The agent configures transcription parameters including diarize=true for speaker identification, punctuate=true for automatic punctuation, smart_format=true for intelligent formatting of dates, numbers, and currency. Supports language detection with detect_language=true across 30+ languages.


For batch processing, it submits audio via URL reference or direct upload with Content-Type: audio/*, using callback URLs for async completion notification. Handles audio formats including WAV, MP3, FLAC, OGG, and WebM. Outputs structured JSON with word-level timestamps, confidence scores, paragraphs, and utterances. Includes post-processing for SRT/VTT subtitle generation and topic detection via Deepgram’s topics=true feature.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-nova-transcriber-agent/)
