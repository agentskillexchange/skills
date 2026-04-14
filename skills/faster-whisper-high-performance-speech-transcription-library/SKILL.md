---
title: "faster-whisper High-Performance Speech Transcription Library"
description: "faster-whisper is SYSTRAN’s high-performance reimplementation of OpenAI Whisper on top of CTranslate2. It is built for transcription pipelines that need lower latency, lower memory usage, optional quantization, and practical Python integration for batch or real-time speech workflows."
verification: security_reviewed
source: "https://github.com/SYSTRAN/faster-whisper"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "SYSTRAN/faster-whisper"
  github_stars: 22156
---

# faster-whisper High-Performance Speech Transcription Library

faster-whisper is an open source Python library from SYSTRAN that reimplements OpenAI Whisper using CTranslate2 for faster inference. The project is aimed at a clear job-to-be-done: transcribe audio with Whisper-compatible models while reducing runtime and memory requirements compared with baseline implementations. The upstream README documents CPU and GPU benchmarks, quantized execution modes, and practical examples for batch and standard transcription.

This makes it a good fit for media processing agents, podcast and meeting transcription, subtitle generation, speech indexing, and any automation that needs reliable local or server-side speech-to-text. The library supports different compute types, integrates voice activity detection with Silero VAD, and can produce segment or word timestamps. It is especially useful when teams want Whisper-class transcription in a Python workflow without paying an API cost per file.

Integration points are simple. Install the package from PyPI, create a WhisperModel instance, and run transcribe() against local audio files or pipeline inputs. For GPU use, the README specifies CUDA and cuDNN requirements; for CPU-only use, teams can run quantized inference with a smaller footprint. It also pairs well with media ingestion queues, diarization pipelines, subtitle tools, and agent systems that summarize or search spoken content.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/faster-whisper-high-performance-speech-transcription-library/)
