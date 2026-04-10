---
title: "librosa Python Audio and Music Analysis Library"
description: "librosa is a Python library for audio and music analysis. It provides tools for feature extraction, spectral analysis, beat tracking, onset detection, and audio visualization, built on top of NumPy and SciPy for scientific audio computing."
slug: "librosa-python-audio-music-analysis-library"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/librosa/librosa"
tool_ecosystem:
  github_repo: "librosa/librosa"
  github_stars: 8294
listed: true
---

# librosa Python Audio and Music Analysis Library

librosa is a Python library for audio and music analysis. It provides tools for feature extraction, spectral analysis, beat tracking, onset detection, and audio visualization, built on top of NumPy and SciPy for scientific audio computing.

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
clawhub install librosa-python-audio-music-analysis-library
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

librosa is an open-source Python library developed by Brian McFee and the librosa development team for analyzing and extracting features from audio signals. It is the standard Python library for music information retrieval (MIR) and audio analysis, widely used in academic research, machine learning pipelines, and production audio systems.
The library provides a comprehensive set of audio analysis tools organized into several modules. The core module handles audio loading and resampling from any format via soundfile/audioread. The feature module extracts spectral features including MFCCs (Mel-frequency cepstral coefficients), chroma features, spectral contrast, tonnetz, and mel spectrograms. The beat module performs tempo estimation and beat tracking. The onset module detects note onsets and transients. The effects module provides time-stretching, pitch-shifting, and harmonic-percussive source separation.
librosa also includes tools for audio visualization via its display module, which generates waveform plots, spectrograms, chromagrams, and other visual representations using matplotlib. The decompose module provides non-negative matrix factorization and other decomposition methods for audio analysis. The segment module handles structural analysis and self-similarity computation.
Installed via pip install librosa, the library requires NumPy, SciPy, scikit-learn, and soundfile as dependencies. Documentation is available at librosa.org/doc/latest/ with extensive examples and tutorials. With 8,200+ GitHub stars, 1,000+ forks, and ISC license, librosa is a mature and actively maintained project. AI agents can use librosa for audio classification tasks, music genre detection, audio fingerprinting, speech analysis, podcast content analysis, audio quality assessment, and building training data pipelines for audio machine learning models.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/librosa-python-audio-music-analysis-library/)
