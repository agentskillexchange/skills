---
title: "Deepgram Real-Time Transcription Connector"
description: "Streams live audio to Deepgram’s WebSocket API at wss://api.deepgram.com/v1/listen for real-time speech-to-text. Handles interim results, utterance detection, and speaker diarization via the Deepgram Node SDK."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/deepgram-realtime-transcription-connector/"
category:
  - "Media &amp; Transcription"
framework:
  - "MCP"
---

# Deepgram Real-Time Transcription Connector

This skill connects to Deepgram’s real-time transcription API using their WebSocket endpoint at wss://api.deepgram.com/v1/listen. It initializes a connection via the Deepgram Node SDK using createClient(apiKey) and establishes a live transcription session with client.listen.live({ model: “nova-2”, language: “en”, smart_format: true, diarize: true }). Audio is streamed in chunks using connection.send(audioBuffer) with support for raw PCM (linear16), WAV, MP3, and Opus formats. The skill handles three event types: “Results” for transcription data (both interim and final), “Metadata” for stream information, and “Error” for connection issues. Speaker diarization assigns speaker labels (Speaker 0, Speaker 1, etc.) to each word with confidence scores. The skill implements utterance end detection via the utterance_end_ms parameter and “UtteranceEnd” events for natural sentence boundary detection. Reconnection logic handles network interruptions with exponential backoff. Output formats include plain text, SRT subtitles with timestamps, and structured JSON with word-level timing. The skill also supports Deepgram’s keyword boosting via keywords=[“custom_term:2.0”] for domain-specific vocabulary.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-realtime-transcription-connector/)
