---
title: "Chatterbox State-of-the-Art Open Source Text-to-Speech"
description: "An agent skill built on Chatterbox by Resemble AI, a state-of-the-art open-source text-to-speech model with zero-shot voice cloning and multilingual synthesis. Generates natural-sounding speech from text with support for 23 languages, voice cloning from reference audio, and emotion/style control."
slug: "chatterbox-sota-open-source-text-to-speech"
category:
  - "Media &amp; Transcription"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/resemble-ai/chatterbox"
tool_ecosystem:
  github_repo: "resemble-ai/chatterbox"
  github_stars: 24089
listed: true
---

# Chatterbox State-of-the-Art Open Source Text-to-Speech

An agent skill built on Chatterbox by Resemble AI, a state-of-the-art open-source text-to-speech model with zero-shot voice cloning and multilingual synthesis. Generates natural-sounding speech from text with support for 23 languages, voice cloning from reference audio, and emotion/style control.

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
clawhub install chatterbox-sota-open-source-text-to-speech
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Chatterbox is a state-of-the-art open-source text-to-speech model developed by Resemble AI. Released under the MIT license with over 24,000 GitHub stars, it delivers production-quality speech synthesis competitive with commercial TTS APIs while running fully locally.
Architecture and Quality
Chatterbox uses an end-to-end neural architecture that generates speech directly from text without separate acoustic model and vocoder stages. The model produces highly natural prosody and intonation, achieving low word error rates on standard benchmarks. The architecture supports both single-speaker and multi-speaker configurations.
Zero-Shot Voice Cloning
A key capability is zero-shot voice cloning: provide a short reference audio clip (as little as 5-10 seconds) and Chatterbox will synthesize new speech in that voice without any fine-tuning or training. This works via speaker embedding extraction from the reference audio, which conditions the generation model on the target voice characteristics.
Multilingual Support
The multilingual variant of Chatterbox supports 23 languages including English, French, German, Spanish, Chinese, Japanese, Korean, Hindi, Arabic, and more. Each language uses the same model architecture with language-specific conditioning, enabling cross-lingual voice cloning where a voice sample in one language drives synthesis in another.
Python API
Install from PyPI with pip install chatterbox-tts. The API is straightforward: load the model, call model.generate(text) for default synthesis, or pass audio_prompt_path for voice cloning. Output is a waveform tensor that can be saved with torchaudio. GPU acceleration via CUDA is supported for faster inference.
Agent Integration
Chatterbox fits naturally into agent workflows that need speech output: generate voice responses, create audio content, produce podcast-style narration, or build voice interfaces. The MIT license and local execution model mean no API keys, rate limits, or data privacy concerns.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chatterbox-sota-open-source-text-to-speech/)
