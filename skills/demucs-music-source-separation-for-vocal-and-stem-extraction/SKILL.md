---
title: "Demucs Music Source Separation for Vocal and Stem Extraction"
description: "Demucs is Meta’s open-source music source separation project for splitting songs into stems such as vocals, drums, bass, and accompaniment. It fits agent workflows that need repeatable audio preprocessing before transcription, remixing, analysis, captioning, or archive preparation."
verification: "security_reviewed"
source: "https://github.com/facebookresearch/demucs"
category:
  - "Media & Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "facebookresearch/demucs"
  github_stars: 9949
---

# Demucs Music Source Separation for Vocal and Stem Extraction

Demucs is a widely used open-source music source separation project from Meta Research. It provides pretrained models and a Python package that can split a full song into separate audio stems such as vocals, drums, bass, and other accompaniment. The repository documents both command-line usage and research context, and it links to sample outputs and papers describing the Hybrid Transformer Demucs architecture. For agentic workflows, Demucs is valuable as an audio preparation step. An assistant can isolate vocals before speech-to-text, remove backing tracks for lyric review, create karaoke-style instrumental versions, or prepare cleaner source material for archival and editing pipelines. Because it is tool-driven rather than SaaS-only, it can be integrated into local media workflows, batch processing systems, or custom Python automations that already use PyTorch and torchaudio. The upstream README documents installation with python3 -m pip install -U demucs and explains practical execution details, including audio format support through torchaudio and FFmpeg fallback notes on Windows. Even though the repository explicitly notes limited maintenance, it remains a real and heavily adopted upstream project with substantial community usage and research relevance. That makes it a strong fit for media-processing skill discovery where the job to be done is clear: split mixed music into usable stems for downstream automation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/demucs-music-source-separation-for-vocal-and-stem-extraction/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/demucs-music-source-separation-for-vocal-and-stem-extraction
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/demucs-music-source-separation-for-vocal-and-stem-extraction`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/demucs-music-source-separation-for-vocal-and-stem-extraction/)
