---
title: "ElevenLabs Voice Cloning Agent"
description: "Clone and synthesize custom voices using the ElevenLabs API v2 with instant voice cloning. Manages voice library operations, text-to-speech generation with SSML markup, and audio stream output via the elevenlabs-python SDK."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/elevenlabs-voice-cloning-agent/"
category:
  - "Media & Transcription"
framework:
  - "OpenClaw"
---

# ElevenLabs Voice Cloning Agent

Build custom voice profiles and generate natural speech using the ElevenLabs API v2 endpoint. This skill handles the full voice cloning workflow from sample upload through synthesis output.

The agent manages voice library operations including creating instant voice clones from audio samples via POST /v1/voices/add, listing available voices, and editing voice settings (stability, similarity_boost, style, use_speaker_boost). Text-to-speech requests are sent to /v1/text-to-speech/{voice_id} with configurable model selection between eleven_monolingual_v1, eleven_multilingual_v2, and eleven_turbo_v2.

Advanced features include SSML markup support for controlling prosody, emphasis, and breaks in generated speech. The skill streams audio output in real-time using chunked transfer encoding for low-latency playback.

Integrates with the elevenlabs-python SDK for programmatic control, and supports output in mp3, pcm, ulaw, and opus formats. Rate limiting and quota tracking are built in to manage API usage across generation requests.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/elevenlabs-voice-cloning-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/elevenlabs-voice-cloning-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elevenlabs-voice-cloning-agent/)
