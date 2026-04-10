---
name: "librosa Python Audio and Music Analysis Library"
description: "librosa is a Python library for audio and music analysis. It provides tools for feature extraction, spectral analysis, beat tracking, onset detection, and audio visualization, built on top of NumPy and SciPy for scientific audio computing."
verification: security_reviewed
source: "https://github.com/librosa/librosa"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "librosa/librosa"
  github_stars: 8294
---

# librosa Python Audio and Music Analysis Library

librosa is an open-source Python library developed by Brian McFee and the librosa development team for analyzing and extracting features from audio signals. It is the standard Python library for music information retrieval (MIR) and audio analysis, widely used in academic research, machine learning pipelines, and production audio systems.
The library provides a comprehensive set of audio analysis tools organized into several modules. The core module handles audio loading and resampling from any format via soundfile/audioread. The feature module extracts spectral features including MFCCs (Mel-frequency cepstral coefficients), chroma features, spectral contrast, tonnetz, and mel spectrograms. The beat module performs tempo estimation and beat tracking. The onset module detects note onsets and transients. The effects module provides time-stretching, pitch-shifting, and harmonic-percussive source separation.
librosa also includes tools for audio visualization via its display module, which generates waveform plots, spectrograms, chromagrams, and other visual representations using matplotlib. The decompose module provides non-negative matrix factorization and other decomposition methods for audio analysis. The segment module handles structural analysis and self-similarity computation.
Installed via pip install librosa, the library requires NumPy, SciPy, scikit-learn, and soundfile as dependencies. Documentation is available at librosa.org/doc/latest/ with extensive examples and tutorials. With 8,200+ GitHub stars, 1,000+ forks, and ISC license, librosa is a mature and actively maintained project. AI agents can use librosa for audio classification tasks, music genre detection, audio fingerprinting, speech analysis, podcast content analysis, audio quality assessment, and building training data pipelines for audio machine learning models.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/librosa-python-audio-music-analysis-library/)
