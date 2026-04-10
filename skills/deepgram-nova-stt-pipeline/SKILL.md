---
title: "Deepgram Nova STT Pipeline"
description: "Real-time speech-to-text using Deepgram Nova-2 API with streaming WebSocket connections. Supports diarization, punctuation, and language detection via the Deepgram Python SDK for podcast and meeting transcription workflows."
slug: "deepgram-nova-stt-pipeline"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/deepgram-nova-stt-pipeline/"
listed: true
---

# Deepgram Nova STT Pipeline

Real-time speech-to-text using Deepgram Nova-2 API with streaming WebSocket connections. Supports diarization, punctuation, and language detection via the Deepgram Python SDK for podcast and meeting transcription workflows.

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
clawhub install deepgram-nova-stt-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Automate speech-to-text transcription using the Deepgram Nova-2 model via their streaming WebSocket API. This skill connects to the Deepgram Python SDK (deepgram-sdk) to process audio files and live audio streams into accurate text transcripts.
Key capabilities include multi-speaker diarization for meeting recordings, automatic punctuation restoration, and real-time interim results for live captioning. The skill supports over 30 languages with automatic language detection.
Configuration options include model selection (nova-2, nova, enhanced, base), sample rate settings, encoding formats (linear16, flac, opus), and callback URLs for async processing. The pipeline handles chunked audio uploads for large files, with automatic retry logic and rate limit management against the Deepgram REST API.
Output formats include plain text, SRT subtitles, VTT captions, and structured JSON with word-level timestamps. Integrates with FFmpeg for audio preprocessing and format conversion before submission to the Deepgram endpoint.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-nova-stt-pipeline/)
