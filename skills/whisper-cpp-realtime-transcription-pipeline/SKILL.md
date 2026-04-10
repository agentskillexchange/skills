---
title: "Whisper.cpp Real-Time Transcription Pipeline"
description: "Streams audio from PulseAudio or ALSA devices into whisper.cpp for real-time speech-to-text with word-level timestamps. Outputs SRT/VTT subtitles and JSON transcripts simultaneously."
slug: "whisper-cpp-realtime-transcription-pipeline"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/whisper-cpp-realtime-transcription-pipeline/"
---

# Whisper.cpp Real-Time Transcription Pipeline

Streams audio from PulseAudio or ALSA devices into whisper.cpp for real-time speech-to-text with word-level timestamps. Outputs SRT/VTT subtitles and JSON transcripts simultaneously.

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
clawhub install whisper-cpp-realtime-transcription-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill configures whisper.cpp for continuous real-time transcription from live audio sources. It captures audio via PulseAudio’s parec or ALSA’s arecord utilities, pipes PCM data into whisper.cpp’s streaming mode with configurable model sizes (tiny through large-v3). The pipeline produces word-level timestamps with confidence scores, outputting simultaneously to SRT subtitle files, WebVTT for web players, and structured JSON for downstream processing. It supports Voice Activity Detection via Silero VAD to skip silence and reduce compute. Language auto-detection uses whisper.cpp’s built-in classifier, with manual override available. The skill handles microphone hot-plugging gracefully using udev rules and systemd socket activation. For multi-speaker scenarios, it integrates with pyannote-audio for speaker diarization as a post-processing step. GPU acceleration is supported via CUDA, Metal, and Vulkan backends. Configuration includes buffer size tuning, beam search parameters, and custom vocabulary via initial prompt injection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-cpp-realtime-transcription-pipeline/)
