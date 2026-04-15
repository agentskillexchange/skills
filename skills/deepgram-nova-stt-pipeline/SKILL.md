---
title: "Deepgram Nova STT Pipeline"
description: "Real-time speech-to-text using Deepgram Nova-2 API with streaming WebSocket connections. Supports diarization, punctuation, and language detection via the Deepgram Python SDK for podcast and meeting transcription workflows."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/deepgram-nova-stt-pipeline/"
category:
  - "Media & Transcription"
framework:
  - "Claude Code"
---

# Deepgram Nova STT Pipeline

Automate speech-to-text transcription using the Deepgram Nova-2 model via their streaming WebSocket API. This skill connects to the Deepgram Python SDK (deepgram-sdk) to process audio files and live audio streams into accurate text transcripts.

Key capabilities include multi-speaker diarization for meeting recordings, automatic punctuation restoration, and real-time interim results for live captioning. The skill supports over 30 languages with automatic language detection.

Configuration options include model selection (nova-2, nova, enhanced, base), sample rate settings, encoding formats (linear16, flac, opus), and callback URLs for async processing. The pipeline handles chunked audio uploads for large files, with automatic retry logic and rate limit management against the Deepgram REST API.

Output formats include plain text, SRT subtitles, VTT captions, and structured JSON with word-level timestamps. Integrates with FFmpeg for audio preprocessing and format conversion before submission to the Deepgram endpoint.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/deepgram-nova-stt-pipeline
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/deepgram-nova-stt-pipeline` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-nova-stt-pipeline/)
