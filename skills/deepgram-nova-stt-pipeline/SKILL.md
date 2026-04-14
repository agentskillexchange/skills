---
title: "Deepgram Nova STT Pipeline"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-nova-stt-pipeline/)
