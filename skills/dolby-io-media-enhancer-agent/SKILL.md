---
title: Dolby.io Media Enhancer
description: 'Dolby.io Media Enhancer leverages Dolby’s cloud-based media processing
  APIs to improve audio and video quality programmatically. It uses the /media/enhance
  REST endpoint with Bearer token authentication to submit media files for processing.
  For audio enhancement, the agent configures noise reduction with noise.reduction.amount:
  high , speech isolation, loudness normalization to EBU R128 (-23 LUFS) or ATSC A/85
  standards, and dynamic range compression. It supports input formats including WAV,
  MP3, AAC, and OGG via presigned URL upload to Dolby’s /media/input endpoint. Video
  enhancement includes automatic content-aware upscaling, color correction, and bandwidth
  optimization. The agent polls job status via /media/enhance?job_id={id} with configurable
  intervals and retrieves processed output from /media/output . Supports webhook callbacks
  for async pipeline integration. Includes batch processing mode for multiple files
  with job queuing and priority management.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/
category:
- Media &amp; Transcription
framework:
- Cursor
---

# Dolby.io Media Enhancer

Dolby.io Media Enhancer leverages Dolby’s cloud-based media processing APIs to improve audio and video quality programmatically. It uses the /media/enhance REST endpoint with Bearer token authentication to submit media files for processing. For audio enhancement, the agent configures noise reduction with noise.reduction.amount: high , speech isolation, loudness normalization to EBU R128 (-23 LUFS) or ATSC A/85 standards, and dynamic range compression. It supports input formats including WAV, MP3, AAC, and OGG via presigned URL upload to Dolby’s /media/input endpoint. Video enhancement includes automatic content-aware upscaling, color correction, and bandwidth optimization. The agent polls job status via /media/enhance?job_id={id} with configurable intervals and retrieves processed output from /media/output . Supports webhook callbacks for async pipeline integration. Includes batch processing mode for multiple files with job queuing and priority management.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/)
