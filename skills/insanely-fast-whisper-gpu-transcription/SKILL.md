---
name: "Insanely Fast Whisper GPU-Accelerated Speech Transcription CLI"
slug: "insanely-fast-whisper-gpu-transcription"
description: "Insanely Fast Whisper is a CLI tool that transcribes audio at extreme speeds using OpenAI Whisper models with Hugging Face Transformers, Flash Attention 2, and batched inference. It can transcribe 150 minutes of audio in under 98 seconds on a GPU."
github_stars: 12204
verification: "security_reviewed"
source: "https://github.com/Vaibhavs10/insanely-fast-whisper"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "vaibhavs10/insanely-fast-whisper"
  github_stars: 12204
---

# Insanely Fast Whisper GPU-Accelerated Speech Transcription CLI

Insanely Fast Whisper is a CLI tool that transcribes audio at extreme speeds using OpenAI Whisper models with Hugging Face Transformers, Flash Attention 2, and batched inference. It can transcribe 150 minutes of audio in under 98 seconds on a GPU.

## Installation

Use the upstream install or setup path that matches your environment:
- pipx install insanely-fast-whisper==0.0.15 --force
- pipx install insanely-fast-whisper
- pipx install insanely-fast-whisper --force --pip-args="--ignore-requires-python"
- Don't want to install insanely-fast-whisper? Just use pipx run:

Requirements and caveats from upstream:
- ⚠️ If you have python 3.11.XX installed, pipx may parse the version incorrectly and install a very old version of insanely-fast-whisper without telling you (version 0.0.8, which won't work anymore with the current Bet...
- If you're installing with pip, you can pass the argument directly: pip install insanely-fast-whisper --ignore-requires-python.

Basic usage or getting-started notes:
- bash
- Run inference from any path on your computer:
- insanely-fast-whisper --file-name <filename or URL>

- Source: https://github.com/Vaibhavs10/insanely-fast-whisper
- Extracted from upstream docs: https://raw.githubusercontent.com/Vaibhavs10/insanely-fast-whisper/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/insanely-fast-whisper-gpu-transcription/)
