---
name: "audioFlux Audio and Music Analysis Feature Extraction Library"
description: "audioFlux is a deep learning tool library for audio and music analysis and feature extraction, supporting dozens of time-frequency transforms and hundreds of feature combinations for classification, separation, MIR, and ASR tasks."
category: "Media & Transcription"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/libAudioFlux/audioFlux"
---
# audioFlux Audio and Music Analysis Feature Extraction Library

audioFlux is a deep learning tool library for audio and music analysis and feature extraction, supporting dozens of time-frequency transforms and hundreds of feature combinations for classification, separation, MIR, and ASR tasks.

## Overview

audioFlux is a high-performance library for audio and music analysis, designed as a feature extraction pipeline for deep learning workflows. Written in C with Python bindings (available on PyPI), it provides dozens of time-frequency analysis transformation methods and hundreds of corresponding time-domain and frequency-domain feature combinations.

Transform Methods

audioFlux implements multiple transform algorithms: BFT (Based Fourier Transform, similar to STFT), NSGT (Non-Stationary Gabor Transform), CWT (Continuous Wavelet Transform), and PWT (Pseudo Wavelet Transform). Each transform supports multiple frequency scale types including Linear (STFT spectrogram), Linspace, Mel, Bark, Erb, and Octave scales. This gives researchers and engineers granular control over spectral representation.

Feature Extraction

The library extracts spectral features (centroid, bandwidth, flatness, rolloff), chroma features, MFCC, onset detection, and pitch tracking. Pitch algorithms include YIN, CEP, PEF, NCF, HPS, LHS, STFT, and FFP. Version 0.1.8 added PitchShift and TimeStretch algorithms. Version 0.1.10 introduced TuneTrack for instrument tuning across guitar, ukulele, bass, banjo, mandolin, and violin.

Integration

audioFlux follows a data stream architecture that decouples algorithm modules for fast, efficient multi-dimensional feature extraction. Features can be fed into deep learning networks (PyTorch, TensorFlow) for tasks like audio classification, source separation, Music Information Retrieval, and Automatic Speech Recognition. Install via `pip install audioflux`. The library is licensed under MIT and documentation is available at audioflux.top.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill audioflux-audio-music-analysis-feature-extraction-library
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill audioflux-audio-music-analysis-feature-extraction-library -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill audioflux-audio-music-analysis-feature-extraction-library -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill audioflux-audio-music-analysis-feature-extraction-library -a codex
```

### OpenClaw

```bash
clawhub install audioflux-audio-music-analysis-feature-extraction-library
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audioflux-audio-music-analysis-feature-extraction-library/)
