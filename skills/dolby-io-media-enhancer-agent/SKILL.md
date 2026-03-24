---
name: "Dolby.io Media Enhancer"
description: "Enhances audio and video quality using the Dolby.io Media Processing API. Applies noise reduction, loudness correction to EBU R128 standards, and dynamic range compression via the /media/enhance endpoint."
category: "Media & Transcription"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/"
---

# Dolby.io Media Enhancer

Enhances audio and video quality using the Dolby.io Media Processing API. Applies noise reduction, loudness correction to EBU R128 standards, and dynamic range compression via the /media/enhance endpoint.

## Overview

Dolby.io Media Enhancer leverages Dolby’s cloud-based media processing APIs to improve audio and video quality programmatically. It uses the `/media/enhance` REST endpoint with Bearer token authentication to submit media files for processing.

For audio enhancement, the agent configures noise reduction with `noise.reduction.amount: high`, speech isolation, loudness normalization to EBU R128 (-23 LUFS) or ATSC A/85 standards, and dynamic range compression. It supports input formats including WAV, MP3, AAC, and OGG via presigned URL upload to Dolby’s `/media/input` endpoint.

Video enhancement includes automatic content-aware upscaling, color correction, and bandwidth optimization. The agent polls job status via `/media/enhance?job_id={id}` with configurable intervals and retrieves processed output from `/media/output`. Supports webhook callbacks for async pipeline integration. Includes batch processing mode for multiple files with job queuing and priority management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dolby-io-media-enhancer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dolby-io-media-enhancer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dolby-io-media-enhancer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dolby-io-media-enhancer-agent -a codex
```

### OpenClaw

```bash
clawhub install dolby-io-media-enhancer-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/dolby-io-media-enhancer-agent/
