---
name: "Whisper.cpp Local Transcription Engine"
slug: "whisper-cpp-local-transcription-engine"
description: "Runs OpenAI Whisper models locally via whisper.cpp with GGML quantized weights for CPU-efficient transcription. Supports beam search decoding, VAD-based segmentation, and SRT/VTT subtitle output formats."
github_stars: 51671
verification: "security_reviewed"
source: "https://github.com/ggml-org/whisper.cpp"
category: "Media & Transcription"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "ggml-org/whisper.cpp"
  github_stars: 51671
---

# Whisper.cpp Local Transcription Engine

Runs OpenAI Whisper models locally via whisper.cpp with GGML quantized weights for CPU-efficient transcription. Supports beam search decoding, VAD-based segmentation, and SRT/VTT subtitle output formats.

## Installation

Use the upstream whisper.cpp build path for local transcription:

```bash
git clone https://github.com/ggml-org/whisper.cpp.git
cd whisper.cpp
sh ./models/download-ggml-model.sh base.en
cmake -B build
cmake --build build -j --config Release
./build/bin/whisper-cli -f samples/jfk.wav
```

For a quick demo, upstream also supports:

```bash
make base.en
```

The `whisper-cli` example currently expects 16-bit WAV input. Convert other audio formats before transcription when needed:

```bash
ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav
./build/bin/whisper-cli -f output.wav
```

Run `./build/bin/whisper-cli -h` for detailed CLI options.

- Source: https://github.com/ggml-org/whisper.cpp
- Extracted from upstream docs: https://raw.githubusercontent.com/ggml-org/whisper.cpp/master/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-cpp-local-transcription-engine/)
