---
title: "ElevenLabs Voice Cloning Agent"
description: "Build custom voice profiles and generate natural speech using the ElevenLabs API v2 endpoint. This skill handles the full voice cloning workflow from sample upload through synthesis output. The agent manages voice library operations including creating instant voice clones from audio samples via POST /v1/voices/add, listing available voices, and editing voice settings (stability, similarity_boost, style, use_speaker_boost). Text-to-speech requests are sent to /v1/text-to-speech/{voice_id} with configurable model selection between eleven_monolingual_v1, eleven_multilingual_v2, and eleven_turbo_v2. Advanced features include SSML markup support for controlling prosody, emphasis, and breaks in generated speech. The skill streams audio output in real-time using chunked transfer encoding for low-latency playback. Integrates with the elevenlabs-python SDK for programmatic control, and supports output in mp3, pcm, ulaw, and opus formats. Rate limiting and quota tracking are built in to manage API usage across generation requests."
source: "https://elevenlabs.io/docs/overview"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
---

# ElevenLabs Voice Cloning Agent

Build custom voice profiles and generate natural speech using the ElevenLabs API v2 endpoint. This skill handles the full voice cloning workflow from sample upload through synthesis output. The agent manages voice library operations including creating instant voice clones from audio samples via POST /v1/voices/add, listing available voices, and editing voice settings (stability, similarity_boost, style, use_speaker_boost). Text-to-speech requests are sent to /v1/text-to-speech/{voice_id} with configurable model selection between eleven_monolingual_v1, eleven_multilingual_v2, and eleven_turbo_v2. Advanced features include SSML markup support for controlling prosody, emphasis, and breaks in generated speech. The skill streams audio output in real-time using chunked transfer encoding for low-latency playback. Integrates with the elevenlabs-python SDK for programmatic control, and supports output in mp3, pcm, ulaw, and opus formats. Rate limiting and quota tracking are built in to manage API usage across generation requests.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elevenlabs-voice-cloning-agent/)
