---
title: "Audio Stem Separator with Demucs"
description: "Audio Stem Separator with Demucs provides production-quality audio source separation by running Meta&#8217;s Demucs hybrid transformer model. It accepts WAV, MP3, FLAC, and other common audio formats, converting them through FFmpeg to the 44.1kHz WAV input required by the demucs Python package&#8217;s separate function. The skill supports multiple Demucs model variants: htdemucs for the best general-purpose separation quality, htdemucs_ft for the fine-tuned variant with improved vocal isolation, and mdx_extra for legacy compatibility. Batch processing handles entire directories with configurable parallelism, automatically managing GPU memory allocation when CUDA is available and falling back to CPU processing on machines without discrete GPUs. Post-separation, each stem (vocals, drums, bass, other) goes through an FFmpeg loudness normalization stage using the loudnorm filter to match EBU R128 targets, ensuring consistent playback levels across separated stems. Output supports WAV for lossless quality, FLAC for compressed lossless archival, and MP3 for distribution. The tool generates a JSON manifest documenting source file metadata, model used, processing time, and output file paths for integration with DAW import workflows and downstream audio processing pipelines."
source: "https://github.com/adefossez/demucs"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "adefossez/demucs"
  github_stars: 2507
---

# Audio Stem Separator with Demucs

Audio Stem Separator with Demucs provides production-quality audio source separation by running Meta&#8217;s Demucs hybrid transformer model. It accepts WAV, MP3, FLAC, and other common audio formats, converting them through FFmpeg to the 44.1kHz WAV input required by the demucs Python package&#8217;s separate function. The skill supports multiple Demucs model variants: htdemucs for the best general-purpose separation quality, htdemucs_ft for the fine-tuned variant with improved vocal isolation, and mdx_extra for legacy compatibility. Batch processing handles entire directories with configurable parallelism, automatically managing GPU memory allocation when CUDA is available and falling back to CPU processing on machines without discrete GPUs. Post-separation, each stem (vocals, drums, bass, other) goes through an FFmpeg loudness normalization stage using the loudnorm filter to match EBU R128 targets, ensuring consistent playback levels across separated stems. Output supports WAV for lossless quality, FLAC for compressed lossless archival, and MP3 for distribution. The tool generates a JSON manifest documenting source file metadata, model used, processing time, and output file paths for integration with DAW import workflows and downstream audio processing pipelines.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audio-stem-separator-demucs/)
