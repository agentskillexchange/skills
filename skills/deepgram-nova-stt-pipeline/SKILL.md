---
name: "Deepgram Nova STT Pipeline"
description: "Real-time speech-to-text using Deepgram Nova-2 API with streaming WebSocket connections. Supports diarization, punctuation, and language detection via the Deepgram Python SDK for podcast and meeting transcription workflows."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/deepgram-nova-stt-pipeline/"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
---

# Deepgram Nova STT Pipeline

Automate speech-to-text transcription using the Deepgram Nova-2 model via their streaming WebSocket API. This skill connects to the Deepgram Python SDK (deepgram-sdk) to process audio files and live audio streams into accurate text transcripts.
Key capabilities include multi-speaker diarization for meeting recordings, automatic punctuation restoration, and real-time interim results for live captioning. The skill supports over 30 languages with automatic language detection.
Configuration options include model selection (nova-2, nova, enhanced, base), sample rate settings, encoding formats (linear16, flac, opus), and callback URLs for async processing. The pipeline handles chunked audio uploads for large files, with automatic retry logic and rate limit management against the Deepgram REST API.
Output formats include plain text, SRT subtitles, VTT captions, and structured JSON with word-level timestamps. Integrates with FFmpeg for audio preprocessing and format conversion before submission to the Deepgram endpoint.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-nova-stt-pipeline/)
