---
name: "whisper.cpp High-Performance C/C++ Speech Recognition Engine"
description: "whisper.cpp is a lightweight, high-performance C/C++ port of OpenAI’s Whisper automatic speech recognition model. It runs on CPU and GPU across all major platforms with zero dependencies and zero runtime memory allocations."
category: "Media &amp; Transcription"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/ggml-org/whisper.cpp"
tool_ecosystem:
  github_repo: "ggml-org/whisper.cpp"
  github_stars: 48315
---
# whisper.cpp High-Performance C/C++ Speech Recognition Engine

whisper.cpp is a lightweight, high-performance C/C++ port of OpenAI’s Whisper automatic speech recognition model. It runs on CPU and GPU across all major platforms with zero dependencies and zero runtime memory allocations.

whisper.cpp is a portable C/C++ implementation of OpenAI’s Whisper speech recognition model, maintained by the ggml-org team. With over 48,000 GitHub stars, it is the leading native implementation for on-device speech-to-text, supporting macOS, iOS, Android, Linux, Windows, WebAssembly, and Raspberry Pi.

Architecture and Performance The implementation is pure C/C++ with no external dependencies. It uses ARM NEON and Apple Accelerate on ARM platforms, AVX/AVX2 intrinsics on x86, and supports GPU acceleration through Apple Metal, NVIDIA CUDA, Vulkan, and OpenVINO. Mixed F16/F32 precision and integer quantization (Q4, Q5, Q8) reduce memory usage while maintaining accuracy. The engine achieves zero runtime memory allocations for predictable performance.

Voice Activity Detection whisper.cpp includes built-in Voice Activity Detection (VAD) that segments audio into speech regions before transcription. This reduces processing time on files with significant silence and improves accuracy by filtering noise. VAD can be configured independently and is available through both CLI and API.

CLI Usage The primary interface is whisper-cli, which transcribes audio files to text with timestamp output. Build with CMake (cmake -B build && cmake --build build) and run: ./build/bin/whisper-cli -f audio.wav. Input must be 16-bit WAV at 16kHz; use ffmpeg to convert: ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav. Output formats include plain text, SRT subtitles, VTT, CSV, and JSON.

Server Mode The built-in HTTP server (whisper-server) provides a REST API compatible with the OpenAI Audio Transcriptions endpoint. This allows applications that use the OpenAI Whisper API to switch to local inference by changing only the base URL. The server supports concurrent requests and streaming output.

Language Bindings Official and community bindings exist for Python, Ruby, Java, Go, and Node.js (available as whisper.cpp on npm). The C-style API in whisper.h makes integration straightforward for any language with FFI support.

Models Pre-converted GGML format models are available via the included download script: sh ./models/download-ggml-model.sh base.en. Models range from tiny (39M parameters) to large-v3 (1.5B parameters), with English-only variants for improved speed on English content.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill whisper-cpp-speech-recognition-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill whisper-cpp-speech-recognition-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill whisper-cpp-speech-recognition-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill whisper-cpp-speech-recognition-engine -a codex
```

### OpenClaw

```bash
clawhub install whisper-cpp-speech-recognition-engine
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-cpp-speech-recognition-engine/)
