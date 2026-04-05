---
name: "pyannote.audio Neural Speaker Diarization Toolkit"
description: "pyannote.audio is an open-source Python toolkit for speaker diarization built on PyTorch. It provides state-of-the-art pretrained models and pipelines for speech activity detection, speaker segmentation, overlapped speech detection, and speaker embedding."
category: "Media &amp; Transcription"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/pyannote/pyannote-audio"
---
# pyannote.audio Neural Speaker Diarization Toolkit

pyannote.audio is an open-source Python toolkit for speaker diarization built on PyTorch. It provides state-of-the-art pretrained models and pipelines for speech activity detection, speaker segmentation, overlapped speech detection, and speaker embedding.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pyannote-audio-speaker-diarization-toolkit
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pyannote-audio-speaker-diarization-toolkit -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pyannote-audio-speaker-diarization-toolkit -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pyannote-audio-speaker-diarization-toolkit -a codex
```

### OpenClaw

```bash
clawhub install pyannote-audio-speaker-diarization-toolkit
```

## Details

pyannote.audio is a leading open-source toolkit for speaker diarization written in Python and built on the PyTorch machine learning framework. Developed and maintained by Hervé Bredin and the pyannote team, it provides state-of-the-art pretrained models and pipelines that can identify who speaks when in an audio recording. The library supports both local inference via community models and premium cloud-based diarization through the pyannoteAI service.

Speaker Diarization Pipeline
The core use case is speaker diarization — automatically segmenting audio into speaker turns. Using Pipeline.from_pretrained("pyannote/speaker-diarization-community-1"), you load the latest community pipeline that runs entirely locally. The pipeline accepts audio files and returns timestamped speaker labels, enabling transcription services to attribute text to specific speakers. GPU acceleration is supported via CUDA for real-time processing.

Neural Building Blocks
Beyond the end-to-end pipeline, pyannote.audio exposes individual neural building blocks: voice activity detection (VAD), speaker change detection, overlapped speech detection, and speaker embedding extraction. These components can be used independently or composed into custom pipelines. Each model is available as a pretrained checkpoint on Hugging Face Hub.

Training and Fine-tuning
The toolkit supports multi-GPU training via pytorch-lightning, allowing you to fine-tune models on your own data for domain-specific performance improvements. This is critical for specialized domains like medical consultations, call center analytics, or meeting transcription where acoustic conditions differ from training data.

Benchmark Performance
pyannote.audio achieves competitive diarization error rates across standard benchmarks including AMI, DIHARD 3, VoxConverse, CALLHOME, and AISHELL-4. The community-1 pipeline consistently outperforms the legacy 3.1 pipeline, with the premium precision-2 service achieving the best results.

Installation and Dependencies
Install with pip install pyannote.audio or uv add pyannote.audio. The library requires ffmpeg for audio decoding via torchcodec. Access to pretrained models requires accepting user conditions on Hugging Face and providing an access token. The package is available on PyPI and supports Python 3.8+.

Agent Integration
For AI agents processing audio content — podcast transcription, meeting notes, interview analysis — pyannote.audio provides the speaker attribution layer. Combined with Whisper or other speech-to-text engines, it enables labeled transcripts that identify each speaker, making downstream summarization and analysis significantly more useful.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pyannote-audio-speaker-diarization-toolkit/)
