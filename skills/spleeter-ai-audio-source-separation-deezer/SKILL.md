---
title: "Spleeter AI Audio Source Separation by Deezer"
description: "Spleeter is Deezer’s open-source audio source separation library with pretrained models. It can split audio into 2, 4, or 5 stems (vocals, drums, bass, piano, accompaniment) and runs 100x faster than real-time on GPU, making it ideal for music production, remix, and audio analysis workflows."
slug: "spleeter-ai-audio-source-separation-deezer"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/deezer/spleeter"
tool_ecosystem:
  github_repo: "deezer/spleeter"
  github_stars: 28130
---

# Spleeter AI Audio Source Separation by Deezer

Spleeter is Deezer’s open-source audio source separation library with pretrained models. It can split audio into 2, 4, or 5 stems (vocals, drums, bass, piano, accompaniment) and runs 100x faster than real-time on GPU, making it ideal for music production, remix, and audio analysis workflows.

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
clawhub install spleeter-ai-audio-source-separation-deezer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Spleeter is an open-source audio source separation library developed by Deezer Research. Written in Python and built on TensorFlow, it provides pretrained models that can split any audio file into individual stems — isolating vocals from instruments, or separating drums, bass, piano, and other elements from a mixed track.
Separation Modes
Spleeter ships with three pretrained separation models: the 2-stems model separates vocals from accompaniment, the 4-stems model isolates vocals, drums, bass, and other instruments, and the 5-stems model adds piano as a separate stem. All models achieve high performance on the musdb benchmark dataset and can process audio 100x faster than real-time when running on GPU hardware.
CLI and Python API
The tool can be used directly from the command line with spleeter separate -i input.mp3 -p spleeter:2stems -o output, or integrated into Python pipelines via its library API. Installation is available through pip (pip install spleeter) or conda (conda install -c conda-forge spleeter). It requires FFmpeg and libsndfile as external dependencies.
Agent Skill Applications
As an agent skill, Spleeter enables automated workflows for music production — extracting vocals for karaoke tracks, isolating drum patterns for remix projects, or analyzing individual instrument parts. Agents can chain Spleeter with transcription tools like Whisper to get cleaner vocal transcriptions, use it for audio quality assessment by examining individual stems, or build automated music analysis pipelines. The tool outputs standard WAV files for each separated stem, making it compatible with downstream audio processing tools.
Technical Details
Spleeter uses U-Net architecture neural networks trained on Deezer’s internal dataset. It operates on Short-Time Fourier Transform (STFT) spectrograms and uses soft masking to produce separated audio. The library is MIT-licensed and has been cited in numerous academic papers on music information retrieval.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/spleeter-ai-audio-source-separation-deezer/)
