---
name: "FFmpeg Audio Transcoder"
description: "Transcodes and processes audio files using the FFmpeg CLI and libavcodec library. Supports batch format conversion, loudness normalization via EBU R128, and metadata extraction with ffprobe."
category: "Media &amp; Transcription"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ffmpeg-audio-transcoder/"
---
# FFmpeg Audio Transcoder

Transcodes and processes audio files using the FFmpeg CLI and libavcodec library. Supports batch format conversion, loudness normalization via EBU R128, and metadata extraction with ffprobe.

FFmpeg Audio Transcoder is built around FFmpeg media processing toolkit. The underlying ecosystem is represented by FFmpeg/FFmpeg (58,257+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to ffmpeg so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Transcodes and processes audio files using the FFmpeg CLI and libavcodec library. Supports batch format conversion, loudness normalization via EBU R128, and metadata extraction with ffprobe. The implementation typically relies on ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses ffmpeg filters, ffprobe metadata, codecs, transcodes, frame extraction, packaging instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as audio/video pipelines, thumbnails, HLS, normalization, and format conversion.

Key integration points include audio/video pipelines, thumbnails, HLS, normalization, and format conversion. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-audio-transcoder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-audio-transcoder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-audio-transcoder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-audio-transcoder -a codex
```

### OpenClaw

```bash
clawhub install ffmpeg-audio-transcoder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-audio-transcoder/)
