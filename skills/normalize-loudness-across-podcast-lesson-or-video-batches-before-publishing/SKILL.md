---
name: "Normalize loudness across podcast, lesson, or video batches before publishing"
slug: "normalize-loudness-across-podcast-lesson-or-video-batches-before-publishing"
description: "Uses ffmpeg-normalize to batch-normalize audio levels so an agent can hand off consistent output without opening a DAW or touching every file by hand. It fits pipelines that need EBU R128, RMS, or peak targets across mixed media before delivery."
github_stars: 1500
verification: "security_reviewed"
source: "https://github.com/slhck/ffmpeg-normalize"
author: "slhck"
publisher_type: "Open Source Project"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "slhck/ffmpeg-normalize"
  github_stars: 1500
---

# Normalize loudness across podcast, lesson, or video batches before publishing

Uses ffmpeg-normalize to batch-normalize audio levels so an agent can hand off consistent output without opening a DAW or touching every file by hand. It fits pipelines that need EBU R128, RMS, or peak targets across mixed media before delivery.

## Prerequisites

ffmpeg plus a Python or uv environment

## Installation

Requirements and caveats from upstream:
- [![Docker Image Version](https://img.shields.io/docker/v/slhck/ffmpeg-normalize?sort=semver&label=Docker%20image)](https://hub.docker.com/r/slhck/ffmpeg-normalize)
- ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/slhck/ffmpeg-normalize/python-package.yml)
- Docker support — Run via Docker container

Basic usage or getting-started notes:
- ## 🚀 Quick Start
- Run pip3 install ffmpeg-normalize and ffmpeg-normalize /path/to/your/file.mp4, alternatively install [uv](https://docs.astral.sh/uv/getting-started/installation/) and run uvx ffmpeg-normalize /path/to/your/file.mp4
- Example:

- Source: https://github.com/slhck/ffmpeg-normalize
- Extracted from upstream docs: https://raw.githubusercontent.com/slhck/ffmpeg-normalize/HEAD/README.md

## Documentation

- https://slhck.info/ffmpeg-normalize/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-loudness-across-podcast-lesson-or-video-batches-before-publishing/)
