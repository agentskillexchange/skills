---
name: Deepgram Real-Time Transcription Connector
description: Streams live audio to Deepgram&#8217;s WebSocket API at wss://api.deepgram.com/v1/listen
  for real-time speech-to-text. Handles interim results, utterance detection, and
  speaker diarization via the Deepgram Node SDK.
verification: security_reviewed
source: https://agentskillexchange.com/skills/deepgram-realtime-transcription-connector/
category:
- Media &amp; Transcription
framework:
- MCP
---
# Deepgram Real-Time Transcription Connector

This skill connects to Deepgram's real-time transcription API using their WebSocket endpoint at wss://api.deepgram.com/v1/listen. It initializes a connection via the Deepgram Node SDK using createClient(apiKey) and establishes a live transcription session with client.listen.live({ model: &#8220;nova-2&#8221;, language: &#8220;en&#8221;, smart_format: true, diarize: true }). Audio is streamed in chunks using connection.send(audioBuffer) with support for raw PCM (linear16), WAV, MP3, and Opus formats. The skill handles three event types: &#8220;Results&#8221; for transcription data (both interim and final), &#8220;Metadata&#8221; for stream information, and &#8220;Error&#8221; for connection issues. Speaker diarization assigns speaker labels (Speaker 0, Speaker 1, etc.) to each word with confidence scores. The skill implements utterance end detection via the utterance_end_ms parameter and &#8220;UtteranceEnd&#8221; events for natural sentence boundary detection. Reconnection logic handles network interruptions with exponential backoff. Output formats include plain text, SRT subtitles with timestamps, and structured JSON with word-level timing. The skill also supports Deepgram's keyword boosting via keywords=[&#8220;custom_term:2.0&#8221;] for domain-specific vocabulary.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-realtime-transcription-connector/)
