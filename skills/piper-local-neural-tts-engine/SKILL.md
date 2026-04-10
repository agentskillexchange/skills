---
title: "Piper Local Neural Text-to-Speech Engine"
description: "Run fast, high-quality neural text-to-speech locally with Piper. Supports 20+ languages with compact ONNX voice models, no cloud API required, and produces natural-sounding speech on CPUs including Raspberry Pi."
slug: "piper-local-neural-tts-engine"
category:
  - "Media &amp; Transcription"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/rhasspy/piper"
tool_ecosystem:
  github_repo: "rhasspy/piper"
  github_stars: 10741
---

# Piper Local Neural Text-to-Speech Engine

Run fast, high-quality neural text-to-speech locally with Piper. Supports 20+ languages with compact ONNX voice models, no cloud API required, and produces natural-sounding speech on CPUs including Raspberry Pi.

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
clawhub install piper-local-neural-tts-engine
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

What is Piper?
Piper is a fast, local neural text-to-speech (TTS) system developed by the Rhasspy project and now maintained by the Open Home Foundation. It converts text to natural-sounding speech using lightweight ONNX neural network models that run entirely on-device — no cloud API calls, no internet connection required. Piper is designed for voice assistants, accessibility tools, and any application that needs offline speech synthesis.
How This Skill Works
This skill enables agents to synthesize speech from text using the Piper TTS engine. Agents can select from a library of pre-trained voice models covering 20+ languages including English, German, French, Spanish, Chinese, Russian, and many more. The engine processes text through an espeak-ng phonemizer, then feeds phoneme sequences through a VITS-based neural network to produce raw audio output. The entire pipeline runs locally on CPU with sub-real-time latency on modern hardware.
Key Capabilities
- Offline operation: All processing happens locally. Models are compact ONNX files (15-100 MB) that load quickly and run without GPU acceleration.
- Multi-language support: Pre-trained voices available for English (US/UK), German, French, Spanish, Portuguese, Italian, Dutch, Russian, Chinese, Arabic, Hindi, Japanese, and 10+ more languages.
- Voice quality tiers: Choose between low, medium, and high quality models trading off file size and CPU usage for naturalness. High-quality models use multi-speaker VITS architectures.
- Streaming output: Piper supports streaming audio generation, outputting PCM audio chunks as they are synthesized for low-latency real-time playback.
- CLI and library usage: Use the piper command-line tool to pipe text in and get WAV audio out, or link against the C++ library for embedding in applications. Python bindings available via piper-tts on PyPI.
Integration Points
Piper integrates with Home Assistant for voice assistant pipelines, with Wyoming protocol for modular voice satellite setups, and with any system that can consume WAV or raw PCM audio. It outputs 16-bit mono audio at configurable sample rates (16kHz or 22.05kHz depending on the model). The CLI accepts text via stdin and writes audio to stdout, making it composable with ffmpeg, sox, aplay, and other audio tools via shell pipes. Docker images are available for containerized deployments.
Source
GitHub: rhasspy/piper (10.7K+ stars, MIT license) — New development: OHF-Voice/piper1-gpl

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/piper-local-neural-tts-engine/)
