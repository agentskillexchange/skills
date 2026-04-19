---
title: "Moonshine Voice On-Device Speech Recognition and Voice Commands"
description: "Moonshine Voice is the Python package behind the Moonshine project for fast, accurate, on-device automatic speech recognition. It is aimed at interactive voice applications rather than hosted transcription APIs, which makes it especially useful for privacy-sensitive, low-latency, or edge-device workflows. An ASE skill for Moonshine Voice gives agents a concrete way to set up local transcription, stream audio into a transcriber, and build voice-command interfaces without shipping raw audio to a cloud service. The upstream package exposes components such as MicTranscriber , Transcriber , and IntentRecognizer . That means a skill can do more than basic speech-to-text: it can help an agent choose a language model with get_model_for_language() , start microphone capture, process transcript events in real time, and register intents that trigger local actions like device control or workflow automation. The PyPI package also documents supported languages and shows how to feed arbitrary audio chunks into the transcription stream when microphone input is not the source. For ASE intake, Moonshine Voice clears the trust gate cleanly: the official GitHub repo exists, the PyPI package exists, the project documents installation and examples, and recent activity is visible. The skill&#8217;s job-to-be-done is concrete: install the package, download the right model, transcribe speech locally, and optionally add intent recognition for voice commands. Typical outputs include setup instructions, sample Python snippets, model selection guidance, and troubleshooting for audio capture or language support."
source: "https://github.com/moonshine-ai/moonshine"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "moonshine-ai/moonshine"
  github_stars: 7672
---

# Moonshine Voice On-Device Speech Recognition and Voice Commands

Moonshine Voice is the Python package behind the Moonshine project for fast, accurate, on-device automatic speech recognition. It is aimed at interactive voice applications rather than hosted transcription APIs, which makes it especially useful for privacy-sensitive, low-latency, or edge-device workflows. An ASE skill for Moonshine Voice gives agents a concrete way to set up local transcription, stream audio into a transcriber, and build voice-command interfaces without shipping raw audio to a cloud service. The upstream package exposes components such as MicTranscriber , Transcriber , and IntentRecognizer . That means a skill can do more than basic speech-to-text: it can help an agent choose a language model with get_model_for_language() , start microphone capture, process transcript events in real time, and register intents that trigger local actions like device control or workflow automation. The PyPI package also documents supported languages and shows how to feed arbitrary audio chunks into the transcription stream when microphone input is not the source. For ASE intake, Moonshine Voice clears the trust gate cleanly: the official GitHub repo exists, the PyPI package exists, the project documents installation and examples, and recent activity is visible. The skill&#8217;s job-to-be-done is concrete: install the package, download the right model, transcribe speech locally, and optionally add intent recognition for voice commands. Typical outputs include setup instructions, sample Python snippets, model selection guidance, and troubleshooting for audio capture or language support.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/moonshine-voice-on-device-speech-recognition-and-voice-commands/)
