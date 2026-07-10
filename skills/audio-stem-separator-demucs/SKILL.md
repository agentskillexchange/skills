---
name: "Audio Stem Separator with Demucs"
slug: "audio-stem-separator-demucs"
description: "Separates audio tracks into individual stems (vocals, drums, bass, other) using Meta's Demucs neural network model via the demucs Python package. Supports batch processing of WAV and MP3 files, outputs isolated stems in FLAC or WAV format, and integrates with FFmpeg for format conversion and loudness matching post-separation."
github_stars: 2507
verification: "security_reviewed"
source: "https://github.com/adefossez/demucs"
author: "adefossez"
category: "Media & Transcription"
framework: "MCP"
tool_ecosystem:
  github_repo: "adefossez/demucs"
  github_stars: 2507
---

# Audio Stem Separator with Demucs

Separates audio tracks into individual stems (vocals, drums, bass, other) using Meta's Demucs neural network model via the demucs Python package. Supports batch processing of WAV and MP3 files, outputs isolated stems in FLAC or WAV format, and integrates with FFmpeg for format conversion and loudness matching post-separation.

## Installation

Use the upstream install or setup path that matches your environment:
- conda env update -f environment-cpu.yml # if you don't have GPUs
- conda env update -f environment-cuda.yml # if you have GPUs
- conda activate demucs
- pip install -e .

Requirements and caveats from upstream:
- requires custom CUDA code that is not ready for release yet.
- You will need at least Python 3.8. See requirements_minimal.txt for requirements for separation only,
- Everytime you see python3, replace it with python.exe. You should always run commands from the

Basic usage or getting-started notes:
- and environment-[cpu|cuda].yml (or requirements.txt) if you want to train a new model.
- ### For Windows users
- Anaconda console.

- Source: https://github.com/adefossez/demucs
- Extracted from upstream docs: https://raw.githubusercontent.com/adefossez/demucs/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audio-stem-separator-demucs/)
