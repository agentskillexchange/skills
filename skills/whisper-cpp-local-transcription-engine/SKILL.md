---
name: "Whisper.cpp Local Transcription Engine"
description: "Runs OpenAI Whisper models locally via whisper.cpp with GGML quantized weights for CPU-efficient transcription. Supports beam search decoding, VAD-based segmentation, and SRT/VTT subtitle output formats."
category: "Media & Transcription"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/whisper-cpp-local-transcription-engine/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "whisper"  # from ase_tool_match
  github_stars: 10761  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/openai-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Whisper.cpp Local Transcription Engine

Runs OpenAI Whisper models locally via whisper.cpp with GGML quantized weights for CPU-efficient transcription. Supports beam search decoding, VAD-based segmentation, and SRT/VTT subtitle output formats.

## Overview

This skill provides fully local speech-to-text transcription using whisper.cpp, the C/C++ port of OpenAI’s Whisper model. It downloads GGML-quantized model weights (tiny, base, small, medium, large-v3) and runs inference on CPU with optional GPU acceleration via CUDA or Metal backends. The core command runs: ./main -m models/ggml-large-v3.bin -f input.wav -osrt -ocsv –beam-size 5 –best-of 5. The skill handles audio preprocessing by converting input files to 16kHz mono WAV using FFmpeg: ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav. It supports multiple output formats: plain text (-otxt), SRT subtitles (-osrt), VTT subtitles (-ovtt), CSV with timestamps (-ocsv), and JSON with word-level timing (-ojson). Advanced features include voice activity detection (–no-speech-thold 0.6) to skip silence, language auto-detection (–language auto), and translation mode (–translate) for non-English audio. The skill implements batch processing for multiple files with progress tracking. Performance tuning includes thread count configuration (–threads N), and the skill benchmarks inference speed as a ratio of audio duration. For long recordings, it uses –max-len 0 to process without segment length limits.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill whisper-cpp-local-transcription-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill whisper-cpp-local-transcription-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill whisper-cpp-local-transcription-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill whisper-cpp-local-transcription-engine -a codex
```

### OpenClaw

```bash
clawhub install whisper-cpp-local-transcription-engine
```

## Source

- Marketplace: https://agentskillexchange.com/skills/whisper-cpp-local-transcription-engine/
