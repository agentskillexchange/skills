---
title: "Silero VAD Pre-Trained Enterprise Voice Activity Detection"
description: "Silero VAD is a pre-trained enterprise-grade Voice Activity Detector that identifies speech segments in audio streams. It runs locally via PyTorch or ONNX Runtime with minimal resource requirements, making it ideal for real-time audio processing pipelines."
slug: "silero-vad-voice-activity-detection"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/snakers4/silero-vad"
tool_ecosystem:
  github_repo: "snakers4/silero-vad"
  github_stars: 8604
---

# Silero VAD Pre-Trained Enterprise Voice Activity Detection

Silero VAD is a pre-trained enterprise-grade Voice Activity Detector that identifies speech segments in audio streams. It runs locally via PyTorch or ONNX Runtime with minimal resource requirements, making it ideal for real-time audio processing pipelines.

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
clawhub install silero-vad-voice-activity-detection
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Silero VAD is a pre-trained, enterprise-grade Voice Activity Detector developed by the Silero team. It detects speech segments in audio with high accuracy, running efficiently on CPU with minimal memory footprint. The model supports both PyTorch and ONNX Runtime backends, enabling deployment on embedded systems, mobile devices, and servers alike.
Core Capabilities
Silero VAD processes audio at 16kHz or 8kHz sampling rates and returns precise speech timestamps. It excels at distinguishing speech from background noise, music, and other non-speech audio. The detector runs in real-time with sub-millisecond latency per audio chunk, requiring only 1GB of RAM and a modern CPU with AVX instruction support.
How It Works
Install via pip install silero-vad and load the model with a single function call. Feed audio data in chunks and receive speech probability scores or timestamp ranges. The library provides utility functions for reading audio files, extracting speech segments, and saving results. Integration through torch.hub is also supported for zero-dependency setups.
Agent Integration
AI agents use Silero VAD as a preprocessing step in audio intelligence pipelines. Before running expensive transcription with Whisper or speaker diarization, VAD identifies which portions of audio contain speech, reducing processing time and cost. It is the default VAD used by WhisperX, faster-whisper, and many real-time transcription systems. The model runs entirely offline with no API calls required.
Key Features
- Enterprise-grade accuracy with sub-millisecond latency
- PyTorch and ONNX Runtime backends
- Supports 16kHz and 8kHz audio
- Real-time streaming and batch processing
- Minimal dependencies (torch or onnxruntime)
- MIT license, free for commercial use
- Used as default VAD in WhisperX and faster-whisper

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/silero-vad-voice-activity-detection/)
