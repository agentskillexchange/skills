---
title: ElevenLabs Voice Cloning Agent
description: Build custom voice profiles and generate natural speech using the ElevenLabs
  API v2 endpoint. This skill handles the full voice cloning workflow from sample
  upload through synthesis output. The agent manages voice library operations including
  creating instant voice clones from audio samples via POST /v1/voices/add, listing
  available voices, and editing voice settings (stability, similarity_boost, style,
  use_speaker_boost). Text-to-speech requests are sent to /v1/text-to-speech/{voice_id}
  with configurable model selection between eleven_monolingual_v1, eleven_multilingual_v2,
  and eleven_turbo_v2. Advanced features include SSML markup support for controlling
  prosody, emphasis, and breaks in generated speech. The skill streams audio output
  in real-time using chunked transfer encoding for low-latency playback. Integrates
  with the elevenlabs-python SDK for programmatic control, and supports output in
  mp3, pcm, ulaw, and opus formats. Rate limiting and quota tracking are built in
  to manage API usage across generation requests.
verification: security_reviewed
source: https://agentskillexchange.com/skills/elevenlabs-voice-cloning-agent/
category:
- Media &amp; Transcription
framework:
- OpenClaw
---

# ElevenLabs Voice Cloning Agent

Build custom voice profiles and generate natural speech using the ElevenLabs API v2 endpoint. This skill handles the full voice cloning workflow from sample upload through synthesis output. The agent manages voice library operations including creating instant voice clones from audio samples via POST /v1/voices/add, listing available voices, and editing voice settings (stability, similarity_boost, style, use_speaker_boost). Text-to-speech requests are sent to /v1/text-to-speech/{voice_id} with configurable model selection between eleven_monolingual_v1, eleven_multilingual_v2, and eleven_turbo_v2. Advanced features include SSML markup support for controlling prosody, emphasis, and breaks in generated speech. The skill streams audio output in real-time using chunked transfer encoding for low-latency playback. Integrates with the elevenlabs-python SDK for programmatic control, and supports output in mp3, pcm, ulaw, and opus formats. Rate limiting and quota tracking are built in to manage API usage across generation requests.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elevenlabs-voice-cloning-agent/)
