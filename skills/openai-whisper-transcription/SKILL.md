---
name: "OpenAI Whisper Transcription"
slug: "openai-whisper-transcription"
description: "Local speech-to-text transcription without relying on an API."
github_stars: 99708
verification: "listed"
source: "https://github.com/openai/whisper"
author: "OpenAI"
publisher_type: "open_source_collective"
category: "Media & Transcription"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 99708
---

# OpenAI Whisper Transcription

Local speech-to-text transcription without relying on an API.

## Prerequisites

Python, pip, FFmpeg

## Installation

Use the upstream install or setup path that matches your environment:
- pip install -U openai-whisper
- pip install git+https://github.com/openai/whisper.git
- pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
- brew install ffmpeg

Requirements and caveats from upstream:
- We used Python 3.9.9 and [PyTorch](https://pytorch.org/) 1.10.1 to train and test our models, but the codebase is expected to be compatible with Python 3.8-3.11 and recent PyTorch versions. The codebase also depends o...
- Alternatively, the following command will pull and install the latest commit from this repository, along with its Python dependencies:
- It also requires the command-line tool [ffmpeg](https://ffmpeg.org/) to be installed on your system, which is available from most package managers:

Basic usage or getting-started notes:
- [[Colab example]](https://colab.research.google.com/github/openai/whisper/blob/master/notebooks/LibriSpeech.ipynb)
- To update the package to the latest version of this repository, please run:
- bash

- Source: https://github.com/openai/whisper
- Extracted from upstream docs: https://raw.githubusercontent.com/openai/whisper/HEAD/README.md

## Documentation

- https://github.com/openclaw/openclaw/tree/main/skills/openai-whisper/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openai-whisper-transcription/)
