---
title: "audioFlux Audio and Music Analysis Feature Extraction Library"
description: "audioFlux is a deep learning tool library for audio and music analysis and feature extraction, supporting dozens of time-frequency transforms and hundreds of feature combinations for classification, separation, MIR, and ASR tasks."
slug: "audioflux-audio-music-analysis-feature-extraction-library"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/libAudioFlux/audioFlux"
---

# audioFlux Audio and Music Analysis Feature Extraction Library

audioFlux is a deep learning tool library for audio and music analysis and feature extraction, supporting dozens of time-frequency transforms and hundreds of feature combinations for classification, separation, MIR, and ASR tasks.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install audioflux-audio-music-analysis-feature-extraction-library
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

audioFlux is a high-performance library for audio and music analysis, designed as a feature extraction pipeline for deep learning workflows. Written in C with Python bindings (available on PyPI), it provides dozens of time-frequency analysis transformation methods and hundreds of corresponding time-domain and frequency-domain feature combinations.
Transform Methods
audioFlux implements multiple transform algorithms: BFT (Based Fourier Transform, similar to STFT), NSGT (Non-Stationary Gabor Transform), CWT (Continuous Wavelet Transform), and PWT (Pseudo Wavelet Transform). Each transform supports multiple frequency scale types including Linear (STFT spectrogram), Linspace, Mel, Bark, Erb, and Octave scales. This gives researchers and engineers granular control over spectral representation.
Feature Extraction
The library extracts spectral features (centroid, bandwidth, flatness, rolloff), chroma features, MFCC, onset detection, and pitch tracking. Pitch algorithms include YIN, CEP, PEF, NCF, HPS, LHS, STFT, and FFP. Version 0.1.8 added PitchShift and TimeStretch algorithms. Version 0.1.10 introduced TuneTrack for instrument tuning across guitar, ukulele, bass, banjo, mandolin, and violin.
Integration
audioFlux follows a data stream architecture that decouples algorithm modules for fast, efficient multi-dimensional feature extraction. Features can be fed into deep learning networks (PyTorch, TensorFlow) for tasks like audio classification, source separation, Music Information Retrieval, and Automatic Speech Recognition. Install via pip install audioflux. The library is licensed under MIT and documentation is available at audioflux.top.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audioflux-audio-music-analysis-feature-extraction-library/)
