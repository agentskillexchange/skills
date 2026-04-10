---
title: "Dolby.io Media Enhancer"
description: "Enhances audio and video quality using the Dolby.io Media Processing API. Applies noise reduction, loudness correction to EBU R128 standards, and dynamic range compression via the /media/enhance endpoint."
slug: "dolby-io-media-enhancer-agent"
category:
  - "Media &amp; Transcription"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/"
---

# Dolby.io Media Enhancer

Enhances audio and video quality using the Dolby.io Media Processing API. Applies noise reduction, loudness correction to EBU R128 standards, and dynamic range compression via the /media/enhance endpoint.

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
clawhub install dolby-io-media-enhancer-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Dolby.io Media Enhancer leverages Dolby’s cloud-based media processing APIs to improve audio and video quality programmatically. It uses the /media/enhance REST endpoint with Bearer token authentication to submit media files for processing.
For audio enhancement, the agent configures noise reduction with noise.reduction.amount: high, speech isolation, loudness normalization to EBU R128 (-23 LUFS) or ATSC A/85 standards, and dynamic range compression. It supports input formats including WAV, MP3, AAC, and OGG via presigned URL upload to Dolby’s /media/input endpoint.
Video enhancement includes automatic content-aware upscaling, color correction, and bandwidth optimization. The agent polls job status via /media/enhance?job_id={id} with configurable intervals and retrieves processed output from /media/output. Supports webhook callbacks for async pipeline integration. Includes batch processing mode for multiple files with job queuing and priority management.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/)
