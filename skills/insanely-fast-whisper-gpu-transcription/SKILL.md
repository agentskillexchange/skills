---
name: "Insanely Fast Whisper GPU-Accelerated Speech Transcription CLI"
description: "Insanely Fast Whisper is a CLI tool that transcribes audio at extreme speeds using OpenAI Whisper models with Hugging Face Transformers, Flash Attention 2, and batched inference. It can transcribe 150 minutes of audio in under 98 seconds on a GPU."
category: "Media &amp; Transcription"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/Vaibhavs10/insanely-fast-whisper"
tool_ecosystem:
  github_repo: "vaibhavs10/insanely-fast-whisper"
  github_stars: 12204
  license: "Apache-2.0"
---
# Insanely Fast Whisper GPU-Accelerated Speech Transcription CLI

Insanely Fast Whisper is a CLI tool that transcribes audio at extreme speeds using OpenAI Whisper models with Hugging Face Transformers, Flash Attention 2, and batched inference. It can transcribe 150 minutes of audio in under 98 seconds on a GPU.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill insanely-fast-whisper-gpu-transcription
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill insanely-fast-whisper-gpu-transcription -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill insanely-fast-whisper-gpu-transcription -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill insanely-fast-whisper-gpu-transcription -a codex
```

### OpenClaw

```bash
clawhub install insanely-fast-whisper-gpu-transcription
```

## Details

Insanely Fast Whisper is an opinionated command-line interface for ultra-fast on-device audio transcription powered by OpenAI’s Whisper models. Built on top of Hugging Face Transformers, Optimum, and Flash Attention, it achieves transcription speeds that are dramatically faster than standard Whisper implementations.

How It Works
The tool leverages several optimization techniques to maximize transcription throughput: batched inference processes multiple audio chunks simultaneously, BetterTransformer and Flash Attention 2 accelerate the model’s attention computation, and fp16 precision reduces memory usage while maintaining accuracy. On an NVIDIA A100 GPU, it can transcribe 150 minutes of audio in under 98 seconds with the large-v3 model.

Key Capabilities

Multiple model support: Works with all Whisper model sizes (tiny through large-v3) and distil-whisper variants for even faster processing.
Flash Attention 2: Enable with --flash True for maximum GPU throughput on supported hardware.
Configurable batching: Adjust batch size with --batch-size to optimize for available GPU memory.
Multiple output formats: Generates transcripts with timestamps suitable for subtitles, captions, and text processing.
URL input support: Accepts both local files and URLs as input, downloading audio automatically.
Mac MPS support: Works on Apple Silicon Macs via the --device-id mps flag.
Distil-Whisper integration: Use distilled models for even faster transcription with minimal quality loss.

Integration Points
Install via pipx install insanely-fast-whisper or run without installing using pipx run insanely-fast-whisper. The tool fits into audio processing pipelines, podcast transcription workflows, subtitle generation systems, and any scenario requiring fast batch transcription. It supports NVIDIA GPUs via CUDA and Apple Silicon via MPS. Combine with downstream tools for speaker diarization, translation, or text analysis.

Example Usage
insanely-fast-whisper --file-name recording.mp3 --flash True --batch-size 24
This transcribes the audio file using Flash Attention 2 with a batch size of 24 for maximum throughput.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/insanely-fast-whisper-gpu-transcription/)
