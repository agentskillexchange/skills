---
name: "Whisper.cpp Real-Time Transcription Pipeline"
description: "Streams audio from PulseAudio or ALSA devices into whisper.cpp for real-time speech-to-text with word-level timestamps. Outputs SRT/VTT subtitles and JSON transcripts simultaneously."
category: "Media & Transcription"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/whisper-cpp-realtime-transcription-pipeline/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "whisper"  # from ase_tool_match
  github_stars: 96530  # from ase_github_stars (integer, not string)
  github_repo: "openai/whisper"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Whisper.cpp Real-Time Transcription Pipeline

Streams audio from PulseAudio or ALSA devices into whisper.cpp for real-time speech-to-text with word-level timestamps. Outputs SRT/VTT subtitles and JSON transcripts simultaneously.

## Overview

This skill configures whisper.cpp for continuous real-time transcription from live audio sources. It captures audio via PulseAudio’s parec or ALSA’s arecord utilities, pipes PCM data into whisper.cpp’s streaming mode with configurable model sizes (tiny through large-v3). The pipeline produces word-level timestamps with confidence scores, outputting simultaneously to SRT subtitle files, WebVTT for web players, and structured JSON for downstream processing. It supports Voice Activity Detection via Silero VAD to skip silence and reduce compute. Language auto-detection uses whisper.cpp’s built-in classifier, with manual override available. The skill handles microphone hot-plugging gracefully using udev rules and systemd socket activation. For multi-speaker scenarios, it integrates with pyannote-audio for speaker diarization as a post-processing step. GPU acceleration is supported via CUDA, Metal, and Vulkan backends. Configuration includes buffer size tuning, beam search parameters, and custom vocabulary via initial prompt injection.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill whisper-cpp-realtime-transcription-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill whisper-cpp-realtime-transcription-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill whisper-cpp-realtime-transcription-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill whisper-cpp-realtime-transcription-pipeline -a codex
```

### OpenClaw

```bash
clawhub install whisper-cpp-realtime-transcription-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/whisper-cpp-realtime-transcription-pipeline/
