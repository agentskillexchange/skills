---
name: "Coqui TTS Deep Learning Text-to-Speech Toolkit"
slug: "coqui-tts-deep-learning-text-to-speech-toolkit"
description: "An agent skill built on Coqui TTS, the open-source deep learning toolkit for text-to-speech synthesis. Provides CLI and Python API access to multiple TTS model architectures including VITS, Tacotron2, and GlowTTS, with support for voice cloning, multilingual synthesis, and on-the-fly voice conversion."
github_stars: 44959
verification: "security_reviewed"
source: "https://github.com/coqui-ai/TTS"
category: "Media & Transcription"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "coqui-ai/TTS"
  github_stars: 44959
---

# Coqui TTS Deep Learning Text-to-Speech Toolkit

An agent skill built on Coqui TTS, the open-source deep learning toolkit for text-to-speech synthesis. Provides CLI and Python API access to multiple TTS model architectures including VITS, Tacotron2, and GlowTTS, with support for voice cloning, multilingual synthesis, and on-the-fly voice conversion.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install TTS
- git clone https://github.com/coqui-ai/TTS
- pip install -e .[all,dev,notebooks] # Select the relevant extras
- $ make system-deps # intended to be used on Ubuntu (Debian). Let us know if you have a different OS.

Requirements and caveats from upstream:
- ![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/docker.yaml/badge.svg)
- 🐸TTS is tested on Ubuntu 18.04 with **python >= 3.9, < 3.12.**.

Basic usage or getting-started notes:
- 📣 ⓍTTS fine-tuning code is out. Check the [example recipes](https://github.com/coqui-ai/TTS/tree/dev/recipes/ljspeech).
- | 👩‍💻 **Usage Questions** | [GitHub Discussions] |
- If you are only interested in [synthesizing speech](https://tts.readthedocs.io/en/latest/inference.html) with the released 🐸TTS models, installing from PyPI is the easiest option.

- Source: https://github.com/coqui-ai/TTS
- Extracted from upstream docs: https://raw.githubusercontent.com/coqui-ai/TTS/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coqui-tts-deep-learning-text-to-speech-toolkit/)
