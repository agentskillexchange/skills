---
name: ElevenLabs Voice Cloning Agent
description: Clone and synthesize custom voices using the ElevenLabs API v2 with instant
  voice cloning. Manages voice library operations, text-to-speech generation with
  SSML markup, and audio stream output via the elevenlabs-python SDK.
verification: security_reviewed
source: https://agentskillexchange.com/skills/elevenlabs-voice-cloning-agent/
category:
- Media &amp; Transcription
framework:
- OpenClaw
---
# ElevenLabs Voice Cloning Agent

Build custom voice profiles and generate natural speech using the ElevenLabs API v2 endpoint. This skill handles the full voice cloning workflow from sample upload through synthesis output.
The agent manages voice library operations including creating instant voice clones from audio samples via POST /v1/voices/add, listing available voices, and editing voice settings (stability, similarity_boost, style, use_speaker_boost). Text-to-speech requests are sent to /v1/text-to-speech/{voice_id} with configurable model selection between eleven_monolingual_v1, eleven_multilingual_v2, and eleven_turbo_v2.
Advanced features include SSML markup support for controlling prosody, emphasis, and breaks in generated speech. The skill streams audio output in real-time using chunked transfer encoding for low-latency playback.
Integrates with the elevenlabs-python SDK for programmatic control, and supports output in mp3, pcm, ulaw, and opus formats. Rate limiting and quota tracking are built in to manage API usage across generation requests.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elevenlabs-voice-cloning-agent/)
