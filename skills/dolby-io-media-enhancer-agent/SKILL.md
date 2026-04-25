---
title: "Dolby.io Media Enhancer"
description: "Enhances audio and video quality using the Dolby.io Media Processing API. Applies noise reduction, loudness correction to EBU R128 standards, and dynamic range compression via the /media/enhance endpoint."
verification: "security_reviewed"
source: "https://optiview.dolby.com/docs/"
category:
  - "Media & Transcription"
framework:
  - "Cursor"
---

# Dolby.io Media Enhancer

Dolby.io Media Enhancer leverages Dolby’s cloud-based media processing APIs to improve audio and video quality programmatically. It uses the /media/enhance REST endpoint with Bearer token authentication to submit media files for processing. For audio enhancement, the agent configures noise reduction with noise.reduction.amount: high, speech isolation, loudness normalization to EBU R128 (-23 LUFS) or ATSC A/85 standards, and dynamic range compression. It supports input formats including WAV, MP3, AAC, and OGG via presigned URL upload to Dolby’s /media/input endpoint. Video enhancement includes automatic content-aware upscaling, color correction, and bandwidth optimization. The agent polls job status via /media/enhance?job_id={id} with configurable intervals and retrieves processed output from /media/output. Supports webhook callbacks for async pipeline integration. Includes batch processing mode for multiple files with job queuing and priority management.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dolby-io-media-enhancer-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/dolby-io-media-enhancer-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/)
