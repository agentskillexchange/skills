---
title: "Dolby.io Media Enhancer"
description: "Dolby.io Media Enhancer leverages Dolby’s cloud-based media processing APIs to improve audio and video quality programmatically. It uses the /media/enhance REST endpoint with Bearer token authentication to submit media files for processing.\nFor audio enhancement, the agent configures noise reduction with noise.reduction.amount: high, speech isolation, loudness normalization to EBU R128 (-23 LUFS) or ATSC A/85 standards, and dynamic range compression. It supports input formats including WAV, MP3, AAC, and OGG via presigned URL upload to Dolby’s /media/input endpoint.\nVideo enhancement includes automatic content-aware upscaling, color correction, and bandwidth optimization. The agent polls job status via /media/enhance?job_id={id} with configurable intervals and retrieves processed output from /media/output. Supports webhook callbacks for async pipeline integration. Includes batch processing mode for multiple files with job queuing and priority management."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/"
framework:
  - "Cursor"
---

# Dolby.io Media Enhancer

Dolby.io Media Enhancer leverages Dolby’s cloud-based media processing APIs to improve audio and video quality programmatically. It uses the /media/enhance REST endpoint with Bearer token authentication to submit media files for processing.
For audio enhancement, the agent configures noise reduction with noise.reduction.amount: high, speech isolation, loudness normalization to EBU R128 (-23 LUFS) or ATSC A/85 standards, and dynamic range compression. It supports input formats including WAV, MP3, AAC, and OGG via presigned URL upload to Dolby’s /media/input endpoint.
Video enhancement includes automatic content-aware upscaling, color correction, and bandwidth optimization. The agent polls job status via /media/enhance?job_id={id} with configurable intervals and retrieves processed output from /media/output. Supports webhook callbacks for async pipeline integration. Includes batch processing mode for multiple files with job queuing and priority management.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dolby-io-media-enhancer-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/dolby-io-media-enhancer-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/)
