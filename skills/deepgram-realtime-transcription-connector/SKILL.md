---
title: "Deepgram Real-Time Transcription Connector"
description: "This skill connects to Deepgram’s real-time transcription API using their WebSocket endpoint at wss://api.deepgram.com/v1/listen. It initializes a connection via the Deepgram Node SDK using createClient(apiKey) and establishes a live transcription session with client.listen.live({ model: “nova-2”, language: “en”, smart_format: true, diarize: true }). Audio is streamed in chunks using connection.send(audioBuffer) with support for raw PCM (linear16), WAV, MP3, and Opus formats. The skill handles three event types: “Results” for transcription data (both interim and final), “Metadata” for stream information, and “Error” for connection issues. Speaker diarization assigns speaker labels (Speaker 0, Speaker 1, etc.) to each word with confidence scores. The skill implements utterance end detection via the utterance_end_ms parameter and “UtteranceEnd” events for natural sentence boundary detection. Reconnection logic handles network interruptions with exponential backoff. Output formats include plain text, SRT subtitles with timestamps, and structured JSON with word-level timing. The skill also supports Deepgram’s keyword boosting via keywords=[“custom_term:2.0”] for domain-specific vocabulary."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/deepgram-realtime-transcription-connector/"
framework:
  - "MCP"
---

# Deepgram Real-Time Transcription Connector

This skill connects to Deepgram’s real-time transcription API using their WebSocket endpoint at wss://api.deepgram.com/v1/listen. It initializes a connection via the Deepgram Node SDK using createClient(apiKey) and establishes a live transcription session with client.listen.live({ model: “nova-2”, language: “en”, smart_format: true, diarize: true }). Audio is streamed in chunks using connection.send(audioBuffer) with support for raw PCM (linear16), WAV, MP3, and Opus formats. The skill handles three event types: “Results” for transcription data (both interim and final), “Metadata” for stream information, and “Error” for connection issues. Speaker diarization assigns speaker labels (Speaker 0, Speaker 1, etc.) to each word with confidence scores. The skill implements utterance end detection via the utterance_end_ms parameter and “UtteranceEnd” events for natural sentence boundary detection. Reconnection logic handles network interruptions with exponential backoff. Output formats include plain text, SRT subtitles with timestamps, and structured JSON with word-level timing. The skill also supports Deepgram’s keyword boosting via keywords=[“custom_term:2.0”] for domain-specific vocabulary.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/deepgram-realtime-transcription-connector
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/deepgram-realtime-transcription-connector` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-realtime-transcription-connector/)
