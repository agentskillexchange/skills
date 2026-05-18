---
name: "faster-whisper High-Performance Speech Transcription Library"
slug: "faster-whisper-high-performance-speech-transcription-library"
description: "faster-whisper is SYSTRAN’s high-performance reimplementation of OpenAI Whisper on top of CTranslate2. It is built for transcription pipelines that need lower latency, lower memory usage, optional quantization, and practical Python integration for batch or real-time speech workflows."
github_stars: 22156
verification: "security_reviewed"
source: "https://github.com/SYSTRAN/faster-whisper"
author: "SYSTRAN"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "SYSTRAN/faster-whisper"
  github_stars: 22156
---

# faster-whisper High-Performance Speech Transcription Library

faster-whisper is SYSTRAN’s high-performance reimplementation of OpenAI Whisper on top of CTranslate2. It is built for transcription pipelines that need lower latency, lower memory usage, optional quantization, and practical Python integration for batch or real-time speech workflows.

## Installation

Use the upstream install or setup path that matches your environment:
- #### Use Docker
- pip install nvidia-cublas-cu12 nvidia-cudnn-cu12==9.*
- pip install faster-whisper
- pip install --force-reinstall "faster-whisper @ https://github.com/SYSTRAN/faster-whisper/archive/refs/heads/master.tar.gz"

Requirements and caveats from upstream:
- Python 3.9 or greater
- Unlike openai-whisper, FFmpeg does **not** need to be installed on the system. The audio is decoded with the Python library [PyAV](https://github.com/PyAV-Org/PyAV) which bundles the FFmpeg libraries in its package.
- GPU execution requires the following NVIDIA libraries to be installed:

Basic usage or getting-started notes:
- For reference, here's the time and memory usage that are required to transcribe [**13 minutes**](https://www.youtube.com/watch?v=0u7tTptBo9I) of audio using different implementations:
- | Implementation | Precision | Beam size | Time | VRAM Usage |
- | Implementation | Precision | Beam size | Time | RAM Usage |

- Source: https://github.com/SYSTRAN/faster-whisper
- Extracted from upstream docs: https://raw.githubusercontent.com/SYSTRAN/faster-whisper/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/faster-whisper-high-performance-speech-transcription-library/)
