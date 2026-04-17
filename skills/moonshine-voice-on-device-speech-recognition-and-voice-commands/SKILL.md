---
title: "Moonshine Voice On-Device Speech Recognition and Voice Commands"
description: "Moonshine Voice is the Python package behind the Moonshine project for fast, accurate, on-device automatic speech recognition. It is aimed at interactive voice applications rather than hosted transcription APIs, which makes it especially useful for privacy-sensitive, low-latency, or edge-device workflows. An ASE skill for Moonshine Voice gives agents a concrete way to set up local transcription, stream audio into a transcriber, and build voice-command interfaces without shipping raw audio to a cloud service.\nThe upstream package exposes components such as MicTranscriber, Transcriber, and IntentRecognizer. That means a skill can do more than basic speech-to-text: it can help an agent choose a language model with get_model_for_language(), start microphone capture, process transcript events in real time, and register intents that trigger local actions like device control or workflow automation. The PyPI package also documents supported languages and shows how to feed arbitrary audio chunks into the transcription stream when microphone input is not the source.\nFor ASE intake, Moonshine Voice clears the trust gate cleanly: the official GitHub repo exists, the PyPI package exists, the project documents installation and examples, and recent activity is visible. The skill’s job-to-be-done is concrete: install the package, download the right model, transcribe speech locally, and optionally add intent recognition for voice commands. Typical outputs include setup instructions, sample Python snippets, model selection guidance, and troubleshooting for audio capture or language support."
verification: security_reviewed
source: "https://github.com/moonshine-ai/moonshine"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "moonshine-ai/moonshine"
  github_stars: 7672
---

# Moonshine Voice On-Device Speech Recognition and Voice Commands

Moonshine Voice is the Python package behind the Moonshine project for fast, accurate, on-device automatic speech recognition. It is aimed at interactive voice applications rather than hosted transcription APIs, which makes it especially useful for privacy-sensitive, low-latency, or edge-device workflows. An ASE skill for Moonshine Voice gives agents a concrete way to set up local transcription, stream audio into a transcriber, and build voice-command interfaces without shipping raw audio to a cloud service.
The upstream package exposes components such as MicTranscriber, Transcriber, and IntentRecognizer. That means a skill can do more than basic speech-to-text: it can help an agent choose a language model with get_model_for_language(), start microphone capture, process transcript events in real time, and register intents that trigger local actions like device control or workflow automation. The PyPI package also documents supported languages and shows how to feed arbitrary audio chunks into the transcription stream when microphone input is not the source.
For ASE intake, Moonshine Voice clears the trust gate cleanly: the official GitHub repo exists, the PyPI package exists, the project documents installation and examples, and recent activity is visible. The skill’s job-to-be-done is concrete: install the package, download the right model, transcribe speech locally, and optionally add intent recognition for voice commands. Typical outputs include setup instructions, sample Python snippets, model selection guidance, and troubleshooting for audio capture or language support.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/moonshine-voice-on-device-speech-recognition-and-voice-commands
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/moonshine-voice-on-device-speech-recognition-and-voice-commands` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/moonshine-voice-on-device-speech-recognition-and-voice-commands/)
