---
title: Silero VAD Pre-Trained Enterprise Voice Activity Detection
description: Silero VAD is a pre-trained, enterprise-grade Voice Activity Detector
  developed by the Silero team. It detects speech segments in audio with high accuracy,
  running efficiently on CPU with minimal memory footprint. The model supports both
  PyTorch and ONNX Runtime backends, enabling deployment on embedded systems, mobile
  devices, and servers alike. Core Capabilities Silero VAD processes audio at 16kHz
  or 8kHz sampling rates and returns precise speech timestamps. It excels at distinguishing
  speech from background noise, music, and other non-speech audio. The detector runs
  in real-time with sub-millisecond latency per audio chunk, requiring only 1GB of
  RAM and a modern CPU with AVX instruction support. How It Works Install via pip
  install silero-vad and load the model with a single function call. Feed audio data
  in chunks and receive speech probability scores or timestamp ranges. The library
  provides utility functions for reading audio files, extracting speech segments,
  and saving results. Integration through torch.hub is also supported for zero-dependency
  setups. Agent Integration AI agents use Silero VAD as a preprocessing step in audio
  intelligence pipelines. Before running expensive transcription with Whisper or speaker
  diarization, VAD identifies which portions of audio contain speech, reducing processing
  time and cost. It is the default VAD used by WhisperX, faster-whisper, and many
  real-time transcription systems. The model runs entirely offline with no API calls
  required. Key Features Enterprise-grade accuracy with sub-millisecond latency PyTorch
  and ONNX Runtime backends Supports 16kHz and 8kHz audio Real-time streaming and
  batch processing Minimal dependencies (torch or onnxruntime) MIT license, free for
  commercial use Used as default VAD in WhisperX and faster-whisper
verification: security_reviewed
source: https://github.com/snakers4/silero-vad
category:
- Media &amp; Transcription
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: snakers4/silero-vad
  github_stars: 8604
---

# Silero VAD Pre-Trained Enterprise Voice Activity Detection

Silero VAD is a pre-trained, enterprise-grade Voice Activity Detector developed by the Silero team. It detects speech segments in audio with high accuracy, running efficiently on CPU with minimal memory footprint. The model supports both PyTorch and ONNX Runtime backends, enabling deployment on embedded systems, mobile devices, and servers alike. Core Capabilities Silero VAD processes audio at 16kHz or 8kHz sampling rates and returns precise speech timestamps. It excels at distinguishing speech from background noise, music, and other non-speech audio. The detector runs in real-time with sub-millisecond latency per audio chunk, requiring only 1GB of RAM and a modern CPU with AVX instruction support. How It Works Install via pip install silero-vad and load the model with a single function call. Feed audio data in chunks and receive speech probability scores or timestamp ranges. The library provides utility functions for reading audio files, extracting speech segments, and saving results. Integration through torch.hub is also supported for zero-dependency setups. Agent Integration AI agents use Silero VAD as a preprocessing step in audio intelligence pipelines. Before running expensive transcription with Whisper or speaker diarization, VAD identifies which portions of audio contain speech, reducing processing time and cost. It is the default VAD used by WhisperX, faster-whisper, and many real-time transcription systems. The model runs entirely offline with no API calls required. Key Features Enterprise-grade accuracy with sub-millisecond latency PyTorch and ONNX Runtime backends Supports 16kHz and 8kHz audio Real-time streaming and batch processing Minimal dependencies (torch or onnxruntime) MIT license, free for commercial use Used as default VAD in WhisperX and faster-whisper

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/silero-vad-voice-activity-detection/)
