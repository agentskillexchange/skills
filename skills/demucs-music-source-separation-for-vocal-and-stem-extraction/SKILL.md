---
name: "Demucs Music Source Separation for Vocal and Stem Extraction"
slug: "demucs-music-source-separation-for-vocal-and-stem-extraction"
description: "Demucs is Meta's open-source music source separation project for splitting songs into stems such as vocals, drums, bass, and accompaniment. It fits agent workflows that need repeatable audio preprocessing before transcription, remixing, analysis, captioning, or archive preparation."
github_stars: 9949
verification: "security_reviewed"
source: "https://github.com/facebookresearch/demucs"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "facebookresearch/demucs"
  github_stars: 9949
---

# Demucs Music Source Separation for Vocal and Stem Extraction

Demucs is Meta's open-source music source separation project for splitting songs into stems such as vocals, drums, bass, and accompaniment. It fits agent workflows that need repeatable audio preprocessing before transcription, remixing, analysis, captioning, or archive preparation.

## Installation

Use the upstream install or setup path that matches your environment:
- conda env update -f environment-cpu.yml # if you don't have GPUs
- conda env update -f environment-cuda.yml # if you have GPUs
- conda activate demucs
- pip install -e .

Requirements and caveats from upstream:
- requires custom CUDA code that is not ready for release yet.
- You will need at least Python 3.8. See requirements_minimal.txt for requirements for separation only,
- Everytime you see python3, replace it with python.exe. You should always run commands from the

Basic usage or getting-started notes:
- and environment-[cpu|cuda].yml (or requirements.txt) if you want to train a new model.
- ### For Windows users
- Anaconda console.

- Source: https://github.com/facebookresearch/demucs
- Extracted from upstream docs: https://raw.githubusercontent.com/facebookresearch/demucs/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/demucs-music-source-separation-for-vocal-and-stem-extraction/)
