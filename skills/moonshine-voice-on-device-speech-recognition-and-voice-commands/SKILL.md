---
title: "Moonshine Voice On-Device Speech Recognition and Voice Commands"
description: "Moonshine Voice is a fast on-device speech recognition library for interactive voice applications. This skill helps agents install the Python package, load supported language models, transcribe live microphone input, and wire transcript events into local voice-command workflows."
slug: "moonshine-voice-on-device-speech-recognition-and-voice-commands"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/moonshine-ai/moonshine"
tool_ecosystem:
  github_repo: "moonshine-ai/moonshine"
  github_stars: 7663
listed: true
---

# Moonshine Voice On-Device Speech Recognition and Voice Commands

Moonshine Voice is a fast on-device speech recognition library for interactive voice applications. This skill helps agents install the Python package, load supported language models, transcribe live microphone input, and wire transcript events into local voice-command workflows.

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
clawhub install moonshine-voice-on-device-speech-recognition-and-voice-commands
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Moonshine Voice is the Python package behind the Moonshine project for fast, accurate, on-device automatic speech recognition. It is aimed at interactive voice applications rather than hosted transcription APIs, which makes it especially useful for privacy-sensitive, low-latency, or edge-device workflows. An ASE skill for Moonshine Voice gives agents a concrete way to set up local transcription, stream audio into a transcriber, and build voice-command interfaces without shipping raw audio to a cloud service.
The upstream package exposes components such as MicTranscriber, Transcriber, and IntentRecognizer. That means a skill can do more than basic speech-to-text: it can help an agent choose a language model with get_model_for_language(), start microphone capture, process transcript events in real time, and register intents that trigger local actions like device control or workflow automation. The PyPI package also documents supported languages and shows how to feed arbitrary audio chunks into the transcription stream when microphone input is not the source.
For ASE intake, Moonshine Voice clears the trust gate cleanly: the official GitHub repo exists, the PyPI package exists, the project documents installation and examples, and recent activity is visible. The skill’s job-to-be-done is concrete: install the package, download the right model, transcribe speech locally, and optionally add intent recognition for voice commands. Typical outputs include setup instructions, sample Python snippets, model selection guidance, and troubleshooting for audio capture or language support.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/moonshine-voice-on-device-speech-recognition-and-voice-commands/)
