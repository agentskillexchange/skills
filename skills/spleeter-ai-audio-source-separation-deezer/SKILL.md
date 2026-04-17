---
title: "Spleeter AI Audio Source Separation by Deezer"
description: "Spleeter is an open-source audio source separation library developed by Deezer Research. Written in Python and built on TensorFlow, it provides pretrained models that can split any audio file into individual stems — isolating vocals from instruments, or separating drums, bass, piano, and other elements from a mixed track.\nSeparation Modes\nSpleeter ships with three pretrained separation models: the 2-stems model separates vocals from accompaniment, the 4-stems model isolates vocals, drums, bass, and other instruments, and the 5-stems model adds piano as a separate stem. All models achieve high performance on the musdb benchmark dataset and can process audio 100x faster than real-time when running on GPU hardware.\nCLI and Python API\nThe tool can be used directly from the command line with spleeter separate -i input.mp3 -p spleeter:2stems -o output, or integrated into Python pipelines via its library API. Installation is available through pip (pip install spleeter) or conda (conda install -c conda-forge spleeter). It requires FFmpeg and libsndfile as external dependencies.\nAgent Skill Applications\nAs an agent skill, Spleeter enables automated workflows for music production — extracting vocals for karaoke tracks, isolating drum patterns for remix projects, or analyzing individual instrument parts. Agents can chain Spleeter with transcription tools like Whisper to get cleaner vocal transcriptions, use it for audio quality assessment by examining individual stems, or build automated music analysis pipelines. The tool outputs standard WAV files for each separated stem, making it compatible with downstream audio processing tools.\nTechnical Details\nSpleeter uses U-Net architecture neural networks trained on Deezer’s internal dataset. It operates on Short-Time Fourier Transform (STFT) spectrograms and uses soft masking to produce separated audio. The library is MIT-licensed and has been cited in numerous academic papers on music information retrieval."
verification: security_reviewed
source: "https://github.com/deezer/spleeter"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "deezer/spleeter"
  github_stars: 28130
---

# Spleeter AI Audio Source Separation by Deezer

Spleeter is an open-source audio source separation library developed by Deezer Research. Written in Python and built on TensorFlow, it provides pretrained models that can split any audio file into individual stems — isolating vocals from instruments, or separating drums, bass, piano, and other elements from a mixed track.
Separation Modes
Spleeter ships with three pretrained separation models: the 2-stems model separates vocals from accompaniment, the 4-stems model isolates vocals, drums, bass, and other instruments, and the 5-stems model adds piano as a separate stem. All models achieve high performance on the musdb benchmark dataset and can process audio 100x faster than real-time when running on GPU hardware.
CLI and Python API
The tool can be used directly from the command line with spleeter separate -i input.mp3 -p spleeter:2stems -o output, or integrated into Python pipelines via its library API. Installation is available through pip (pip install spleeter) or conda (conda install -c conda-forge spleeter). It requires FFmpeg and libsndfile as external dependencies.
Agent Skill Applications
As an agent skill, Spleeter enables automated workflows for music production — extracting vocals for karaoke tracks, isolating drum patterns for remix projects, or analyzing individual instrument parts. Agents can chain Spleeter with transcription tools like Whisper to get cleaner vocal transcriptions, use it for audio quality assessment by examining individual stems, or build automated music analysis pipelines. The tool outputs standard WAV files for each separated stem, making it compatible with downstream audio processing tools.
Technical Details
Spleeter uses U-Net architecture neural networks trained on Deezer’s internal dataset. It operates on Short-Time Fourier Transform (STFT) spectrograms and uses soft masking to produce separated audio. The library is MIT-licensed and has been cited in numerous academic papers on music information retrieval.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/spleeter-ai-audio-source-separation-deezer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/spleeter-ai-audio-source-separation-deezer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/spleeter-ai-audio-source-separation-deezer/)
