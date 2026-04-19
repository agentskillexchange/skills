---
title: "Whisper.cpp Real-Time Transcription Pipeline"
description: "This skill configures whisper.cpp for continuous real-time transcription from live audio sources. It captures audio via PulseAudio&#8217;s parec or ALSA&#8217;s arecord utilities, pipes PCM data into whisper.cpp&#8217;s streaming mode with configurable model sizes (tiny through large-v3). The pipeline produces word-level timestamps with confidence scores, outputting simultaneously to SRT subtitle files, WebVTT for web players, and structured JSON for downstream processing. It supports Voice Activity Detection via Silero VAD to skip silence and reduce compute. Language auto-detection uses whisper.cpp&#8217;s built-in classifier, with manual override available. The skill handles microphone hot-plugging gracefully using udev rules and systemd socket activation. For multi-speaker scenarios, it integrates with pyannote-audio for speaker diarization as a post-processing step. GPU acceleration is supported via CUDA, Metal, and Vulkan backends. Configuration includes buffer size tuning, beam search parameters, and custom vocabulary via initial prompt injection."
source: "https://github.com/openai/whisper"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97775
---

# Whisper.cpp Real-Time Transcription Pipeline

This skill configures whisper.cpp for continuous real-time transcription from live audio sources. It captures audio via PulseAudio&#8217;s parec or ALSA&#8217;s arecord utilities, pipes PCM data into whisper.cpp&#8217;s streaming mode with configurable model sizes (tiny through large-v3). The pipeline produces word-level timestamps with confidence scores, outputting simultaneously to SRT subtitle files, WebVTT for web players, and structured JSON for downstream processing. It supports Voice Activity Detection via Silero VAD to skip silence and reduce compute. Language auto-detection uses whisper.cpp&#8217;s built-in classifier, with manual override available. The skill handles microphone hot-plugging gracefully using udev rules and systemd socket activation. For multi-speaker scenarios, it integrates with pyannote-audio for speaker diarization as a post-processing step. GPU acceleration is supported via CUDA, Metal, and Vulkan backends. Configuration includes buffer size tuning, beam search parameters, and custom vocabulary via initial prompt injection.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-cpp-realtime-transcription-pipeline/)
