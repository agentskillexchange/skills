---
name: "OpenAI Whisper Batch Transcription Pipeline"
slug: "whisper-batch-transcription-pipeline"
description: "Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English."
github_stars: 97803
verification: "security_reviewed"
source: "https://github.com/openai/whisper"
category: "Media & Transcription"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97803
---

# OpenAI Whisper Batch Transcription Pipeline

Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English.

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

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/)
