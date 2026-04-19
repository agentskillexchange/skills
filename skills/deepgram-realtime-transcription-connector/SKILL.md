---
title: "Deepgram Real-Time Transcription Connector"
description: "This skill connects to Deepgram&#8217;s real-time transcription API using their WebSocket endpoint at wss://api.deepgram.com/v1/listen. It initializes a connection via the Deepgram Node SDK using createClient(apiKey) and establishes a live transcription session with client.listen.live({ model: &#8220;nova-2&#8221;, language: &#8220;en&#8221;, smart_format: true, diarize: true }). Audio is streamed in chunks using connection.send(audioBuffer) with support for raw PCM (linear16), WAV, MP3, and Opus formats. The skill handles three event types: &#8220;Results&#8221; for transcription data (both interim and final), &#8220;Metadata&#8221; for stream information, and &#8220;Error&#8221; for connection issues. Speaker diarization assigns speaker labels (Speaker 0, Speaker 1, etc.) to each word with confidence scores. The skill implements utterance end detection via the utterance_end_ms parameter and &#8220;UtteranceEnd&#8221; events for natural sentence boundary detection. Reconnection logic handles network interruptions with exponential backoff. Output formats include plain text, SRT subtitles with timestamps, and structured JSON with word-level timing. The skill also supports Deepgram&#8217;s keyword boosting via keywords=[&#8220;custom_term:2.0&#8221;] for domain-specific vocabulary."
source: "https://agentskillexchange.com/skills/deepgram-realtime-transcription-connector/"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "MCP"
---

# Deepgram Real-Time Transcription Connector

This skill connects to Deepgram&#8217;s real-time transcription API using their WebSocket endpoint at wss://api.deepgram.com/v1/listen. It initializes a connection via the Deepgram Node SDK using createClient(apiKey) and establishes a live transcription session with client.listen.live({ model: &#8220;nova-2&#8221;, language: &#8220;en&#8221;, smart_format: true, diarize: true }). Audio is streamed in chunks using connection.send(audioBuffer) with support for raw PCM (linear16), WAV, MP3, and Opus formats. The skill handles three event types: &#8220;Results&#8221; for transcription data (both interim and final), &#8220;Metadata&#8221; for stream information, and &#8220;Error&#8221; for connection issues. Speaker diarization assigns speaker labels (Speaker 0, Speaker 1, etc.) to each word with confidence scores. The skill implements utterance end detection via the utterance_end_ms parameter and &#8220;UtteranceEnd&#8221; events for natural sentence boundary detection. Reconnection logic handles network interruptions with exponential backoff. Output formats include plain text, SRT subtitles with timestamps, and structured JSON with word-level timing. The skill also supports Deepgram&#8217;s keyword boosting via keywords=[&#8220;custom_term:2.0&#8221;] for domain-specific vocabulary.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-realtime-transcription-connector/)
