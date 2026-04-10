---
title: "FFmpeg Intelligent Media Processor"
description: "Orchestrates complex video and audio processing pipelines using FFmpeg and FFprobe with scene detection via PySceneDetect. Handles format conversion, thumbnail generation, HLS packaging, and loudness normalization per EBU R128."
slug: "ffmpeg-intelligent-media-processor"
category:
  - "Image &amp; Creative Automation"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ffmpeg-intelligent-media-processor/"
---

# FFmpeg Intelligent Media Processor

Orchestrates complex video and audio processing pipelines using FFmpeg and FFprobe with scene detection via PySceneDetect. Handles format conversion, thumbnail generation, HLS packaging, and loudness normalization per EBU R128.

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
clawhub install ffmpeg-intelligent-media-processor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

FFmpeg Intelligent Media Processor is built around FFmpeg media processing toolkit. The underlying ecosystem is represented by FFmpeg/FFmpeg (58,257+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to ffmpeg so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Orchestrates complex video and audio processing pipelines using FFmpeg and FFprobe with scene detection via PySceneDetect. Handles format conversion, thumbnail generation, HLS packaging, and loudness normalization per EBU R128. The implementation typically relies on ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as audio/video pipelines, thumbnails, HLS, normalization, and format conversion.
Key integration points include audio/video pipelines, thumbnails, HLS, normalization, and format conversion. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-intelligent-media-processor/)
