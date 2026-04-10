---
title: "RealtimeSTT Low-Latency Speech-to-Text Python Library"
description: "RealtimeSTT is a Python library for real-time speech-to-text with advanced voice activity detection, wake word activation, and instant transcription. It combines WebRTC VAD, Silero VAD, and Faster Whisper for production-grade voice input in agent applications."
slug: "realtimestt-low-latency-speech-to-text-python"
category:
  - "Media &amp; Transcription"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/KoljaB/RealtimeSTT"
---

# RealtimeSTT Low-Latency Speech-to-Text Python Library

RealtimeSTT is a Python library for real-time speech-to-text with advanced voice activity detection, wake word activation, and instant transcription. It combines WebRTC VAD, Silero VAD, and Faster Whisper for production-grade voice input in agent applications.

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
clawhub install realtimestt-low-latency-speech-to-text-python
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

RealtimeSTT is a Python library that provides easy-to-use, low-latency speech-to-text conversion designed for real-time applications. Created by Kolja Beigel, it combines industry-standard components for voice activity detection and speech recognition into a unified API that handles the complex pipeline of listening, detecting speech boundaries, and transcribing audio.
Architecture
The library uses a multi-stage processing pipeline. First, WebRTC VAD performs initial voice activity detection with minimal latency. Silero VAD then provides more accurate verification to reduce false positives. Finally, Faster Whisper handles GPU-accelerated transcription using OpenAI’s Whisper models. For wake word detection, it supports both Picovoice Porcupine and OpenWakeWord.
Core Features
- Automatic voice activity detection that identifies speech start and stop points
- Real-time transcription with configurable Whisper model sizes (tiny through large-v3)
- Wake word activation using Porcupine or OpenWakeWord for hands-free operation
- Client-server architecture with AudioToTextRecorderClient for distributed deployments
- CLI interface with stt-server and stt commands for quick integration
- Callback-based API for processing transcribed text as it becomes available
Agent Integration
RealtimeSTT is particularly valuable for building voice-controlled AI agents and assistants. Its AudioToTextRecorder class provides a simple interface where agents receive transcribed text through callbacks, making it straightforward to pipe voice input into LLM-based conversation systems. The library handles all the complexity of microphone input, silence detection, and transcription timing.
Usage
Basic usage requires just a few lines of Python. Initialize AudioToTextRecorder, then call recorder.text() in a loop with a callback function. The library automatically manages audio capture, speech detection, and transcription. GPU acceleration via CUDA significantly improves transcription speed for larger models.
The library is available on PyPI via pip install RealtimeSTT and is MIT-licensed. It has over 9,600 GitHub stars and an active community. The companion library RealtimeTTS handles the output side for complete voice conversation systems.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/realtimestt-low-latency-speech-to-text-python/)
