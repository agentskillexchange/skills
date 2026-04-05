---
name: "Deepgram Real-Time Transcription Connector"
description: "Streams live audio to Deepgram’s WebSocket API at wss://api.deepgram.com/v1/listen for real-time speech-to-text. Handles interim results, utterance detection, and speaker diarization via the Deepgram Node SDK."
category: "Media &amp; Transcription"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/deepgram-realtime-transcription-connector/"
---
# Deepgram Real-Time Transcription Connector

Streams live audio to Deepgram’s WebSocket API at wss://api.deepgram.com/v1/listen for real-time speech-to-text. Handles interim results, utterance detection, and speaker diarization via the Deepgram Node SDK.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill deepgram-realtime-transcription-connector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill deepgram-realtime-transcription-connector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill deepgram-realtime-transcription-connector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill deepgram-realtime-transcription-connector -a codex
```

### OpenClaw

```bash
clawhub install deepgram-realtime-transcription-connector
```

## Details

This skill connects to Deepgram’s real-time transcription API using their WebSocket endpoint at wss://api.deepgram.com/v1/listen. It initializes a connection via the Deepgram Node SDK using createClient(apiKey) and establishes a live transcription session with client.listen.live({ model: “nova-2”, language: “en”, smart_format: true, diarize: true }). Audio is streamed in chunks using connection.send(audioBuffer) with support for raw PCM (linear16), WAV, MP3, and Opus formats. The skill handles three event types: “Results” for transcription data (both interim and final), “Metadata” for stream information, and “Error” for connection issues. Speaker diarization assigns speaker labels (Speaker 0, Speaker 1, etc.) to each word with confidence scores. The skill implements utterance end detection via the utterance_end_ms parameter and “UtteranceEnd” events for natural sentence boundary detection. Reconnection logic handles network interruptions with exponential backoff. Output formats include plain text, SRT subtitles with timestamps, and structured JSON with word-level timing. The skill also supports Deepgram’s keyword boosting via keywords=[“custom_term:2.0”] for domain-specific vocabulary.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-realtime-transcription-connector/)
