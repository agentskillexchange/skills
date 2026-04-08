---
title: Whisper.cpp Local Transcription Engine
description: 'This skill provides fully local speech-to-text transcription using whisper.cpp,
  the C/C++ port of OpenAI’s Whisper model. It downloads GGML-quantized model weights
  (tiny, base, small, medium, large-v3) and runs inference on CPU with optional GPU
  acceleration via CUDA or Metal backends. The core command runs: ./main -m models/ggml-large-v3.bin
  -f input.wav -osrt -ocsv –beam-size 5 –best-of 5. The skill handles audio preprocessing
  by converting input files to 16kHz mono WAV using FFmpeg: ffmpeg -i input.mp3 -ar
  16000 -ac 1 -c:a pcm_s16le output.wav. It supports multiple output formats: plain
  text (-otxt), SRT subtitles (-osrt), VTT subtitles (-ovtt), CSV with timestamps
  (-ocsv), and JSON with word-level timing (-ojson). Advanced features include voice
  activity detection (–no-speech-thold 0.6) to skip silence, language auto-detection
  (–language auto), and translation mode (–translate) for non-English audio. The skill
  implements batch processing for multiple files with progress tracking. Performance
  tuning includes thread count configuration (–threads N), and the skill benchmarks
  inference speed as a ratio of audio duration. For long recordings, it uses –max-len
  0 to process without segment length limits.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/whisper-cpp-local-transcription-engine/
category:
- Media &amp; Transcription
framework:
- Claude Code
---

# Whisper.cpp Local Transcription Engine

This skill provides fully local speech-to-text transcription using whisper.cpp, the C/C++ port of OpenAI’s Whisper model. It downloads GGML-quantized model weights (tiny, base, small, medium, large-v3) and runs inference on CPU with optional GPU acceleration via CUDA or Metal backends. The core command runs: ./main -m models/ggml-large-v3.bin -f input.wav -osrt -ocsv –beam-size 5 –best-of 5. The skill handles audio preprocessing by converting input files to 16kHz mono WAV using FFmpeg: ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav. It supports multiple output formats: plain text (-otxt), SRT subtitles (-osrt), VTT subtitles (-ovtt), CSV with timestamps (-ocsv), and JSON with word-level timing (-ojson). Advanced features include voice activity detection (–no-speech-thold 0.6) to skip silence, language auto-detection (–language auto), and translation mode (–translate) for non-English audio. The skill implements batch processing for multiple files with progress tracking. Performance tuning includes thread count configuration (–threads N), and the skill benchmarks inference speed as a ratio of audio duration. For long recordings, it uses –max-len 0 to process without segment length limits.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-cpp-local-transcription-engine/)
