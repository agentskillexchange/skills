---
title: "Dolby.io Media Enhancer"
description: "Enhances audio and video quality using the Dolby.io Media Processing API. Applies noise reduction, loudness correction to EBU R128 standards, and dynamic range compression via the /media/enhance endpoint."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/"
category:
  - "Media & Transcription"
framework:
  - "Cursor"
---

# Dolby.io Media Enhancer

Dolby.io Media Enhancer leverages Dolby’s cloud-based media processing APIs to improve audio and video quality programmatically. It uses the /media/enhance REST endpoint with Bearer token authentication to submit media files for processing.


For audio enhancement, the agent configures noise reduction with noise.reduction.amount: high, speech isolation, loudness normalization to EBU R128 (-23 LUFS) or ATSC A/85 standards, and dynamic range compression. It supports input formats including WAV, MP3, AAC, and OGG via presigned URL upload to Dolby’s /media/input endpoint.


Video enhancement includes automatic content-aware upscaling, color correction, and bandwidth optimization. The agent polls job status via /media/enhance?job_id={id} with configurable intervals and retrieves processed output from /media/output. Supports webhook callbacks for async pipeline integration. Includes batch processing mode for multiple files with job queuing and priority management.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/)
