---
title: Audio Stem Separator with Demucs
description: 'Audio Stem Separator with Demucs provides production-quality audio source
  separation by running Meta’s Demucs hybrid transformer model. It accepts WAV, MP3,
  FLAC, and other common audio formats, converting them through FFmpeg to the 44.1kHz
  WAV input required by the demucs Python package’s separate function. The skill supports
  multiple Demucs model variants: htdemucs for the best general-purpose separation
  quality, htdemucs_ft for the fine-tuned variant with improved vocal isolation, and
  mdx_extra for legacy compatibility. Batch processing handles entire directories
  with configurable parallelism, automatically managing GPU memory allocation when
  CUDA is available and falling back to CPU processing on machines without discrete
  GPUs. Post-separation, each stem (vocals, drums, bass, other) goes through an FFmpeg
  loudness normalization stage using the loudnorm filter to match EBU R128 targets,
  ensuring consistent playback levels across separated stems. Output supports WAV
  for lossless quality, FLAC for compressed lossless archival, and MP3 for distribution.
  The tool generates a JSON manifest documenting source file metadata, model used,
  processing time, and output file paths for integration with DAW import workflows
  and downstream audio processing pipelines.'
verification: security_reviewed
source: https://github.com/adefossez/demucs
category:
- Media &amp; Transcription
framework:
- MCP
tool_ecosystem:
  github_repo: adefossez/demucs
  github_stars: 2507
---

# Audio Stem Separator with Demucs

Audio Stem Separator with Demucs provides production-quality audio source separation by running Meta’s Demucs hybrid transformer model. It accepts WAV, MP3, FLAC, and other common audio formats, converting them through FFmpeg to the 44.1kHz WAV input required by the demucs Python package’s separate function. The skill supports multiple Demucs model variants: htdemucs for the best general-purpose separation quality, htdemucs_ft for the fine-tuned variant with improved vocal isolation, and mdx_extra for legacy compatibility. Batch processing handles entire directories with configurable parallelism, automatically managing GPU memory allocation when CUDA is available and falling back to CPU processing on machines without discrete GPUs. Post-separation, each stem (vocals, drums, bass, other) goes through an FFmpeg loudness normalization stage using the loudnorm filter to match EBU R128 targets, ensuring consistent playback levels across separated stems. Output supports WAV for lossless quality, FLAC for compressed lossless archival, and MP3 for distribution. The tool generates a JSON manifest documenting source file metadata, model used, processing time, and output file paths for integration with DAW import workflows and downstream audio processing pipelines.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audio-stem-separator-demucs/)
