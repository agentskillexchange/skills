---
title: "Audio Stem Separator with Demucs"
description: "Separates audio tracks into individual stems (vocals, drums, bass, other) using Meta’s Demucs neural network model via the demucs Python package. Supports batch processing of WAV and MP3 files, outputs isolated stems in FLAC or WAV format, and integrates with FFmpeg for format conversion and loudness matching post-separation."
verification: security_reviewed
source: "https://github.com/adefossez/demucs"
category:
  - "Media & Transcription"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "adefossez/demucs"
  github_stars: 2507
---

# Audio Stem Separator with Demucs

Audio Stem Separator with Demucs provides production-quality audio source separation by running Meta’s Demucs hybrid transformer model. It accepts WAV, MP3, FLAC, and other common audio formats, converting them through FFmpeg to the 44.1kHz WAV input required by the demucs Python package’s separate function.

The skill supports multiple Demucs model variants: htdemucs for the best general-purpose separation quality, htdemucs_ft for the fine-tuned variant with improved vocal isolation, and mdx_extra for legacy compatibility. Batch processing handles entire directories with configurable parallelism, automatically managing GPU memory allocation when CUDA is available and falling back to CPU processing on machines without discrete GPUs.

Post-separation, each stem (vocals, drums, bass, other) goes through an FFmpeg loudness normalization stage using the loudnorm filter to match EBU R128 targets, ensuring consistent playback levels across separated stems. Output supports WAV for lossless quality, FLAC for compressed lossless archival, and MP3 for distribution. The tool generates a JSON manifest documenting source file metadata, model used, processing time, and output file paths for integration with DAW import workflows and downstream audio processing pipelines.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/audio-stem-separator-demucs
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/audio-stem-separator-demucs` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audio-stem-separator-demucs/)
