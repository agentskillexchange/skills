---
title: "ElevenLabs Voice Cloning Agent"
description: "Clone and synthesize custom voices using the ElevenLabs API v2 with instant voice cloning. Manages voice library operations, text-to-speech generation with SSML markup, and audio stream output via the elevenlabs-python SDK."
slug: "elevenlabs-voice-cloning-agent"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/elevenlabs-voice-cloning-agent/"
listed: true
---

# ElevenLabs Voice Cloning Agent

Clone and synthesize custom voices using the ElevenLabs API v2 with instant voice cloning. Manages voice library operations, text-to-speech generation with SSML markup, and audio stream output via the elevenlabs-python SDK.

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
clawhub install elevenlabs-voice-cloning-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Build custom voice profiles and generate natural speech using the ElevenLabs API v2 endpoint. This skill handles the full voice cloning workflow from sample upload through synthesis output.
The agent manages voice library operations including creating instant voice clones from audio samples via POST /v1/voices/add, listing available voices, and editing voice settings (stability, similarity_boost, style, use_speaker_boost). Text-to-speech requests are sent to /v1/text-to-speech/{voice_id} with configurable model selection between eleven_monolingual_v1, eleven_multilingual_v2, and eleven_turbo_v2.
Advanced features include SSML markup support for controlling prosody, emphasis, and breaks in generated speech. The skill streams audio output in real-time using chunked transfer encoding for low-latency playback.
Integrates with the elevenlabs-python SDK for programmatic control, and supports output in mp3, pcm, ulaw, and opus formats. Rate limiting and quota tracking are built in to manage API usage across generation requests.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elevenlabs-voice-cloning-agent/)
