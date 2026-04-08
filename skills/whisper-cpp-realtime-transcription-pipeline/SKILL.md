---
title: Whisper.cpp Real-Time Transcription Pipeline
description: This skill configures whisper.cpp for continuous real-time transcription
  from live audio sources. It captures audio via PulseAudio’s parec or ALSA’s arecord
  utilities, pipes PCM data into whisper.cpp’s streaming mode with configurable model
  sizes (tiny through large-v3). The pipeline produces word-level timestamps with
  confidence scores, outputting simultaneously to SRT subtitle files, WebVTT for web
  players, and structured JSON for downstream processing. It supports Voice Activity
  Detection via Silero VAD to skip silence and reduce compute. Language auto-detection
  uses whisper.cpp’s built-in classifier, with manual override available. The skill
  handles microphone hot-plugging gracefully using udev rules and systemd socket activation.
  For multi-speaker scenarios, it integrates with pyannote-audio for speaker diarization
  as a post-processing step. GPU acceleration is supported via CUDA, Metal, and Vulkan
  backends. Configuration includes buffer size tuning, beam search parameters, and
  custom vocabulary via initial prompt injection.
verification: security_reviewed
source: https://agentskillexchange.com/skills/whisper-cpp-realtime-transcription-pipeline/
category:
- Media &amp; Transcription
framework:
- Claude Code
---

# Whisper.cpp Real-Time Transcription Pipeline

This skill configures whisper.cpp for continuous real-time transcription from live audio sources. It captures audio via PulseAudio’s parec or ALSA’s arecord utilities, pipes PCM data into whisper.cpp’s streaming mode with configurable model sizes (tiny through large-v3). The pipeline produces word-level timestamps with confidence scores, outputting simultaneously to SRT subtitle files, WebVTT for web players, and structured JSON for downstream processing. It supports Voice Activity Detection via Silero VAD to skip silence and reduce compute. Language auto-detection uses whisper.cpp’s built-in classifier, with manual override available. The skill handles microphone hot-plugging gracefully using udev rules and systemd socket activation. For multi-speaker scenarios, it integrates with pyannote-audio for speaker diarization as a post-processing step. GPU acceleration is supported via CUDA, Metal, and Vulkan backends. Configuration includes buffer size tuning, beam search parameters, and custom vocabulary via initial prompt injection.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-cpp-realtime-transcription-pipeline/)
