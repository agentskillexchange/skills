---
title: "Demucs Music Source Separation for Vocal and Stem Extraction"
description: "Demucs is Meta’s open-source music source separation project for splitting songs into stems such as vocals, drums, bass, and accompaniment. It fits agent workflows that need repeatable audio preprocessing before transcription, remixing, analysis, captioning, or archive preparation."
slug: "demucs-music-source-separation-for-vocal-and-stem-extraction"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/facebookresearch/demucs"
tool_ecosystem:
  github_repo: "facebookresearch/demucs"
  github_stars: 9948
---

# Demucs Music Source Separation for Vocal and Stem Extraction

Demucs is Meta’s open-source music source separation project for splitting songs into stems such as vocals, drums, bass, and accompaniment. It fits agent workflows that need repeatable audio preprocessing before transcription, remixing, analysis, captioning, or archive preparation.

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
clawhub install demucs-music-source-separation-for-vocal-and-stem-extraction
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Demucs is a widely used open-source music source separation project from Meta Research. It provides pretrained models and a Python package that can split a full song into separate audio stems such as vocals, drums, bass, and other accompaniment. The repository documents both command-line usage and research context, and it links to sample outputs and papers describing the Hybrid Transformer Demucs architecture.
For agentic workflows, Demucs is valuable as an audio preparation step. An assistant can isolate vocals before speech-to-text, remove backing tracks for lyric review, create karaoke-style instrumental versions, or prepare cleaner source material for archival and editing pipelines. Because it is tool-driven rather than SaaS-only, it can be integrated into local media workflows, batch processing systems, or custom Python automations that already use PyTorch and torchaudio.
The upstream README documents installation with python3 -m pip install -U demucs and explains practical execution details, including audio format support through torchaudio and FFmpeg fallback notes on Windows. Even though the repository explicitly notes limited maintenance, it remains a real and heavily adopted upstream project with substantial community usage and research relevance. That makes it a strong fit for media-processing skill discovery where the job to be done is clear: split mixed music into usable stems for downstream automation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/demucs-music-source-separation-for-vocal-and-stem-extraction/)
