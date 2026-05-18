---
name: "YouTube Chapters Generator with Whisper"
slug: "youtube-chapters-generator-whisper"
description: "Downloads YouTube audio via yt-dlp, transcribes with Whisper, and uses NLP topic segmentation via TextTiling algorithm to auto-generate chapter markers with timestamps and titles."
github_stars: 97803
verification: "listed"
source: "https://github.com/openai/whisper"
category: "Media & Transcription"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97803
---

# YouTube Chapters Generator with Whisper

Downloads YouTube audio via yt-dlp, transcribes with Whisper, and uses NLP topic segmentation via TextTiling algorithm to auto-generate chapter markers with timestamps and titles.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/youtube-chapters-generator-whisper/)
