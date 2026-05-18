---
name: "Podcast RSS Feed Transcriber"
slug: "podcast-rss-feed-transcriber"
description: "Automatically fetches podcast episodes from RSS feeds using feedparser, downloads audio enclosures, and transcribes them through OpenAI Whisper API or local faster-whisper models. Generates timestamped SRT files and searchable markdown transcripts with speaker diarization via pyannote.audio."
github_stars: 97391
verification: "listed"
source: "https://github.com/openai/whisper"
author: "openai"
category: "Media & Transcription"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97391
---

# Podcast RSS Feed Transcriber

Automatically fetches podcast episodes from RSS feeds using feedparser, downloads audio enclosures, and transcribes them through OpenAI Whisper API or local faster-whisper models. Generates timestamped SRT files and searchable markdown transcripts with speaker diarization via pyannote.audio.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-transcriber/)
