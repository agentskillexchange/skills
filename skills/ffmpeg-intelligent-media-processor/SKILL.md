---
name: "FFmpeg Intelligent Media Processor"
description: "Orchestrates complex video and audio processing pipelines using FFmpeg and FFprobe with scene detection via PySceneDetect. Handles format conversion, thumbnail generation, HLS packaging, and loudness normalization per EBU R128."
category: "Image & Creative Automation"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ffmpeg-intelligent-media-processor/"
---
# FFmpeg Intelligent Media Processor

Orchestrates complex video and audio processing pipelines using FFmpeg and FFprobe with scene detection via PySceneDetect. Handles format conversion, thumbnail generation, HLS packaging, and loudness normalization per EBU R128.

FFmpeg Intelligent Media Processor is built around FFmpeg media processing toolkit. The underlying ecosystem is represented by FFmpeg/FFmpeg (58,257+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging and preserving the operational context that matters for real tasks.



In practice, the skill gives an agent a stable interface to ffmpeg so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Orchestrates complex video and audio processing pipelines using FFmpeg and FFprobe with scene detection via PySceneDetect. Handles format conversion, thumbnail generation, HLS packaging, and loudness normalization per EBU R128. The implementation typically relies on ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.



- Accesses ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging instead of scraping a UI, which makes runs easier to audit and retry.



- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.



- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.



- Fits into broader integration points such as audio/video pipelines, thumbnails, HLS, normalization, and format conversion.



Key integration points include audio/video pipelines, thumbnails, HLS, normalization, and format conversion. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-intelligent-media-processor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-intelligent-media-processor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-intelligent-media-processor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-intelligent-media-processor -a codex
```

### OpenClaw

```bash
clawhub install ffmpeg-intelligent-media-processor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-intelligent-media-processor/)
