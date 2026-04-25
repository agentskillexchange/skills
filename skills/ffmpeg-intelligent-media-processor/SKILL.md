---
title: "FFmpeg Intelligent Media Processor"
description: "Orchestrates complex video and audio processing pipelines using FFmpeg and FFprobe with scene detection via PySceneDetect. Handles format conversion, thumbnail generation, HLS packaging, and loudness normalization per EBU R128."
verification: "security_reviewed"
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Image & Creative Automation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "ffmpeg/ffmpeg"
  github_stars: 58972
---

# FFmpeg Intelligent Media Processor

FFmpeg Intelligent Media Processor is built around FFmpeg media processing toolkit. The underlying ecosystem is represented by FFmpeg/FFmpeg (58,257+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging and preserving the operational context that matters for real tasks. In practice, the skill gives an agent a stable interface to ffmpeg so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Orchestrates complex video and audio processing pipelines using FFmpeg and FFprobe with scene detection via PySceneDetect. Handles format conversion, thumbnail generation, HLS packaging, and loudness normalization per EBU R128. The implementation typically relies on ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform. Accesses ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging instead of scraping a UI, which makes runs easier to audit and retry. Supports structured inputs and outputs so another tool, agent, or CI step can consume the result. Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format. Fits into broader integration points such as audio/video pipelines, thumbnails, HLS, normalization, and format conversion. Key integration points include audio/video pipelines, thumbnails, HLS, normalization, and format conversion. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/ffmpeg-intelligent-media-processor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ffmpeg-intelligent-media-processor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/ffmpeg-intelligent-media-processor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-intelligent-media-processor/)
