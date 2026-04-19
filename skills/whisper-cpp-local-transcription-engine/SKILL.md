---
title: "Whisper.cpp Local Transcription Engine"
description: "This skill provides fully local speech-to-text transcription using whisper.cpp, the C/C++ port of OpenAI&#8217;s Whisper model. It downloads GGML-quantized model weights (tiny, base, small, medium, large-v3) and runs inference on CPU with optional GPU acceleration via CUDA or Metal backends. The core command runs: ./main -m models/ggml-large-v3.bin -f input.wav -osrt -ocsv &#8211;beam-size 5 &#8211;best-of 5. The skill handles audio preprocessing by converting input files to 16kHz mono WAV using FFmpeg: ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav. It supports multiple output formats: plain text (-otxt), SRT subtitles (-osrt), VTT subtitles (-ovtt), CSV with timestamps (-ocsv), and JSON with word-level timing (-ojson). Advanced features include voice activity detection (&#8211;no-speech-thold 0.6) to skip silence, language auto-detection (&#8211;language auto), and translation mode (&#8211;translate) for non-English audio. The skill implements batch processing for multiple files with progress tracking. Performance tuning includes thread count configuration (&#8211;threads N), and the skill benchmarks inference speed as a ratio of audio duration. For long recordings, it uses &#8211;max-len 0 to process without segment length limits."
source: "https://github.com/openai/whisper"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97775
---

# Whisper.cpp Local Transcription Engine

This skill provides fully local speech-to-text transcription using whisper.cpp, the C/C++ port of OpenAI&#8217;s Whisper model. It downloads GGML-quantized model weights (tiny, base, small, medium, large-v3) and runs inference on CPU with optional GPU acceleration via CUDA or Metal backends. The core command runs: ./main -m models/ggml-large-v3.bin -f input.wav -osrt -ocsv &#8211;beam-size 5 &#8211;best-of 5. The skill handles audio preprocessing by converting input files to 16kHz mono WAV using FFmpeg: ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav. It supports multiple output formats: plain text (-otxt), SRT subtitles (-osrt), VTT subtitles (-ovtt), CSV with timestamps (-ocsv), and JSON with word-level timing (-ojson). Advanced features include voice activity detection (&#8211;no-speech-thold 0.6) to skip silence, language auto-detection (&#8211;language auto), and translation mode (&#8211;translate) for non-English audio. The skill implements batch processing for multiple files with progress tracking. Performance tuning includes thread count configuration (&#8211;threads N), and the skill benchmarks inference speed as a ratio of audio duration. For long recordings, it uses &#8211;max-len 0 to process without segment length limits.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-cpp-local-transcription-engine/)
