---
title: "Vosk Offline Speech Recognition Toolkit"
description: "Perform offline speech recognition across 20+ languages with Vosk. Provides compact models, zero-latency streaming transcription, and bindings for Python, Node.js, Java, C#, and Go — all without cloud API dependencies."
verification: "security_reviewed"
source: "https://github.com/alphacep/vosk-api"
category:
  - "Media & Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "alphacep/vosk-api"
  github_stars: 14474
  license: "Apache-2.0"
---

# Vosk Offline Speech Recognition Toolkit

What is Vosk?
Vosk is an open-source offline speech recognition toolkit developed by Alpha Cephei. It provides accurate speech-to-text transcription for 20+ languages using compact acoustic models that run entirely on-device. Unlike cloud-based ASR services, Vosk requires no internet connection, sends no audio data externally, and operates with zero-latency streaming response — making it ideal for privacy-sensitive applications, embedded devices, and real-time transcription scenarios.


How This Skill Works
This skill enables agents to transcribe audio to text using the Vosk speech recognition API. Agents load a pre-trained language model (as small as 50 MB for lightweight models, or 1-2 GB for large-vocabulary models), create a recognizer instance configured for the audio sample rate, and feed audio data through the recognizer in chunks. Vosk returns partial results in real-time as audio streams in, and final results when utterances complete, all formatted as JSON with word-level timestamps and confidence scores.


Key Capabilities

Multi-language support: Pre-trained models for English, German, French, Spanish, Portuguese, Chinese, Russian, Turkish, Vietnamese, Italian, Dutch, Arabic, Greek, Hindi, Japanese, Ukrainian, and more.
Streaming recognition: Process audio in real-time with streaming API that returns partial hypotheses as speech is detected, enabling live captioning and voice command scenarios.
Speaker identification: Built-in speaker diarization support identifies different speakers in multi-party conversations without additional models.
Reconfigurable vocabulary: Dynamically set grammar and vocabulary constraints to improve accuracy for domain-specific recognition (menu navigation, command sets, specialized terminology).
Cross-platform bindings: Native API bindings for Python, Node.js, Java, C#, C++, Rust, and Go. Works on Linux, Windows, macOS, Android, iOS, and Raspberry Pi.

Integration Points
Vosk accepts PCM audio input at 8kHz or 16kHz sample rates in mono format. It integrates with ffmpeg for audio format conversion, with WebSocket servers for browser-based real-time transcription, and with microphone input via PyAudio or PortAudio for live transcription. The Python package installs via pip install vosk and the Node.js package via npm install vosk. Output is structured JSON containing transcript text, word-level timings, and confidence scores suitable for downstream NLP processing.


Source
GitHub: alphacep/vosk-api (14.4K+ stars, Apache-2.0 license) — Docs: alphacephei.com/vosk

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vosk-offline-speech-recognition-toolkit/)
