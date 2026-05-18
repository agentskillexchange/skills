---
name: "Moonshine Voice On-Device Speech Recognition and Voice Commands"
slug: "moonshine-voice-on-device-speech-recognition-and-voice-commands"
description: "Moonshine Voice is a fast on-device speech recognition library for interactive voice applications. This skill helps agents install the Python package, load supported language models, transcribe live microphone input, and wire transcript events into local voice-command workflows."
github_stars: 7672
verification: "listed"
source: "https://github.com/moonshine-ai/moonshine"
author: "moonshine-ai"
publisher_type: "Open Source Project"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "moonshine-ai/moonshine"
  github_stars: 7672
---

# Moonshine Voice On-Device Speech Recognition and Voice Commands

Moonshine Voice is a fast on-device speech recognition library for interactive voice applications. This skill helps agents install the Python package, load supported language models, transcribe live microphone input, and wire transcript events into local voice-command workflows.

## Prerequisites

Python 3 environment, microphone or other audio source, and downloaded Moonshine language models for the target language.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install moonshine-voice
- cmake ..
- cmake --build .
- uv run -m moonshine_voice.transcriber --options='log_api_calls=true'

Requirements and caveats from upstream:
- It's easy to integrate across platforms, with the same library running on [Python](#python), [iOS](#ios), [Android](#android), [MacOS](#macos), [Linux](#linux), [Windows](#windows), [Raspberry Pis](#raspberry-pi), [Io...
- ### Python
- python -m moonshine_voice.mic_transcriber --language en

Basic usage or getting-started notes:
- [Join our community on Discord to get live support](https://discord.gg/27qp9zSRXF).
- Example apps for iOS, Android, macOS, Windows, and Raspberry Pi are published on [GitHub Releases](https://github.com/moonshine-ai/moonshine/releases/latest) as separate archives (mostly **{platform}-{Project}.tar.gz*...
- bash

- Source: https://github.com/moonshine-ai/moonshine
- Extracted from upstream docs: https://raw.githubusercontent.com/moonshine-ai/moonshine/HEAD/README.md

## Documentation

- https://github.com/moonshine-ai/moonshine/blob/main/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/moonshine-voice-on-device-speech-recognition-and-voice-commands/)
