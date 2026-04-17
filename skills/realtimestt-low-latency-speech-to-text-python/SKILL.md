---
title: "RealtimeSTT Low-Latency Speech-to-Text Python Library"
description: "RealtimeSTT is a Python library that provides easy-to-use, low-latency speech-to-text conversion designed for real-time applications. Created by Kolja Beigel, it combines industry-standard components for voice activity detection and speech recognition into a unified API that handles the complex pipeline of listening, detecting speech boundaries, and transcribing audio.\nArchitecture\nThe library uses a multi-stage processing pipeline. First, WebRTC VAD performs initial voice activity detection with minimal latency. Silero VAD then provides more accurate verification to reduce false positives. Finally, Faster Whisper handles GPU-accelerated transcription using OpenAI’s Whisper models. For wake word detection, it supports both Picovoice Porcupine and OpenWakeWord.\nCore Features\n\nAutomatic voice activity detection that identifies speech start and stop points\nReal-time transcription with configurable Whisper model sizes (tiny through large-v3)\nWake word activation using Porcupine or OpenWakeWord for hands-free operation\nClient-server architecture with AudioToTextRecorderClient for distributed deployments\nCLI interface with stt-server and stt commands for quick integration\nCallback-based API for processing transcribed text as it becomes available\n\nAgent Integration\nRealtimeSTT is particularly valuable for building voice-controlled AI agents and assistants. Its AudioToTextRecorder class provides a simple interface where agents receive transcribed text through callbacks, making it straightforward to pipe voice input into LLM-based conversation systems. The library handles all the complexity of microphone input, silence detection, and transcription timing.\nUsage\nBasic usage requires just a few lines of Python. Initialize AudioToTextRecorder, then call recorder.text() in a loop with a callback function. The library automatically manages audio capture, speech detection, and transcription. GPU acceleration via CUDA significantly improves transcription speed for larger models.\nThe library is available on PyPI via pip install RealtimeSTT and is MIT-licensed. It has over 9,600 GitHub stars and an active community. The companion library RealtimeTTS handles the output side for complete voice conversation systems."
verification: security_reviewed
source: "https://github.com/KoljaB/RealtimeSTT"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "koljab/realtimestt"
  github_stars: 9615
---

# RealtimeSTT Low-Latency Speech-to-Text Python Library

RealtimeSTT is a Python library that provides easy-to-use, low-latency speech-to-text conversion designed for real-time applications. Created by Kolja Beigel, it combines industry-standard components for voice activity detection and speech recognition into a unified API that handles the complex pipeline of listening, detecting speech boundaries, and transcribing audio.
Architecture
The library uses a multi-stage processing pipeline. First, WebRTC VAD performs initial voice activity detection with minimal latency. Silero VAD then provides more accurate verification to reduce false positives. Finally, Faster Whisper handles GPU-accelerated transcription using OpenAI’s Whisper models. For wake word detection, it supports both Picovoice Porcupine and OpenWakeWord.
Core Features

Automatic voice activity detection that identifies speech start and stop points
Real-time transcription with configurable Whisper model sizes (tiny through large-v3)
Wake word activation using Porcupine or OpenWakeWord for hands-free operation
Client-server architecture with AudioToTextRecorderClient for distributed deployments
CLI interface with stt-server and stt commands for quick integration
Callback-based API for processing transcribed text as it becomes available

Agent Integration
RealtimeSTT is particularly valuable for building voice-controlled AI agents and assistants. Its AudioToTextRecorder class provides a simple interface where agents receive transcribed text through callbacks, making it straightforward to pipe voice input into LLM-based conversation systems. The library handles all the complexity of microphone input, silence detection, and transcription timing.
Usage
Basic usage requires just a few lines of Python. Initialize AudioToTextRecorder, then call recorder.text() in a loop with a callback function. The library automatically manages audio capture, speech detection, and transcription. GPU acceleration via CUDA significantly improves transcription speed for larger models.
The library is available on PyPI via pip install RealtimeSTT and is MIT-licensed. It has over 9,600 GitHub stars and an active community. The companion library RealtimeTTS handles the output side for complete voice conversation systems.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/realtimestt-low-latency-speech-to-text-python
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/realtimestt-low-latency-speech-to-text-python` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/realtimestt-low-latency-speech-to-text-python/)
