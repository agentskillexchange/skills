---
title: "Dolby.io Media Enhancer"
description: "Dolby.io Media Enhancer leverages Dolby&#8217;s cloud-based media processing APIs to improve audio and video quality programmatically. It uses the /media/enhance REST endpoint with Bearer token authentication to submit media files for processing. For audio enhancement, the agent configures noise reduction with noise.reduction.amount: high , speech isolation, loudness normalization to EBU R128 (-23 LUFS) or ATSC A/85 standards, and dynamic range compression. It supports input formats including WAV, MP3, AAC, and OGG via presigned URL upload to Dolby&#8217;s /media/input endpoint. Video enhancement includes automatic content-aware upscaling, color correction, and bandwidth optimization. The agent polls job status via /media/enhance?job_id={id} with configurable intervals and retrieves processed output from /media/output . Supports webhook callbacks for async pipeline integration. Includes batch processing mode for multiple files with job queuing and priority management."
source: "https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Cursor"
---

# Dolby.io Media Enhancer

Dolby.io Media Enhancer leverages Dolby&#8217;s cloud-based media processing APIs to improve audio and video quality programmatically. It uses the /media/enhance REST endpoint with Bearer token authentication to submit media files for processing. For audio enhancement, the agent configures noise reduction with noise.reduction.amount: high , speech isolation, loudness normalization to EBU R128 (-23 LUFS) or ATSC A/85 standards, and dynamic range compression. It supports input formats including WAV, MP3, AAC, and OGG via presigned URL upload to Dolby&#8217;s /media/input endpoint. Video enhancement includes automatic content-aware upscaling, color correction, and bandwidth optimization. The agent polls job status via /media/enhance?job_id={id} with configurable intervals and retrieves processed output from /media/output . Supports webhook callbacks for async pipeline integration. Includes batch processing mode for multiple files with job queuing and priority management.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/)
