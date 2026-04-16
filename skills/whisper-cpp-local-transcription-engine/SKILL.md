---
title: "Whisper.cpp Local Transcription Engine"
description: "Runs OpenAI Whisper models locally via whisper.cpp with GGML quantized weights for CPU-efficient transcription. Supports beam search decoding, VAD-based segmentation, and SRT/VTT subtitle output formats."
verification: "security_reviewed"
source: "https://github.com/openai/whisper"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97775
  license: "MIT"
---

# Whisper.cpp Local Transcription Engine

This skill provides fully local speech-to-text transcription using whisper.cpp, the C/C++ port of OpenAI’s Whisper model. It downloads GGML-quantized model weights (tiny, base, small, medium, large-v3) and runs inference on CPU with optional GPU acceleration via CUDA or Metal backends. The core command runs: ./main -m models/ggml-large-v3.bin -f input.wav -osrt -ocsv –beam-size 5 –best-of 5. The skill handles audio preprocessing by converting input files to 16kHz mono WAV using FFmpeg: ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav. It supports multiple output formats: plain text (-otxt), SRT subtitles (-osrt), VTT subtitles (-ovtt), CSV with timestamps (-ocsv), and JSON with word-level timing (-ojson). Advanced features include voice activity detection (–no-speech-thold 0.6) to skip silence, language auto-detection (–language auto), and translation mode (–translate) for non-English audio. The skill implements batch processing for multiple files with progress tracking. Performance tuning includes thread count configuration (–threads N), and the skill benchmarks inference speed as a ratio of audio duration. For long recordings, it uses –max-len 0 to process without segment length limits.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-cpp-local-transcription-engine/)
